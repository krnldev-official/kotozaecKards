from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from datetime import datetime, timedelta
import database as db
from cards_data import get_random_card

router = Router()
TRIGGERS = ["котоед", "cateater", "поймать котоеда", "котоед карту"]
@router.message(Command("cateater"))
@router.message(F.text.lower().in_(TRIGGERS))
async def cmd_cateater(message: types.Message):
    user_id = message.from_user.id
    _, points, coins, _, last_time_str = await db.get_user(user_id)
    if last_time_str:
        last_time = datetime.fromisoformat(last_time_str)
        time_passed = datetime.now() - last_time
        if time_passed < timedelta(hours=3):
            time_left = timedelta(hours=3) - time_passed
            hours, remainder = divmod(int(time_left.total_seconds()), 3600)
            minutes, _ = divmod(remainder, 60)
            await message.answer(
                f"Котоед пока не найден Вернись через <b>{hours} ч. {minutes} мин.</b>",
                parse_mode="HTML"
            )
            return
    card_id, won_card = get_random_card()
    await db.add_reward(user_id, won_card["points"], won_card["coins"], card_id, timer_type="last_komaru")
    
    _, new_points, new_coins, _, _ = await db.get_user(user_id)
    text = (
        f"Новая карточка - «<b>{won_card['name']}</b>»\n"
        f"<i>{won_card.get('description', '')}</i>\n\n"
        f"Редкость:  {won_card['rarity']}\n"
        f"Очки: {won_card['points']:,} [{new_points:,}]\n"
        f" Монеты: {won_card['coins']} [{new_coins}]\n\n"
        f"Следующая попытка через 3 часа"
    ).replace(",", ".")

    try:
        photo = FSInputFile(won_card['image'])
        await message.answer_photo(photo=photo, caption=text, parse_mode="HTML")
    except Exception:
        await message.answer(f"Карточка получена, но фото не найдено.Доложите админам!\n\n{text}", parse_mode="HTML")


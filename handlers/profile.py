from aiogram import Router, types
from aiogram.filters import Command
import database as db
from cards_data import CARDS

router = Router()

@router.message(Command("profile"))
async def cmd_profile(message: types.Message):
    user_id = message.from_user.id
    nickname, points, coins, _, _ = await db.get_user(user_id)
    inventory = await db.get_inventory(user_id)


    display_name = nickname if nickname else message.from_user.first_name

    text = f"<b>Профиль {display_name}</b>\n\n"
    text += f"Очки: {points:,}\n".replace(",", ".")
    text += f"Монеты: {coins:,}\n\n".replace(",", ".")
    
    if not inventory:
        text += "Твой инвентарь пуст. Используй /cateatet или /bonus!"
    else:
        text += "<b>Твои карты:</b>\n"
        for card_id, amount in inventory:
            card_info = CARDS.get(str(card_id)) or CARDS.get(card_id)
            if card_info:
                text += f"• {card_info['name']} ({card_info['rarity']}) — {amount} шт.\n"

    await message.answer(text, parse_mode="HTML")


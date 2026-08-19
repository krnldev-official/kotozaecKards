from aiogram import Router, types
from aiogram.filters import Command
import database as db

router = Router()

@router.message(Command("start", "help"))
async def cmd_start(message: types.Message):
    await db.get_user(message.from_user.id)
    
    text = (
        "<b>Что это за бот?</b>\n"
        "Ты можешь собиратт карточки\n\n"
        "<b>Команды</b>\n"
        "/profile — ваш профиль\n"
        "/name [ник] — изменить никнейм\n"
        "/cateater — получатт котов\n"
        "/top — топ игроков\n"
        "/premium — приобрести п....[недоступно]\n"
        "/bonus — получить бонус\n"
    )
    await message.answer(text, parse_mode="HTML")


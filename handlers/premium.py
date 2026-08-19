from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("premium"))
async def cmd_premium(message: types.Message):
    text = (
        " <b>Приобретение Premium статуса</b>\n\n"
        "Что дает Premium:\n"
        " Увеличенные награды с /cateater и /bonus\n"
        " Уменьшенное время перезарядки команд\n"
        "<i>Пока недоступна! LinuxAngel добавит потом!</i>"
    )
    await message.answer(text, parse_mode="HTML")


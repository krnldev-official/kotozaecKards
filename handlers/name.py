from aiogram import Router, types
from aiogram.filters import Command
import database as db
router = Router()
@router.message(Command("name"))
async def cmd_name(message: types.Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer(
            "Использование команды\nОтправьте /name [ник]\nНапример: <code>/name murchalkaPidorasTupoy</code>", 
            parse_mode="HTML"
        )
        return
        
    new_name = args[1][:20]
    await db.update_nickname(message.from_user.id, new_name)
    
    await message.answer(f"Ваш никнейм  изменен на: <b>{new_name}</b>", parse_mode="HTML")


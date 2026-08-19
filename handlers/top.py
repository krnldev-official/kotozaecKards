from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import database as db

router = Router()

top_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="По очкам", callback_data="top_points")],
    [InlineKeyboardButton(text="По монетам", callback_data="top_coins")]
])

@router.message(Command("top"))
async def cmd_top(message: types.Message):
    await message.answer("🏆 <b>Топ 10 игроков</b>\nВыберите по какому значению показать топ:", reply_markup=top_kb, parse_mode="HTML")

@router.callback_query(F.data.startswith("top_"))
async def process_top_callback(callback: types.CallbackQuery):
    order_by = callback.data.split("_")[1] 
    top_players = await db.get_top(order_by=order_by, limit=10)
    title = "очкам" if order_by == "points" else "монетам"
    icon = "✨" if order_by == "points" else "💰"
    
    text = f"🏆 <b>Топ 10 по {title}:</b>\n\n"
    
    if not top_players:
        text += "Топ пока пуст."
    else:
        for i, (nickname, user_id, value) in enumerate(top_players, 1):
            name = nickname if nickname else f"ID: {user_id}"
            text += f"<b>{i}.</b> {name} — {value:,} {icon}\n".replace(",", ".")
    await callback.message.edit_text(text, reply_markup=top_kb, parse_mode="HTML")


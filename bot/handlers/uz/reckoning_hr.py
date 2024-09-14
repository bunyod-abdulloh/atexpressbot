from aiogram import Router, F, types

from loader import db

router = Router()


@router.message(F.text == "🧮 Hisoblar")
async def reckoning_first_rtr(message: types.Message):
    telegram_id = message.from_user.id
    user = await db.select_user(
        telegram_id=telegram_id
    )
    await message.answer(
        text=f"🆔 raqam: {user['id']}\n"
             f"Foydalanuvchi: {user['full_name']}\n"
             f"Telefon raqam: {user['phone']}\n"
             f"Manzil: {user['address']}\n"
             f"Balans: {user['balance']}"
    )

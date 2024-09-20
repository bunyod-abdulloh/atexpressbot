from aiogram import Router, types
from aiogram.filters import CommandStart

from bot.keyboards.reply.users_dkb import select_language_dkb
from loader import db

router = Router()


@router.message(CommandStart())
async def start_rtr(message: types.Message):
    try:
        await db.add_user(
            telegram_id=message.from_user.id, full_name=message.from_user.full_name
        )
    except:
        pass
    await message.answer(
        text="Tilni tanlang", reply_markup=select_language_dkb
    )

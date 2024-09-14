from aiogram import Router, types
from aiogram.filters import CommandStart

from bot.keyboards.reply.users_dkb import select_language_dkb

router = Router()


@router.message(CommandStart())
async def start_rtr(message: types.Message):
    await message.answer(
        text="Tilni tanlang", reply_markup=select_language_dkb
    )

from aiogram import Router, types, F
from aiogram.filters import CommandStart

from bot.keyboards.reply.main_dkb import uzmain_start_dkb, uzmain_dkb

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message, i18n):
    full_name = message.from_user.full_name

    await message.answer(
        text=i18n.gettxt("start"))


@router.message(F.text == "🏡 Bosh sahifa")
async def back_main_menu(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=uzmain_dkb
    )

from aiogram import Router, types, F

from bot.keyboards.reply.users_dkb import main_dkb, select_language_dkb
from data.jsonfiles.uz import uz_dict

router = Router()


@router.message(F.text == "🇺🇿 O'zbek")
async def main_hr(message: types.Message):
    await message.answer(
        text=uz_dict["main_menu"], reply_markup=main_dkb(
            texts=uz_dict["main_buttons"]
        )
    )


@router.message(F.text == "🏡 Bosh sahifa")
async def back_main_menu(message: types.Message):
    await message.answer(
        text=message.text
    )


@router.message(F.text == "⬅️ Ortga")
async def back_to_main_menu(message: types.Message):
    await message.answer(
        text="Tilni tanlang", reply_markup=select_language_dkb
    )

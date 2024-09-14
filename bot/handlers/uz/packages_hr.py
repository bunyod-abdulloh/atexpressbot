from aiogram import Router, F, types

from bot.keyboards.reply.users_dkb import second_main_dkb, main_dkb
from data.languages.uz import uz_dict

router = Router()


@router.message(F.text == "📦 Jo'natmalar")
async def up_to_first_rtr(message: types.Message):
    await message.answer(
        text=uz_dict["main_menu"], reply_markup=second_main_dkb(
            texts=uz_dict['up_to_main']
        )
    )


@router.message(F.text == "30 kg dan ko'p bo'lgan jo'natmalar")
async def more_packages_rtr(message: types.Message):
    await up_to_first_rtr(
        message=message
    )


@router.message(F.text == "◀️ Ortgа")
async def up_to_back_uz(message: types.Message):
    await message.answer(
        text=uz_dict["main_menu"], reply_markup=main_dkb(
            texts=uz_dict['main_buttons']
        )
    )

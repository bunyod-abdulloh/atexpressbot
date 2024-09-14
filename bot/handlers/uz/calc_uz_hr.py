from aiogram import F, types, Router

from bot.keyboards.reply.users_dkb import countries_dkb, second_main_dkb
from data.jsonfiles.uz import uz_dict

router = Router()


@router.message(F.text == "🧮 Kalkulator")
async def calculator_rtr(message: types.Message):
    await message.answer(
        text=uz_dict['calc_text'], reply_markup=countries_dkb(
            texts=uz_dict['calc_main']
        )
    )


@router.message(F.text == "⏮ Ortga")
async def back_calc_rtr(message: types.Message):
    await message.answer(
        text=uz_dict['main_menu'], reply_markup=second_main_dkb(
            texts=uz_dict['up_to_main']
        )
    )

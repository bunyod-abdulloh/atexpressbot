from aiogram import F, types, Router

from bot.keyboards.reply.users_dkb import countries_dkb
from data.languages.uz import uz_dict

router = Router()


@router.message(F.text == "🧮 Kalkulator")
async def calculator_rtr(message: types.Message):
    await message.answer(
        text=uz_dict['calc_text'], reply_markup=countries_dkb(
            texts=uz_dict['calc_main']
        )
    )


@router.message(F.text.in_(uz_dict['calc_countries']))
async def calc_country_rtr(message: types.Message):
    country = message.text.split(' ')[1]
    await message.answer(
        text=f"{country}{uz_dict['calc_country_text']}"
    )

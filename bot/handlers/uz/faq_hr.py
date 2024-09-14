from aiogram import Router, F, types

from bot.keyboards.reply.users_dkb import faq_dkb, second_main_dkb
from data.jsonfiles.uz import uz_dict

router = Router()


@router.message(F.text == "⁉️ FAQ va maslahatlar")
async def faq_uz_rtr(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=faq_dkb(
            texts=uz_dict['faq']
        )
    )


@router.message(F.text == "📝 Yetkazib berishni rasmiylashtirish")
async def delivery_faq_uz_rtr(message: types.Message):
    await message.answer(
        text=message.text
    )


@router.message(F.text == "🛃 Bojxonadan o'tish")
async def customs_faq_uz_rtr(message: types.Message):
    await message.answer(
        text=message.text
    )


@router.message(F.text == "📖 Reklamatsiya siyosati")
async def advertising_faq_uz_rtr(message: types.Message):
    await message.answer(
        text=message.text
    )


@router.message(F.text == "◀️ Ortga")
async def back_faq_uz_rtr(message: types.Message):
    await message.answer(
        text=uz_dict['main_menu'], reply_markup=second_main_dkb(
            texts=uz_dict['up_to_main']
        )
    )

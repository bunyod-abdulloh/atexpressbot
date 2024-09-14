from aiogram import Router, F, types

from bot.keyboards.reply.users_dkb import second_main_dkb
from data.jsonfiles.uz import uz_dict

router = Router()


@router.message(F.text == "30 kg gacha bo'lgan jo'natmalar")
async def up_to_first_rtr(message: types.Message):
    await message.answer(
        text=uz_dict["main_menu"], reply_markup=second_main_dkb(
            texts=uz_dict['up_to_main']
        )
    )

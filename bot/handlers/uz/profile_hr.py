from aiogram import Router, F, types

from bot.keyboards.reply.users_dkb import profile_dkb
from data.languages.uz import uz_profile_buttons

router = Router()


@router.message(F.text == "👤 Profil")
async def profile_uz_rtr(message: types.Message):
    await message.answer(
        text="Sizning profilingiz", reply_markup=profile_dkb(
            texts=uz_profile_buttons
        )
    )

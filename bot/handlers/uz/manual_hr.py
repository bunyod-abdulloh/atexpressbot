from aiogram import Router, F, types

router = Router()


@router.message(F.text == "ℹ️ Qo'llanma")
async def about_info_uz(message: types.Message):
    await message.answer(
        text="Bot bo'yicha qo'llanma hozircha tayyor bo'lmadi!"
    )

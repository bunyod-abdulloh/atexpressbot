from aiogram import Router, F, types

router = Router()


@router.message(F.text == "📌 Tariflar")
async def tarifs_uz_rtr(message: types.Message):
    await message.answer(
        text=message.text
    )

from aiogram import Router, F, types

router = Router()


@router.message(F.text == "🚀 Treking")
async def treking_uz_rtr(message: types.Message):
    await message.answer(
        text="Trek raqamini yuboring"
    )

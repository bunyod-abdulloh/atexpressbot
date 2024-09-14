from aiogram import Router, F, types

router = Router()


@router.message(F.text == "📲 Operator bilan bog'lanish")
async def call_to_admin_uz_rtr(message: types.Message):
    await message.answer(
        text="Tez orada operatorlarimiz Siz bilan bog'lanadilar!"
    )

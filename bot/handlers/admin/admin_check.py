from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from bot.keyboards.inline.admin_ikb import admin_check_second_ikb
from bot.states import AdminState
from loader import bot

router = Router()


@router.callback_query(F.data.startswith("admincheck_yes:"))
async def admincheck_yes_rtr(call: types.CallbackQuery):
    user_id = call.data.split(':')[1]
    user_shop_id = call.data.split(':')[2]
    await bot.send_message(
        chat_id=user_id,
        text=f"Sizning ID olish so'rovingiz tasdiqlandi!\n\nID raqamingiz: <code>{user_shop_id}</code>"
             f"\n\nManzilni <b>📍 Manzil olish</b> tugmasi orqali olishingiz mumkin!"
    )
    await call.message.edit_text(
        text="Habar foydalanuvchiga yuborildi!"
    )


@router.callback_query(F.data.startswith("admincheck_no:"))
async def admincheck_no_rtr(call: types.CallbackQuery, state: FSMContext):
    user_id = call.data.split(":")[1]
    await state.update_data(
        user_id_=user_id,
        admin_check_no_msg_id=call.message.message_id
    )
    await call.message.edit_text(
        text="Rad etilish sababini kiriting:"
    )
    await state.set_state(AdminState.check_no)


@router.message(AdminState.check_no)
async def check_no_rtr(message: types.Message, state: FSMContext):
    await state.update_data(
        admin_disclaimer=message.text
    )
    await message.answer(
        text="Habaringizni tasdiqlaysizmi?", reply_markup=admin_check_second_ikb
    )


@router.callback_query(F.data == "admincheck_second_yes")
async def admincheck_second_yes_rtr(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data.get("user_id_")
    admin_disclaimer = data.get("admin_disclaimer")

    await bot.send_message(
        chat_id=user_id,
        text=f"Sizning ID olish so'rovingiz rad etildi!\n\n<b>Sabab:</b>\n{admin_disclaimer}\n\nIltimos, so'rovingizni "
             f"qayta yuboring!"
    )
    await call.message.edit_text(
        text="Habar foydalanuvchiga yuborildi!"
    )
    await state.clear()


@router.callback_query(F.data == "admincheck_second_no")
async def admincheck_second_no_rtr(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        text="Habaringizni qayta kiriting:"
    )
    await state.set_state(AdminState.check_no)

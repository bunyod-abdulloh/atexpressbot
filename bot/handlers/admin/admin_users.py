import asyncio
import logging

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from bot.filters import IsBotAdminFilter
from bot.keyboards.inline.users_ikb import are_you_sure_markup
from bot.keyboards.reply.admin_dkb import admin_users_dkb
from bot.states import AdminState
from data.config import ADMINS
from loader import db, bot

router = Router()


@router.message(IsBotAdminFilter(ADMINS), F.text == "Foydalanuvchilar bo'limi")
async def users_router(message: types.Message):
    await message.answer(
        text="Foydalanuvchilar bo'limi", reply_markup=admin_users_dkb
    )


@router.message(IsBotAdminFilter(ADMINS), F.text == "Foydalanuvchilar soni")
async def users_count_router(message: types.Message):
    users_count = await db.count_users()
    await message.answer(
        text=f"Foydalanuvchilar soni: {users_count}"
    )


@router.message(F.text == "Habar yuborish", IsBotAdminFilter(ADMINS))
async def ask_ad_content(message: types.Message, state: FSMContext):
    await message.answer(
        text="Habar matnini yuboring"
    )
    await state.set_state(
        state=AdminState.ask
    )


@router.message(AdminState.ask, IsBotAdminFilter(ADMINS))
async def send_to_users(message: types.Message, state: FSMContext):
    await message.answer(
        text="Habaringizni tasdiqlaysizmi?", reply_markup=are_you_sure_markup
    )
    await state.update_data(
        admin_message=message.text
    )
    await state.set_state(
        state=AdminState.send_to_users
    )


@router.callback_query(AdminState.send_to_users)
async def send_ad_to_users(call: types.CallbackQuery, state: FSMContext):
    if call.data == "yes":
        data = await state.get_data()
        message_text = data.get("admin_message")
        users = await db.select_all_users()
        count = 0
        for user in users:
            user_id = user[3]
            try:
                await bot.send_message(
                    chat_id=user_id,
                    text=message_text
                )
                count += 1
                await asyncio.sleep(0.05)
            except Exception as error:
                await db.delete_user(
                    telegram_id=user_id
                )
                await db.delete_ayztemptemp(
                    telegram_id=user_id
                )
                await db.delete_user_yaxintemporary(
                    telegram_id=user_id
                )
                await db.delete_leotemp(
                    telegram_id=user_id
                )
                logging.info(f"Ad did not send to user: {user_id}. Error: {error}")
        await call.message.answer(
            text=f"Habar {count} ta foydalanuvchiga muvaffaqiyatli yuborildi."
        )
        await state.clear()

    elif call.data == "no":
        await call.message.edit_text(
            text="Habar yuborish bekor qilindi."
        )
        await state.clear()

import os

from aiogram import Router, F, types

from bot.filters import IsBotAdminFilter
from bot.keyboards.reply.admin_dkb import admin_download_dkb
from data.config import ADMINS
from loader import db
from utils.pgtoexcel import export_to_excel

router = Router()


@router.message(IsBotAdminFilter(ADMINS), F.text == "Excel yuklab olish")
async def download_router(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=admin_download_dkb
    )


@router.message(IsBotAdminFilter(ADMINS), F.text == "Foydalanuvchilar yuklash")
async def upload_users_router(message: types.Message):
    users = await db.select_all_users()

    file_path = f"data/foydalanuvchilar.xlsx"
    await export_to_excel(data=users, headings=['ID', 'Full Name', 'Username', 'Telegram ID'], filepath=file_path)

    await message.answer_document(types.input_file.FSInputFile(file_path))
    os.remove(file_path)

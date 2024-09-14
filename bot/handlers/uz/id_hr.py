from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from bot.keyboards.inline.admin_ikb import admin_check_ikb
from bot.keyboards.inline.users_ikb import get_id_ikeys
from bot.states.user_states import UserAnketa
from data.config import ADMINS
from loader import db, bot

router = Router()


@router.message(F.text == "🆔 ID olish")
async def get_iduz_rtr(message: types.Message):
    await message.answer(
        text="Siz oldin bizdan ID raqam olganmisiz?", reply_markup=get_id_ikeys()
    )


@router.callback_query(F.data == "get_iduz_yes")
async def get_iduz_yes_rtr(call: types.CallbackQuery):
    pass


@router.callback_query(F.data == "get_iduz_no")
async def get_iduz_no_rtr(call: types.CallbackQuery, state: FSMContext):
    await db.add_user(
        username=call.from_user.username, telegram_id=call.from_user.id
    )
    await call.message.edit_text(
        text="Ism va familiyangizni kiriting:\n\n<b>(Namuna: Kimdir Kimdirov)</b>"
    )
    await state.set_state(UserAnketa.addfullname)


@router.message(UserAnketa.addfullname)
async def addfullname_rtr(message: types.Message, state: FSMContext):
    await db.update_user_fullname(
        fullname=message.text, telegram_id=message.from_user.id
    )
    await message.answer(
        text="Telefon raqamingizni kiriting:\n\n<b>(Namuna: +998991234567)</b>"
    )
    await state.set_state(UserAnketa.addphone)


@router.message(UserAnketa.addphone)
async def addphone_rtr(message: types.Message, state: FSMContext):
    await db.update_user_phone(
        phone=message.text, telegram_id=message.from_user.id
    )
    await message.answer(
        text="Manzilingizni kiriting:\n\n<b>(Namuna: Toshkent sh, Chilonzor 16-mavze, 20-uy, 65-honadon)</b>"
    )
    await state.set_state(UserAnketa.addaddress)


@router.message(UserAnketa.addaddress)
async def addaddress_rtr(message: types.Message, state: FSMContext):
    await db.update_user_address(
        address=message.text, telegram_id=message.from_user.id
    )
    await message.answer(
        text="Pasportingizni old tomoni rasmini yuboring.\n\n<b>Eslatma!!!\n\nRasm tiniq, barcha yozuvlar "
             "ko'rinadigan va tushunadigan darajada bo'lishi lozim!</b>"
    )
    await state.set_state(UserAnketa.passport_a_side)


@router.message(UserAnketa.passport_a_side, F.photo)
async def passport_a_side_rtr(message: types.Message, state: FSMContext):
    await db.update_user_passport_a_side(
        passport_a_side=message.photo[-1].file_id, telegram_id=message.from_user.id
    )
    await message.answer(
        text="Pasportingizni orqa tomoni rasmini yuboring.\n\n<b>Eslatma!!!\n\nRasm tiniq, barcha yozuvlar "
             "ko'rinadigan va tushunadigan darajada bo'lishi lozim!</b>"
    )
    await state.set_state(UserAnketa.passport_b_side)


@router.message(UserAnketa.passport_b_side, F.photo)
async def passport_b_side_rtr(message: types.Message, state: FSMContext):
    await db.update_user_passport_b_side(
        passport_b_side=message.photo[-1].file_id, telegram_id=message.from_user.id
    )
    user = await db.select_user(
        telegram_id=message.from_user.id
    )

    user_datas = (f"Yangi foydalanuvchi ma'lumotlari qabul qilindi!\n\n"
                  f"Ism familiya: {user['full_name']}\n"
                  f"Telefon raqam: {user['phone']}\n"
                  f"Manzil: {user['address']}\n")

    album = []
    passport_a_side = types.InputMediaPhoto(media=user['passport_a_side'])
    passport_b_side = types.InputMediaPhoto(media=user['passport_b_side'], caption=user_datas)
    album.append(passport_a_side)
    album.append(passport_b_side)

    await bot.send_media_group(
        chat_id=ADMINS[0],
        media=album)
    await bot.send_message(
        chat_id=ADMINS[0],
        text="Ma'lumotlarni tasdiqlaysizmi?", reply_markup=admin_check_ikb(
            user_id=user['telegram_id'], user_shop_id=user['id']
        )
    )
    await message.answer(
        text="Ma'lumotlaringiz adminga yuborildi! Tez orada xabar beramiz!"
    )
    await state.clear()

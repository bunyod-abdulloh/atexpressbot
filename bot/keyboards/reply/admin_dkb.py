from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_main_dkb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Web adminka"),
            KeyboardButton(text="Foydalanuvchilar bo'limi")
        ],
        [
            KeyboardButton(text="Excel yuklab olish")
        ],
        [
            KeyboardButton(text="🏡 Bosh sahifa")
        ]
    ],
    resize_keyboard=True
)

admin_users_dkb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foydalanuvchilar soni"),
            KeyboardButton(text="Habar yuborish")
        ],
        [
            KeyboardButton(text="Admin bosh sahifasi")
        ]
    ],
    resize_keyboard=True
)

admin_download_dkb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar"),
            KeyboardButton(text="Dars va kurslar jadvali")
        ],
        [
            KeyboardButton(text="Maqolalar"),
            KeyboardButton(text="Suhbat va loyihalar")
        ],
        [
            KeyboardButton(text="Foydalanuvchilar yuklash")
        ],
        [
            KeyboardButton(text="Admin bosh sahifasi")
        ]
    ]
)

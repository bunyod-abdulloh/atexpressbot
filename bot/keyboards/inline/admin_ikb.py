from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def admin_check_ikb(user_id, user_shop_id):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="✅ Ha", callback_data=f"admincheck_yes:{user_id}:{user_shop_id}")
        ],
            [
                InlineKeyboardButton(text="❌ Yo'q", callback_data=f"admincheck_no:{user_id}")
            ]
        ]
    )
    return markup


admin_check_second_ikb = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Ha", callback_data=f"admincheck_second_yes")
    ],
        [
            InlineKeyboardButton(text="❌ Yo'q", callback_data=f"admincheck_second_no")
        ]
    ]
)

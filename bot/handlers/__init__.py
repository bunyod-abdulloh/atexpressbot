from aiogram import Router

from bot.filters import ChatPrivateFilter


def setup_routers() -> Router:
    from .uz import (main_hr, id_hr)
    from .errors import error_handler
    from .admin import admin_main, admin_users, admin_downloads, admin_check

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    main_hr.router.message.filter(ChatPrivateFilter(chat_type=["private"]))
    #  Users
    router.include_routers(main_hr.router, id_hr.router)
    # Admins
    router.include_routers(admin_main.router, admin_users.router, admin_downloads.router, admin_check.router)
    return router

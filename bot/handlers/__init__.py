from aiogram import Router

from bot.filters import ChatPrivateFilter


def setup_routers() -> Router:
    from .users import start_hr
    from .uz import (main_hr, id_hr, up_to_hr, calc_uz_hr)
    from .errors import error_handler
    from .admin import admin_main, admin_users, admin_downloads, admin_check

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    main_hr.router.message.filter(ChatPrivateFilter(chat_type=["private"]))
    #  Users
    router.include_routers(start_hr.router, main_hr.router, id_hr.router, up_to_hr.router, calc_uz_hr.router)
    # Admins
    router.include_routers(admin_main.router, admin_users.router, admin_downloads.router, admin_check.router)
    return router

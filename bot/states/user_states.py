from aiogram.filters.state import StatesGroup, State


class UserAnketa(StatesGroup):
    addfullname = State()
    addphone = State()
    addaddress = State()
    passport_a_side = State()
    passport_b_side = State()

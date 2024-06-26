from aiogram.fsm.state import StatesGroup, State


class RegisterForm(StatesGroup):
    company_name = State()
    employee_number = State()
    lifetime = State()
    company_employee_name = State()
    company_contact = State()

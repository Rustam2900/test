from aiogram.fsm.context import FSMContext

from aiogram import Router, F, types

from kb_buuton import shaxs, contact_user
from state_ import RegisterForm

router = Router()


@router.message(F.text == '🇺🇿')
async def lang_uz(message: types.Message):
    await message.answer(text='Harakatni tanlang 〽️:', reply_markup=shaxs())


@router.message(F.text == 'yuridikt shaxs')
async def legal_entity(message: types.Message, state: FSMContext):
    await state.set_state(RegisterForm.company_name)
    await message.answer("Kompaniya nomini kiriting:")


@router.message(RegisterForm.company_name)
async def process_company_name(message: types.Message, state: FSMContext):
    await state.update_data(company_name=message.text)
    await state.set_state(RegisterForm.employee_number)
    await message.answer("Xodimlar sonini kiriting:")


@router.message(RegisterForm.employee_number)
async def process_employee_number(message: types.Message, state: FSMContext):
    await state.update_data(employee_number=int(message.text))
    await state.set_state(RegisterForm.lifetime)
    await message.answer("Davomiyligini (kunlarda) kiriting:")


@router.message(RegisterForm.lifetime)
async def process_lifetime(message: types.Message, state: FSMContext):
    await state.update_data(lifetime=int(message.text))
    data = await state.get_data()

    # Hisob-kitoblarni amalga oshiramiz
    employees = data['employee_number']
    days = data['lifetime']
    water_per_day_per_employee = 2  # 1 xodim uchun kuniga 2 litr suv
    workdays_per_week = 5

    if days < 7:
        total_workdays = days
    else:
        weeks = days // 7
        remaining_days = days % 7
        total_workdays = weeks * workdays_per_week + min(remaining_days, workdays_per_week)

    total_water_per_day = employees * water_per_day_per_employee
    total_water_needed = total_water_per_day * total_workdays

    advice = f"Sizga maslahat: {days} kunga {total_water_needed / 20:.0f} ta 20 L suv buyurtma bersangiz bo'ladi."
    await message.answer(advice)
    await state.set_state(RegisterForm.company_employee_name)
    await message.answer("Kompaniya xodimining ismini kiriting:")


@router.message(RegisterForm.company_employee_name)
async def process_company_employee_name(message: types.Message, state: FSMContext):
    await state.update_data(company_employee_name=message.text)
    await state.set_state(RegisterForm.company_contact)
    await message.answer("Kompaniya kontakt ma'lumotlarini kiriting tugmani bosing:", reply_markup=contact_user())


@router.message(RegisterForm.company_contact)
async def process_company_contact(message: types.Message, state: FSMContext):
    contact = message.contact.phone_number
    await state.update_data(number=contact)
    print(contact)
    await state.update_data(company_contact=message.text)
    data = await state.get_data()

    # Hamma kiritilgan ma'lumotlarni chiqaramiz
    result = (f"Kompaniya nomi: {data['company_name']}\n"
              f"Xodimlar soni: {data['employee_number']}\n"
              f"Davomiylik: {data['lifetime']} kun\n"
              f"Kompaniya xodimining ismi: {data['company_employee_name']}\n"
              f"Kontakt ma'lumotlari: {contact}")

    await message.reply("Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!\n" + result)
    await state.clear()

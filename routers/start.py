from aiogram import Router
from aiogram.filters import CommandStart

from aiogram import types

from kb_buuton import lang_change

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(text="Salom botga xush kelibsiz tilnii tanlang", reply_markup=lang_change())


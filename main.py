import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, Router, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import TOKEN
from routers.start import router as start_router
from routers.order import router as order_router

router = Router()
router.include_router(start_router)
router.include_router(order_router)

bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main() -> None:
    dp = Dispatcher()

    commands = [
        types.BotCommand(command="start", description="botga ishga tushurish uchun bosing")
    ]
    dp.include_router(router)
    await bot.set_my_commands(commands)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

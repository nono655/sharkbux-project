import asyncio

from aiogram import Bot, Dispatcher

from bot.config import TOKEN
from bot.handlers import router
from bot.server import start_server


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    await asyncio.gather(dp.start_polling(bot), start_server())


if __name__ == "__main__":
    asyncio.run(main())

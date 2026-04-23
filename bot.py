import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = '7984683232:AAHWb6fdOK9g_IPDNJFVESFMNXGvv757pTU'
WEB_APP_URL = "https://sharkbox-app.vercel.app"

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def welcome(message: types.Message):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="فتح تطبيق SharkBox 🦈", web_app=WebAppInfo(url=WEB_APP_URL))]
        ])
        await message.answer(f"أهلاً يا {message.from_user.first_name} في SharkBox! 🦈", reply_markup=keyboard)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

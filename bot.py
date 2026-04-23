import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiohttp import web

TOKEN = '7984683232:AAHWb6fdOK9g_IPDNJFVESFMNXGvv757pTU'
# سيتم استبدال هذا الرابط لاحقاً برابط Vercel الخاص بك
WEB_APP_URL = "https://sharkbux-project.vercel.app"

# سطر برمجي لفتح منفذ وهمي لكي يقبله موقع Render المجاني
async def handle(request):
    return web.Response(text="SharkBox is Active!")

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def welcome(message: types.Message):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="فتح تطبيق SharkBox 🦈", web_app=WebAppInfo(url=WEB_APP_URL))]
        ])
        await message.answer(f"أهلاً يا {message.from_user.first_name} في SharkBox! 🦈", reply_markup=keyboard)

    # إعداد السيرفر ليتوافق مع سياسة Render المجانية
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    
    # تشغيل البوت والسيرفر معاً
    await asyncio.gather(dp.start_polling(bot), site.start())

if __name__ == '__main__':
    asyncio.run(main())
  

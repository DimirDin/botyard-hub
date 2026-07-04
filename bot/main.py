import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, MenuButtonWebApp

BOT_TOKEN = os.environ["BOT_TOKEN"]
MINI_APP_URL = os.environ.get("MINI_APP_URL", "https://hub.botyard.site")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎛 Открыть пункт управления", web_app={"url": MINI_APP_URL})],
    ])
    await message.answer(
        "Пункт управления ботами platform botyard.site.\n\n"
        "Здесь — переходы во все действующие боты платформы и форма обратной связи "
        "напрямую разработчику.",
        reply_markup=kb,
    )


async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.set_chat_menu_button(menu_button=MenuButtonWebApp(text="Пункт управления", web_app={"url": MINI_APP_URL}))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

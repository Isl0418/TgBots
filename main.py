from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ContentType, Contact
from core.handlers.basic import get_start, get_photo, get_hello
import asyncio
import logging
from core.settings import settings
from aiogram.filters import Command
from aiogram import F
from core.utils.commands import set_commands
from core.handlers.basic import get_location
from aiogram.enums import ContentType
# from core.handlers.contact import get_fake_contact, get_true_contact
from core.handlers.basic import get_inline

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Bot is working')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot stopped the work')



async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_inline, Command(commands='inline'))
    # dp.message.register(get_photo, ContentTypesFilter(content_types=[ContentType.PHOTO]))
    # dp.name.register(get_true_contact, F.contact, F.content_type == ContentType)
    # dp.register_message_handler(get_true_contact, content_types=types.ContentType.CONTACT)

    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == "Hello")

    dp.message.register(get_start, Command(commands=['start', 'run']))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())


import config
import logging
import aiogram

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.info)

bot = Bot(token=config.token)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

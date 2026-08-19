import asyncio
import logging
from aiogram import Bot, Dispatcher
import config
import database
from handlers import routers
async def main():
    logging.basicConfig(level=logging.INFO)
    await database.init_db()
    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()
    for router in routers:
        dp.include_router(router)   
    print("Бот успешно запущен ")
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())

import config
import logging
from anime import anime_list, check_last_anime_ser, update_last_anime_ser, get_users, get_voice

from parcerV1 import parce_new

from aiogram import Bot, Dispatcher
import asyncio

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


async def updates_of_sers():
    print('Update')
    for us in get_users():
        print(us)
        for an in anime_list(us):
            print(an)
            k = check_last_anime_ser(us, an)
            v = get_voice(us, an)
            read, k = parce_new(an, k, v)
            if read.isdigit() == False:
                await bot.send_message(us, an + '\n' + read)
                update_last_anime_ser(an, k, us)


if __name__ == '__main__':
    asyncio.run(updates_of_sers())

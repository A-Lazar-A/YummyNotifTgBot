import config
import logging
from anime import add_anime, anime_list, delete_anime, add_voice

from parcerV1 import parce_name

from aiogram import Bot, Dispatcher, executor, types




logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def start(message: types.Message):
	return await message.answer("Введите /add 'ссылка на аниме' - чтобы добавить аниме в ваш список \nВведите /check - чтобы посмотреть список отслеживаемых аниме")

@dp.message_handler(commands=['delete'])
async def delete(message: types.Message):
	argument = message.get_args()
	if not argument:
		return await message.answer("Введите /delete 'название аниме'\nТочное навзание можно посмтротеть через /check")
	else: 
		delete_anime(message.from_user.id, argument)
		return await message.answer("Вы удалили "+argument)

@dp.message_handler(commands=['add'])
async def add_ani(message: types.Message):
	arguments = message.get_args()
	print('Adding anime for user ' + str(message.from_user.id))
	if not arguments:
		return await message.answer("Введите /add 'ссылка на аниме'")
	if arguments:
		name, voices = parce_name(arguments)
		if voices == 0:
			return await message.answer("Попробуте еще раз")
		await message.answer("Доступная озвучка")
		for voice in voices:
			text_voice = voice.text.strip()
			if 'Озвучили' in text_voice:
				text_voice = text_voice[:text_voice.find('Озвучили')]
				await message.answer(text_voice)
			else: 
				await message.answer(text_voice)
		add_anime(message.from_user.id, name)
		await message.answer("Вы добавили аниме!\nОбязательно добавте озвучку через /addvoice иначе боту будет плохо\nНазвание нужно копировать из предыдущих сообщений")
		await message.answer("Если хотите добавить субтитры введите:")
		return await message.answer("/addvoice Субтитры")
		
@dp.message_handler(commands=['addvoice'])
async def addvoice(message: types.Message):
	print('Adding voice for user ' + str(message.from_user.id))
	argument = message.get_args()
	if not argument:
		return await message.answer("Скопирутей название озвучки и напишите /addvoice 'название озвучки'")
	else:
		add_voice(message.from_user.id, argument)
		return await message.answer("Вы добавили озвучку!")

@dp.message_handler(commands=['check'])
async def check(message: types.Message):
	await message.answer("Вы следите за аниме:")
	for an in anime_list(message.from_user.id):
		
		await message.answer(an)


if __name__ == '__main__':
	executor.start_polling(dp)
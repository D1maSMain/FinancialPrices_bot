import asyncio
import sqlite3
import time

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup

import keyb as kb
from config import BOT_TOKEN
from TechnicalSide import Stocks_Parsing as SP
from TechnicalSide import Currencies_Parsing as CP

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

Currenc_Ticker = {'Dollar': "Dollar%20USA",'Euro': "Euro", 'Yuan': "Chinese%20Yuan", 'Swiss Frank': "Swiss%20Frank", 
                  'British Pound': "British%20Pound", 'Yen': "Japanese%20Yen"}

Is_Stock = False

conn = sqlite3.connect('People.db')
cur = conn.cursor()

@dp.message_handler(commands=['start'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте, пожалуйста зарегестрируйтесь или войдите. (Внимание вы запишитесь как {0.username} и если у вас нет аккаунта зарегистрируйтесь! Если вы зарегистрировались но у вас еть аккаун просто нажмите выход! Если вы просто так нажмёте "Регистрация" и у вас есть аккаунт из-за этого у вас откроется новое окно и оно не будет сохронять ввод. Если у вас нет аккаунта и вы нажмёте "Вход" вы не сохранитесь и мы не сможем вернуть данные!)'.format(message.from_user), reply_markup=kb.Mnum_1)


@dp.message_handler(commands=['registration'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Registring'.format(message.from_user))
    global cur

    if (cur.execute('SELECT *FROM Users WHERE userid = "{0.userid}";'.format(message.from_user.id))):
        await bot.send_message(message.from_user.id, 'У вас уже есть аккаунт!'.format(message.from_user, reply_markup=kb.Mnum_2))
    else:
        await bot.send_message(message.from_user.id, 'Введите "/Registration"'.format(message.from_user), reply_markup=kb.Mnum_2)

@dp.message_handler(commands=['Login'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вход!'.format(message.from_user))
    global cur

    if (cur.execute('SELECT *FROM Users WHERE userid = "{0.userid}";'.format(message.from_user.id))):
        if message.from_user != None:
            await bot.send_message(message.from_user.id, 'How are you, {0.username}'.format(message.from_user), reply_markup=kb.Mnum_2)
        else:
            await bot.send_message(message.from_user.id, 'How are you', reply_markup=kb.Mnum_2)
    else:
        await bot.send_message(message.from_user.id, 'Зарегистрируйтесь!'.format(message.from_user))

@dp.message_handler(commands=['Signin'])
async def process_hello(message: types.Message):
    if message.from_user != None:
        await bot.send_message(message.from_user.id, 'How are you, {0.username}'.format(message.from_user), reply_markup=kb.Mnum_2)
    else:
         await bot.send_message(message.from_user.id, 'How are you', reply_markup=kb.Mnum_2)

@dp.message_handler(commands=['Registration'])
async def process_hello(message: types.Message):
    global cur 
    cur.execute("INSERT INTO Users (username, userid) VALUES({0.username}, {1.userid})".format(message.from_user, message.from_user.id))
    await bot.send_message(message.from_user.id, 'Hello {0.username}!'.format(message.from_user), reply_markup=kb.Mnum_2)

@dp.message_handler(commands=['курсы_валют_📈'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'There is currencies list!'.format(message.from_user), reply_markup=kb.Mnum_3)

@dp.message_handler(commands=['Exit_🚪'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'You logged out account!'.format(message.from_user), reply_markup=kb.Mnum_1)

@dp.message_handler(commands=['доллар_руб_💵'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Coming soon...', reply_markup=kb.Mnum_2)

@dp.message_handler(commands=['📰_News'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Here\'s news bulletin', reply_markup=kb.MNews)

@dp.message_handler(commands=['📈_Crypto'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Crypto prices! (Attantion, prices are in 💵!)', reply_markup=kb.MKnum)

@dp.message_handler(commands=['Crypto'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'News about Crypto!', reply_markup=kb.MnBitcoin_2)

@dp.message_handler(commands=['Back'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Backward!', reply_markup=kb.Mnum_2)

@dp.message_handler(commands=['⚙_Settings'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Settings', reply_markup=kb.Mse)

@dp.message_handler(commands=['Bitcoin'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Bitcoin!', reply_markup=kb.MBitcoin)

@dp.message_handler(commands=['Bitcoin_News'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'News about Bitcoin! https://ru.investing.com/crypto/bitcoin/news', reply_markup=kb.MnBitcoin_3)

@dp.message_handler(commands=['Ethereum'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ethereum!', reply_markup=kb.MEthereum)

@dp.message_handler(commands=['Ethereum_News'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'News about Ethereum! https://ru.investing.com/crypto/ethereum/news', reply_markup=kb.MNEthereum)

@dp.message_handler(commands=['Binance_Coin_News'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'News about Binance Coin! https://ru.investing.com/crypto/binance-coin/news', reply_markup=kb.MNBinance_Coin)

@dp.message_handler(commands=['Stock'])
async def process_hello(message: types.Message):
    global cur
    if message.get_args().split()[0] == "Follow":
        await bot.send_message(message.from_user.id, SP.parse("https://www.google.com/search?q="+ message.get_args().split()[1] +"+price", True))
    elif message.get_args().split()[0] == "Unfollow":
        await bot.send_message(message.from_user.id, "Unfollow")
    else:
        await bot.send_message(message.from_user.id, SP.parse("https://www.google.com/search?q="+ message.get_args().split()[0] +"+price", False))

@dp.message_handler(commands=['Exchange_rates📈'])
async def process_hello(message: types.Message):

    await bot.send_message(message.from_user.id, 'Валюты!', reply_markup=kb.NM)

@dp.message_handler(commands=['Ruble_Dollar'])
async def process_hello(message: types.Message):
    global Currenc_Ticker
    await bot.send_message(message.from_user.id, CP.parse("https://www.google.com/search?q="+ Currenc_Ticker['Dollar'] +"+price"), reply_markup=kb.NM)

@dp.message_handler(commands=['Ruble_Yuan'])
async def process_hello(message: types.Message):
    global Currenc_Ticker
    await bot.send_message(message.from_user.id, CP.parse("https://www.google.com/search?q="+ Currenc_Ticker['Yuan'] +"+price"), reply_markup=kb.NM)

@dp.message_handler(commands=['Ruble_Euro'])
async def process_hello(message: types.Message):
    global Currenc_Ticker
    await bot.send_message(message.from_user.id, CP.parse("https://www.google.com/search?q="+ Currenc_Ticker['Euro'] +"+price"), reply_markup=kb.NM)

@dp.message_handler(commands=['Ruble_Swiss_Frank'])
async def process_hello(message: types.Message):
    global Currenc_Ticker
    await bot.send_message(message.from_user.id, CP.parse("https://www.google.com/search?q="+ Currenc_Ticker['Swiss Frank'] +"+price"), reply_markup=kb.NM)

@dp.message_handler(commands=['Ruble_Pound'])
async def process_hello(message: types.Message):
    global Currenc_Ticker
    await bot.send_message(message.from_user.id, CP.parse("https://www.google.com/search?q="+ Currenc_Ticker['British Pound'] +"+price"), reply_markup=kb.NM)

@dp.message_handler(commands=['Ruble_Yen'])
async def process_hello(message: types.Message):
    global Currenc_Ticker
    await bot.send_message(message.from_user.id, CP.parse("https://www.google.com/search?q="+ Currenc_Ticker['Yen'] +"+price"), reply_markup=kb.NM)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)

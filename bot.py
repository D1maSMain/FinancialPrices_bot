import asyncio
import sqlite3
import time

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import keyb as kb
from config import BOT_TOKEN
from TechnicalSide import Stocks_Parsing as SP
from TechnicalSide import Currencies_Parsing as CP
from TechnicalSide import Data_Analyze as DA




loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

Currenc_Ticker = {'Dollar': "Dollar+USA",'Euro': "Euro", 'Yuan': "Chinese+Yuan", 'Swiss Frank': "Swiss+Frank", 
                  'British Pound': "British+Pound", 'Yen': "Japanese+Yen"}

Is_Stock = False 
alerts_kb = InlineKeyboardMarkup(row_width = 5)

State = State()

conn = sqlite3.connect('TechnicalSide\\People.db')
cur = conn.cursor()


@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    await bot.send_message(message.from_user.id, "Hello, if you have an account, please tap Login, if you don't, tap Registration that would be automatically.".format(message.from_user), reply_markup=kb.Mnum_1)

@dp.message_handler(commands=['Login'])
async def Login(message: types.Message):
    global cur
    await bot.send_message(message.from_user.id, 'Logining'.format(message.from_user))
    cur.execute('SELECT *FROM Users WHERE userid = ?;', (message.from_user.id,))
    try:
        if(cur.fetchall()[0] != None):
            if message.from_user != None:
                await bot.send_message(message.from_user.id, 'How are you, {0.username}'.format(message.from_user), reply_markup=kb.Mnum_2)
                await bot.send_message(message.from_user.id, "If you want to follow to the stock price you need to write /Stock Follow Stock_Name. But if you want to Unfollow, then write /Stock Unfollow Stock_Name", reply_markup=kb.Mnum_2)
            
            else:
                await bot.send_message(message.from_user.id, 'How are you', reply_markup=kb.Mnum_2)
                await bot.send_message(message.from_user.id, "If you want to follow to the stock price you need to write /Stock Follow Stock_Name. But if you want to Unfollow, then write /Stock Unfollow Stock_Name", reply_markup=kb.Mnum_2)
    
    except:
        await bot.send_message(message.from_user.id, 'Register Please!'.format(message.from_user))

@dp.message_handler(commands=['Registration'])
async def Registration(message: types.Message):
    global cur 

    cur.execute('SELECT * FROM Users WHERE userid = ?;', (message.from_user.id,))
    try:
        if(cur.fetchall()[0] != None):
            await bot.send_message(message.from_user.id, 'You already exist account!', reply_markup=kb.Mnum_1)
    except: 
        cur.execute("INSERT INTO Users(username, userid) VALUES(?, ?);", (message.from_user.username, message.from_user.id))
        conn.commit()
        await bot.send_message(message.from_user.id, 'Hello {0.username}!'.format(message.from_user), reply_markup=kb.Mnum_2)
        await bot.send_message(message.from_user.id, "If you want to follow to the stock price you need to write /Stock Follow Stock_Name. But if you want to Unfollow, then write /Stock Unfollow Stock_Name", reply_markup=kb.Mnum_2)

@dp.message_handler(commands=['Exit_🚪'])
async def Logout(message: types.Message):
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
        await bot.send_message(message.from_user.id, SP.parse("https://www.google.com/search?q="+ message.get_args().split()[1] +"+price", True, message.from_user.id))
    elif message.get_args().split()[0] == "Unfollow":
        await bot.send_message(message.from_user.id, SP.parse("https://www.google.com/search?q="+ message.get_args().split()[1] +"+price", False, message.from_user.id))
    elif message.get_args().split()[0] == "Alert":
        pass

    else:
        await bot.send_message(message.from_user.id, SP.parse("https://www.google.com/search?q="+ message.get_args().split()[0] +"+price", None, message.from_user.id))

@dp.message_handler(commands=['Alerts'])
async def alerts(message: types.Message):
    global alerts_kb
    alerts_kb = InlineKeyboardMarkup(row_width = 5)
    Empty_AlertL = False
    Buttons = []
    NewAlert = InlineKeyboardButton(text = "New Alert", callback_data = "New")
 
    try:
        F = open(os.path.abspath(os.curdir) + "\\TechnicalSide\\Alerts\\" + message.from_user.id + ".txt", "r")
        for line in F: 
            Data = line
            Name = re.search("[(A-Z)(a-z)(\s+)]", Data).group(0)
            Buttons.append(InlineKeyboardButton(text = Name, callback_data = "Name_" + Name))

            while True:
                Value = re.search("[(\d+)(\.+)]", Data).group(0)
                if Value != None:
                    Buttons.append(InlineKeyboardButton(text = Value, callback_data = "Value_" + Value + "_" + Name))
                    Data = re.sub(Value + ";", "", Data)
                else: 
                    break

        alerts_kb.add(Buttons).insert(NewAlert) 
        await bot.send_message(message.from_user.id, "Your alerts:", reply_markup = alerts_kb)
        F.close()
    except:
        alerts_kb.insert(NewAlert)   
        await bot.send_message(message.from_user.id,"You have got no alerts.", reply_markup = alerts_kb) 
    
@dp.message_handler(commands="New")
async def NewAlert(message: types.Message):
    await bot.send_message(message.from_user.id, "Please write investment instrument name")

@dp.callback_query_handler(Text(startswith = "Name_"))
async def Name_action(callback : types.CallbackQuery):
    pass

@dp.callback_query_handler(Text(startswith = "Value_"))
async def Value_action(callback : types.CallbackQuery):
    pass



@dp.message_handler(commands=['Graph'])
async def process_hello(message: types.Message):
    path = DA.GetData(message.get_args().split()[0], message.from_user.id, message.get_args().split()[1])
    if path == "WrongDate":
        await bot.send_message(message.from_user.id, "Nonexistent date in your followings")
    else:
        photo = open(path, "rb")
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

@dp.message_handler(commands=['Exchange_rates📈'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'There is currencies list', reply_markup=kb.NM)

@dp.message_handler(commands=['Ruble_Dollar'])
async def process_hello(message: types.Message):
    global Currenc_Ticker
    await bot.send_message(message.from_user.id, CP.parse("https://www.google.com/search?q="+ Currenc_Ticker['Dollar'] +"+price", None, message.from_user.id, "USADollar"), reply_markup=kb.NM)

@dp.message_handler(commands=['Ruble_Yuan'])
async def process_hello(message: types.Message):
    global Currenc_Ticker
    await bot.send_message(message.from_user.id, CP.parse("https://www.google.com/search?q="+ Currenc_Ticker['Yuan'] +"+price", None, message.from_user.id, "Yuan"), reply_markup=kb.NM)

@dp.message_handler(commands=['Ruble_Euro'])
async def process_hello(message: types.Message):
    global Currenc_Ticker
    await bot.send_message(message.from_user.id, CP.parse("https://www.google.com/search?q="+ Currenc_Ticker['Euro'] +"+price", None, message.from_user.id, "Euro"), reply_markup=kb.NM)

@dp.message_handler(commands=['Ruble_Swiss_Frank'])
async def process_hello(message: types.Message):
    global Currenc_Ticker
    await bot.send_message(message.from_user.id, CP.parse("https://www.google.com/search?q="+ Currenc_Ticker['Swiss Frank'] +"+price", None, message.from_user.id, "Swiss Frank"), reply_markup=kb.NM)

@dp.message_handler(commands=['Ruble_Pound'])
async def process_hello(message: types.Message):
    global Currenc_Ticker
    await bot.send_message(message.from_user.id, CP.parse("https://www.google.com/search?q="+ Currenc_Ticker['British Pound'] +"+price", None, message.from_user.id, "British Pound"), reply_markup=kb.NM)

@dp.message_handler(commands=['Ruble_Yen'])
async def process_hello(message: types.Message):
    global Currenc_Ticker
    await bot.send_message(message.from_user.id, CP.parse("https://www.google.com/search?q="+ Currenc_Ticker['Yen'] +"+price", None, message.from_user.id, "Yen"), reply_markup=kb.NM)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Back = KeyboardButton("/Back")

btnnum_1 = KeyboardButton("/Registration")
btnnum_7 = KeyboardButton("/Login")
Mnum_1 = ReplyKeyboardMarkup().add(btnnum_1).add(btnnum_7)

btnnum2 = KeyboardButton("/Exchange_rates📈")
btnnum3 = KeyboardButton("/📰_News")
btnnum4 = KeyboardButton("/⚙_Settings")
btnnum21 = KeyboardButton("/Stock")
Mnum_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum2).add(btnnum3).add(btnnum21).add(btnnum4)

btnnum6 = KeyboardButton("/📈_Crypto")
btnnum14 = KeyboardButton("/💵_Currencies")
Mnum_3 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum6).add(btnnum14).add(Back)

btnnum8 = KeyboardButton("/Currencies")
btnnum9 = KeyboardButton("/Petrol and gas")
btnnum10 = KeyboardButton("/Crypto_Currencies")
MNews = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum8).add(btnnum9).add(btnnum10).add(Back)

btnnum11 = KeyboardButton("/Ethereum")
btnnum12 = KeyboardButton("/Bitcoin")
btnnum13 = KeyboardButton("/Binance_Coin")
MKnum = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum11).add(btnnum12).add(btnnum13).add().add(Back)

btnnum23 = KeyboardButton("/Get_Bitcoin_price")
btnnum18 = KeyboardButton("/Get_Bitcoin_graph")
MBitcoin = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum18).add(btnnum23).add(Back)

btnnum5 = KeyboardButton("/Exit_🚪")
btnnum20 = KeyboardButton("/Synchronize_Currency_Using_Geolocation", request_location=True)
Mse = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum5).add(btnnum20).add(Back)

MNBitcoin = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum23).add(Back)

btnnum22 = KeyboardButton("/Bitcoin_News")
btnnum26 = KeyboardButton("/Ethereum_News")
btnnum27 = KeyboardButton("/Binance_Coin_News")
MnBitcoin_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum22).add(btnnum26).add(btnnum27).add(Back)


MnBitcoin_3 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum23).add(Back)

btnnum24 = KeyboardButton("/Узнать_цену_Ethereum")
btnnum25 = KeyboardButton("/Вывести_график_Ethereum")
MEthereum = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum24).add(btnnum25).add(Back)

MNEthereum = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum24).add(Back)

btnnum28 = KeyboardButton("/Узнать_цену_Binance_Coin")
MNBinance_Coin = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum28).add(Back)


Ak = ReplyKeyboardMarkup(resize_keyboard=True).add(Back)

btnnum29 = KeyboardButton("/Ruble_Dollar")
btnnum30 = KeyboardButton("/Ruble_Euro")
btnnum31 = KeyboardButton("/Ruble_Pound")
btnnum32 = KeyboardButton("/Ruble_Yuan")
btnnum33 = KeyboardButton("/Ruble_Swiss_Frank")
btnnum34 = KeyboardButton("/Ruble_Yen")
NM = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum29).add(btnnum30).add(btnnum31).add(btnnum32).add(btnnum33).add(btnnum34).add(Back)

btnnum35 = KeyboardButton("/Узнать цену ещё раз")
NM_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum35).add(Back)

back = ReplyKeyboardMarkup(resize_keyboard=True).add(Back)

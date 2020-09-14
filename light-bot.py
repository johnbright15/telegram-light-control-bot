!pip install adafruit-io
import os
x = os.getenv("ADAFRUIT_IO_USERNAME")
y = os.getenv("ADAFRUIT_IO_KEY")
from Adafruit_IO import Client,Feed
aio = Client(x,y)
#Create new feed
new = Feed(name='bot') #feed name created
result = aio.create_feed(new)
result
from Adafruit_IO import Data

!pip install python-telegram-bot
from Adafruit_IO import Client,Data
from telegram.ext import Updater,CommandHandler

def on(bot,update):
  chat_id = update.message.chat_id    
  aio.create_data('bot',Data(value = 1))
  bot.send_message(chat_id =chat_id,text ="Lights On")

def off(bot,update):
  chat_id = update.message.chat_id
  aio.create_data('bot',Data(value = 0))
  bot.send_message(chat_id =chat_id,text ="Lights Off")

u = Updater('TELEGRAM KEY')     #Use Telegram Token HTTP API
dp =u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()

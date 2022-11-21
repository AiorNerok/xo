import redis
import json
import telebot
from dotenv import load_dotenv, dotenv_values

from extensions import *

load_dotenv()
config = dict(dotenv_values(".env"))


redis_connect = redis.Redis(
    host=config["REDIS_HOST"],
    port=config["REDIS_PORT"],
    password=config["REDIS_PASSWORD"],
)


# red.set("currency", str(currency))
currency = redis_connect.get("currency").decode("utf8").replace("'", '"')
currency = json.loads(currency)

currency_values = currency.values()


bot = telebot.TeleBot(config["TOKEN"])


@bot.message_handler(commands=["/info"], content_types=["text"])
def info_currency(msg: telebot.types.Message):
    print(msg)
    bot.send_message(msg.chat.id, msg)


bot.polling(non_stop=True)

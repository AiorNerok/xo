import telebot
from telebot import types
from dotenv import load_dotenv, dotenv_values

from extensions import (
    API,
    number_separator,
    BadRequestError,
    SameArgumentsError,
    NotNumberError,
)

load_dotenv()
config = dict(dotenv_values(".env"))

currency = {"Российский рубль": "RUR", "Доллар США": "USD", "Евро": "EUR"}

bot = telebot.TeleBot(config["TOKEN"])


@bot.message_handler(commands=["values"])
def values(msg: types.Message):
    bot.send_message(
        chat_id=msg.chat.id,
        text=f"""<pre>
Доступные валюты:
________________________
|Наименование    | код |
|----------------|-----|
|Российский рубль| RUR |
|Доллар США      | USD |
|Евро            | EUR |
|________________|_____|
</pre>""",
        parse_mode="HTML",
    )


@bot.message_handler(commands=["help"])
def help(msg: types.Message):
    bot.send_message(msg.chat.id, '''Пример запроса "RUR USD 250"''')


@bot.message_handler(content_types=["text"])
def convert_currency(msg: types.Message):

    try:
        base, quote, amount = msg.text.split()

        if all([x in list(currency.values()) for x in [base, quote]]):

            result = API.get_price(base, quote, amount)

            bot.send_message(
                msg.chat.id,
                f'{base} - {number_separator(amount)[:-2]}\n{quote} - {number_separator(round(result["data"]["sum_result"], 2))}',
            )
        else:
            raise Exception

    except BadRequestError:
        bot.send_message(
            msg.chat.id,
            'Number of arguments should be 3\nExample "RUR USD 100"',
        )
    except SameArgumentsError:
        bot.send_message(
            msg.chat.id,
            'The first argument and the second argument are equal\nBut must be different\nExample "RUR USD 100"',
        )
    except NotNumberError:
        bot.send_message(
            msg.chat.id,
            'The last argument must be an integer greater than 0\nExample "RUR USD 100"',
        )
    except:
        bot.send_message(msg.chat.id, 'invalid arguments\nExample "RUR USD 100"')


bot.polling(non_stop=True)

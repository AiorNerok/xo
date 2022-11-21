import requests
import json
import lxml
import lxml.html


class CurrencyConvertApi:
    _main_url = "https://cash.rbc.ru/cash/json/converter_currency_rate"

    def convert(self, currency_from, currency_to, amount):
        req = requests.get(
            f"{self._main_url}/?currency_from={currency_from}&currency_to={currency_to}&source=cbrf&sum={amount}&date="
        )
        value = json.loads(req.content)
        return value

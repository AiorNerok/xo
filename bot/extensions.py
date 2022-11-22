import requests
import json


def validate_arguments(func):
    def wrapper(*args, **kwargs):
        
        if len(set(args)) != 3:

            if args[0] == args[1]:
                raise SameArgumentsError

            raise BadRequestError

        if not args[2].isdigit():
            raise NotNumberError

        return func(*args, **kwargs)

    return wrapper


class API:
    @validate_arguments
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        _main_url = "https://cash.rbc.ru/cash/json/converter_currency_rate"
        req = requests.get(
            f"{_main_url}/?currency_from={base}&currency_to={quote}&source=cbrf&sum={amount}&date="
        )

        result = json.loads(req.content)
        return result


class BadRequestError(Exception):
    pass

class SameArgumentsError(Exception):
    pass

class NotNumberError(Exception):
    pass


def number_separator(num):
    return "{0:,}".format(round(float(num), 2)).replace(",", " ")


if __name__ == "__main__":
    pass

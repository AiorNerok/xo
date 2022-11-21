import requests
import json


def validate_arguments(func):
    def wrapper(*args, **kwargs):
        if len(set(args)) != 3:
            raise BadRequestError(
                """
                    Number of arguments should be 3
                    Example "RUR USD 100"
                                    """
            )

        if args[0] == args[1]:
            raise BadRequestError(
                """
                    The first argument and the second argument are equal
                    But must be different
                                    """
            )

        if not args[2].isdigit():
            raise BadRequestError(
                """
                    the last argument must be an integer greater than 0
                                    """
            )

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



def number_separator(num):
    return "{0:,}".format(round(float(num), 2)).replace(",", " ")


if __name__ == "__main__":
    pass

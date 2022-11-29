"""Кастомные ошибки"""
from dataclasses import dataclass


@dataclass(frozen=True)
class CustomException(Exception):
    msg: str = ""

    def __str__(self) -> str:
        return self.msg


BoardException = CustomException()
BoardOutException = CustomException("Вы пытаетесь выстрелить за доску!")
BoardUsedException = CustomException("Вы уже стреляли в эту клетку")
BoardWrongShipException = CustomException()

if __name__ == "__main__":
    pass

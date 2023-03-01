from datetime import datetime


def debug(func):
    def wrapper(n, *args, **kwargs):
        start = datetime.now()
        func(n, *args, **kwargs)
        end = datetime.now()
        timer = end - start
        with open("debug.txt", "a", encoding="utf-8") as file:
            file.write(f"{start} - Функция {func.__name__} исполнена,\nАргументы {n, args}, именованные аргументы {kwargs}.\nФункция вернула значение {func(n)} , время выполнения функции {timer} сек.\n")
    return wrapper


@debug
def some_func(n, *args, **kwargs):
    return n * 2


if __name__ == '__main__':
    some_func(3)

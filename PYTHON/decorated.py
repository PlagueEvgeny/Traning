def hello_world():
    print("Hello, World")


type(hello_world)
class Hello:
    pass

type(10)

# hello = hello_world
# hello()


def higher_order(func):
    print('Получена функция {} в качестве аргумента'.format(func))
    func()
    return func

# @higher_order
# def hello_world():
#     print("Hello, World")


def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper


@decorator_function
def hello_world():
    print("Hello, World")


hello_world()
"""
    Создайте собственный класс-исключение, обрабатывающий ситуацию деления
на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
пользователем нуля в качестве делителя программа должна корректно обработать
эту  ситуацию и не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, text):
        self.text = text
        print(text)


flag = True
while flag:
    input_number = input('give me number: ')
    try:
        input_number = int(input_number)
        if input_number == 0:
            raise OwnError('you cant divide by zero')

    except ValueError:
        print("it not a number")

    except OwnError:
        OwnError
    else:
        print(f'everything ok res={100 / input_number}')
        flag = False

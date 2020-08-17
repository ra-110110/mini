from colorama import init
from colorama import Fore

init()
print(Fore.CYAN)
print("Введите \"stop\" для выхода!")
while True:
    question = input("Что делаем? (+,-,*,/): ")
    if question == 'stop':
        break
    if question in ('+', '-', '*', '/'):
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        if question == "+":
            res = a + b
            print(f"Результат: {res}")
        elif question == "-":
            res = a - b
            print(f"Результат: {res}")
        elif question == "*":
            res = a * b
            print(f"Результат: {res}")
        elif question == "/":
            if b != 0:
                res = a / b
                res = round(res, 2)
                print(f"Результат: {res}")
            else:
                print("На ноль делить нельзя, даже если очень хочется! Попробуйте еще раз!")
else:
    print("Вы ввели неверную операцию!")

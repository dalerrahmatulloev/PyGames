import random

while True:
    try:
        numTo = int(input("Выберите до какого числа хотите отгадывать: "))
        num = random.randint(1, numTo)
        break
    except ValueError:
        print("Введите число!!!")
change = 5
print(f"У вас есть {change} попыток угадать число")

while True:
    try:
        if change == 0: break
        inputNum = int(input("Введите загадонное число: "))
        if num == inputNum:
            print(f"Вы победили!!! Правильное число {num}")
            break
        elif num > inputNum:
            print("Неправильно, загадая цифра больше")
        else:
            print("Неправильно, загадая цифра меньше")
        change -= 1
        print(f"У вас осталось {change} попыток")
    except ValueError:
        print("Иди понюхай")
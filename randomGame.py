import random

while True:
    try:
        numTo = int(input("Выберите до какого числа хотите отгадывать: "))
        num = random.randint(0, numTo)
        break
    except ValueError:
        print("Введите число!!!")
change = 5
print(f"У вас есть {change} попыток угадать число")

while True:
    try:
        inputNum = int(input("Введите загадонное число: "))
        if num == inputNum:
            print(f"Вы победили!!! Правильное число {num}")
            break
        elif num > inputNum:
            print("Неправильно, загадая цифра больше")
        else:
            print("Неправильно, загадая цифра меньше")
        change -= 1
        if change == 0: 
            print(f"вы не отгодали число, правильное число {num})")
            break
        print(f"У вас осталось {change} попыток")
    except ValueError:
        print("Иди понюхай")
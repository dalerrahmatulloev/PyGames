import random

choices = {1: "Камень", 2: "Ножницы", 3: "Бумага"}

while True:
    try:
        player = int(input("Выберите: камень(1), ножницы(2), бумага(3): "))
        if player not in [1, 2, 3]:
            print("Выберите 1, 2 или 3!")
            continue

        comp = random.randint(1, 3)

        print(f"Игрок выбрал: {choices[player]}")
        print(f"Компьютер выбрал: {choices[comp]}")

        if player == comp:
            print("Ничья!")
        elif (player == 1 and comp == 2) or (player == 2 and comp == 3) or (player == 3 and comp == 1):
            print("Победил Игрок!")
        else:
            print("Победил Компьютер!")
        
        answer = input("Хотите начать заново? y/n: ").lower()
        if answer == "n": 
            print("До свидания!")
            break
        elif answer == "y":
            continue
        else:
            print("Пожалуйста, введите 'y' или 'n'.")
    except ValueError:
        print("Введите число!!!")
import random

while True:
    try:
        players = int(input("Введите количество игроков: "))
        break
    except ValueError:
        print("Введи правильное количество!!!")

cnt = 1
while True:
    if cnt > players:
        answer = input("Хотите начать заново? yes/no ").lower
        if answer == "no": break
        print("\n")
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    print(f"Игроку {cnt} выпали {num1} и {num2}, всего {num1 + num2}")
    cnt += 1
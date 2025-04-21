questions = [
    {
        "question": "Сколько будет 5 * 3?",
        "options": [8, 15, 10, 20],
        "correct_option": 2
    },
    {
        "question": "Какой цвет получается при смешивании синего и жёлтого?",
        "options": ["Зелёный", "Фиолетовый", "Оранжевый", "Коричневый"],
        "correct_option": 1
    },
    {
        "question": "Сколько планет в Солнечной системе?",
        "options": [7, 8, 9, 10],
        "correct_option": 2
    },
    {
        "question": "Что тяжелее: 1 кг железа или 1 кг ваты?",
        "options": ["Железо", "Вата", "Одинаково", "Зависит от объёма"],
        "correct_option": 3
    },
    {
        "question": "Какой язык программирования используется для веб-разметки?",
        "options": ["Python", "C++", "HTML", "Java"],
        "correct_option": 3
    }
]

for question in questions:
    print(question["question"])
    tips = ""
    for i in range(4):
        tips = f"{tips}{i + 1}) {question["options"][i]}; \n"
    print(tips)
    while True:
        try:
            answer = int(input("Введите номер варианта ответа (1, 2, 3, 4): "))
            if answer not in [1, 2, 3, 4]:
                print("Выберите 1, 2, 3 или 4!")
                continue
            break
        except ValueError:
            print("Введите число!!!")
    if answer == question["correct_option"]:
        print("Ты не даун(Джасур)\n")
    else:
        print("Ты Джасур(даун)\n")
    
import re

def arrMath(math):
    # Убираем пробелы
    math = math.replace(" ", "")
    
    # Разбиваем строку на числа и операторы
    math_elements = re.findall(r'\d+|[-+*/^()]', math)
    return math_elements

def answerMath(math):
    # Простой алгоритм для вычисления выражений с двумя операндами
    if len(math) != 3:
        return "Некорректное выражение"
    
    num1 = int(math[0])
    operator = math[1]
    num2 = int(math[2])
    
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Ошибка: деление на ноль"
        return num1 / num2
    else:
        return "Неизвестный оператор"

while True:
    # Основной код
    math = input("Напишите задачу или exit: ")
    if math == "exit":
        break
    math = arrMath(math)

    print(f"Разобранное выражение: {math}")
    result = answerMath(math)
    print(f"Ответ: {result}")
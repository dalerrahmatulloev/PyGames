# Запись в файл
with open("text.txt", "w") as file:
    file.write(input("Что хотите ввести в файл? "))
    
# Чтение из файла
with open("text.txt", "r") as file:
    content = file.read()
    print(content)


print("Файл успешно записан.")
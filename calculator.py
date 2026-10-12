a = float(input("Введ первое число: "))
operation = input("Выбери операцию (+, -, *, /): ")
b = float(input("Введи второе число: "))

if operation == "+":
    print("Результат:", a + b)
elif operation == "-":
    print("Результат:", a - b)
elif operation == "*":
    print("Результат:", a * b)
elif operation == "/":
    if b != 0:
        print("Результат:", a / b)
    else:
        print("Ошибка! Деление на ноль невозможно.")
else:
    print("Неизвестная операция!")
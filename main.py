"""
from calculations import add,minus,multiply,div,power
a = int(input("enter first number: "))
b = int(input("enter second number: "))
choice = None
while choice !=0:
    choice = int(input("enter your choice \n (0-stop program, 1-add numbers, 2-minus, 3-div numbers, 4-multiply, 5-power):"))
    if choice == 1:
        c = add(a,b)
        print(c)
        continue
    if choice == 2:
        c = minus(a,b)
        print(c)
        continue
    if choice == 3:
        c = div(a,b)
        print(c)
        continue
    if choice == 4:
        c = multiply(a,b)
        print(c)
        continue
    if choice == 5:
        c = power(a,b)
        print(c)
        continue


import os
os.mkdir("створенна папка")
os.rename("створенна папка", "folder")

with open("file.txt", "r") as file:
    text = file.read()
    print(text)
with open("file.txt", "at") as my_file:
    my_file.write("this is our first text")
    

name = input("write ur name: ")
hobby = input("write ue hobby: ")
dish = input("write ur favorit eat: ")
with open("file.txt", "w") as file:
    file.write(name)
    file.write(hobby)
    file.write(dish)

with open("file.txt", "r") as file:
    text = file.read()
    print(text)
with open("file.txt", "r") as file:
    text = file.readline()
    print(text)
with open("file.txt", "r") as file:
    text = file.readlines()
    print(text) 
    
a = int(input("Enter your choice(1 - показати усі справи, 2 - додати нову справу, 3 - очистити справи, 4 - вийти): "))
if a == 1:
    with open("file.txt", "r") as file:
        text = filr.read()
        print(text)
elif a == 2:
    b = input("Напиши справу: ")
    with open("file.txt", "a+") as file:
        file.write
elif a == 3:
    with open("file.txt", "w") as file:
        file.close()
        os.remove("file.txt")
elif a == 4:
    print("ви вийшли з програми")
    

try:
    num = int(input("enter number: "))
    print(f"Ти ввів {num} ")
except ValueError:
    print("ви ввели не число, а щось інше. ")
    

try:
    a = int (input ("Enter number: "))
    b = int(input ("Enter number: "))
except ValueError:
    print("Ви ввели не число, Я щось інше.")
else:
    print(a+b)
finally:
    print("Цей код виконався незалежно від помилки.")

try:
    a = int(input("Enter first number: "))
    b = int(input ("Enter second number: "))
    a/b
except ZeroDivisionError:
    print("Ви хочете виконати ділення на 0. Це неможливо")
else:
    print ("a/b = ", a/b)
finally:
    print("Для цього коду ми використали конструкцію if-except-else-finally")

try:
    cash = float (input("Введіть суму яку хочете конвертувати: "))
except ValueError:
        print("Ви ввели неправильне значення або порожній рядок")
else:
    convert = input(" яку валюту хочете перевести (EUR/USD): ")
if convert == "EUR" :
    print(f"(cash) гривень - це {cash/45:.2f}")
if convert == "USD":
    print(f"{cash} гривень - це {cash/42:.2f}")
finally:
    print ("Дякуємо, що скористалися нашими послугами!")

"""


import os


phonebook = {
    "Мама": "+380501234567",
    "Тато": "+380671234567"
}
notes_file = "notes.txt"



def show_menu():
    print("\nОберіть програму:")
    print("1. Телефонна книга")
    print("2. Калькулятор")
    print("3. Записник")
    print("0. Вихід")


def phone_app():
    print("\nТелефонна книга:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

    name = input("Введіть ім'я для пошуку (або натисніть Enter для виходу): ").strip()
    if name:
        if name in phonebook:
            print(f"Номер {name}: {phonebook[name]}")
        else:
            print("Ім’я не знайдено у телефонній книзі.")


def calculator():
    print("\nКалькулятор (доступні операції: +, -, *, /)")
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть операцію: ")
        num2 = float(input("Введіть друге число: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Помилка: ділення на нуль.")
                return
            result = num1 / num2
        else:
            print("Невідома операція.")
            return

        print(f"Результат: {result}")
    except ValueError:
        print("Помилка: введіть числові значення.")
    
def notebook():
    while True:
        print("\n Записник:")
        print("1. Переглянути нотатки")
        print("2. Додати нотатку")
        print("0. Назад")
        choice = input("Ваш вибір: ")

        if choice == "1":
            read_notes()
        elif choice == "2":
            add_note()
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Спробуйте ще.")


def read_notes():
    print("\n Ваші нотатки:")
    if not os.path.exists(notes_file):
        print("Нотаток ще немає.")
        return

    try:
        with open(notes_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if lines:
                for idx, line in enumerate(lines, 1):
                    print(f"{idx}. {line.strip()}")
            else:
                print("Нотаток ще немає.")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")


def add_note():
    note = input("Введіть текст нотатки: ").strip()
    if not note:
        print("Нотатка не може бути порожньою.")
        return
    try:
        with open(notes_file, "a", encoding="utf-8") as f:
            f.write(note + "\n")
        print("Нотатку збережено.")
    except Exception as e:
        print(f"Помилка при записі у файл: {e}")
def main():
    while True:
        show_menu()
        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            phone_app()
        elif choice == "2":
            calculator()
        elif choice == "3":
            notebook()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
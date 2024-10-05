def validate_number(input_value, lang):
    try:
        return float(input_value)
    except ValueError:
        if lang == 'en':
            print("Error! You entered an invalid number.")
        elif lang == 'ua':
            print("Помилка! Ви ввели не число.")
        elif lang == 'pl':
            print("Błąd! Wprowadzono nieprawidłową liczbę.")

        return None


def calculator(lang):
    if lang == 'en':
        print("Welcome to the terminal calculator.")
        print("Choose an operation:")
        print("1. Addition +")
        print("2. Subtraction -")
        print("3. Multiplication *")
        print("4. Division /")
    elif lang == 'ua':
        print("Ласкаво просимо до термінального калькулятора!")
        print("Виберіть операцію:")
        print("1. Додавання +")
        print("2. Віднімання -")
        print("3. Множення *")
        print("4. Ділення /")
    elif lang == 'pl':
        print("Witamy w terminalowym kalkulatorze!")
        print("Wybierz operację:")
        print("1. Dodawanie +")
        print("2. Odejmowanie -")
        print("3. Mnożenie *")
        print("4. Dzielenie /")

    if lang == 'en':
        operation = input("Enter choice (1 / 2 / 3 / 4): ")
    elif lang == 'ua':
        operation = input("Виберіть операцію (1 / 2 / 3 / 4): ")
    elif lang == 'pl':
        operation = input("Wybierz operację (1 / 2 / 3 / 4): ")

    if operation not in ['1', '2', '3', '4']:
        if lang == 'en':
            print("Error! Invalid operation choice.")
        elif lang == 'ua':
            print("Помилка! Неправильний вибір операції.")
        elif lang == 'pl':
            print("Błąd! Nieprawidłowy wybór operacji.")
   
        return



    num1 = None
    num2 = None

    while num1 is None:
        num1 = validate_number(
            input("Enter the first number:  ") if lang == 'en' else
            input("Введіть перше число: ") if lang == 'ua' else
            input("Wprowadź pierwszą liczbę: "), lang
        )
    
    while num2 is None:
        num2 = validate_number(
            input("Enter the second number:  ") if lang == 'en' else
            input("Введіть друге число:  ") if lang == 'ua' else
            input("Wprowadź drugą liczbę: "), lang
        )

    if operation == '1':
        result = num1 + num2
        if lang == 'en':
            print(f"Result: {result}")
        elif lang == 'ua':
            print(f"Результат: {result}")
        elif lang == 'pl':
            print(f"Wynik: {result}")

    elif operation == '2':
        result = num1 - num2
        if lang == 'en':
            print(f"Result: {result}")
        elif lang == 'ua':
            print(f"Результат: {result}")
        elif lang == 'pl':
            print(f"Wynik: {result}")

    elif operation == '3':
        result = num1 * num2
        if lang == 'en':
            print(f"Result: {result}")
        elif lang == 'ua':
            print(f"Результат: {result}")
        elif lang == 'pl':
            print(f"Wynik: {result}")

    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            if lang == 'en':
                print(f"Result: {result}")
            elif lang == 'ua':
                print(f"Результат: {result}")
            elif lang == 'pl':
                print(f"Wynik: {result}")
        else:
            if lang == 'en':
                print("Error! Division by zero")
            elif lang == 'ua':
                print("Помилка! Ділення на нуль.")
            elif lang == 'pl':
                print("Błąd! Dzielenie przez zero.")


def main():
    lang = input("Choose language en / ua / pl:  ").lower()
    if lang not in ['en', 'ua', 'pl']:
        print("Invalid language choice")
        return
    calculator(lang)

if __name__ == "__main__":
    main()
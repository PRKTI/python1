def check_leap_year():
    while True:
        try:
            user_input = input("Введите год (целое положительное число): ")
            year = int(user_input)
            
            if year <= 0:
                print("Ошибка: Год должен быть положительным числом.\n")
                continue  
            break  

        except ValueError:
            print("Ошибка: Введено некорректное значение. Пожалуйста, введите целое число.\n")
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"Год {year} является високосным.")
    else:
        print(f"Год {year} не является високосным.")
if __name__ == "__main__":
    check_leap_year()
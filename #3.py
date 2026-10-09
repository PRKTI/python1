def check_even_number():
    print("=== Проверка числа на четность ===")
    user_input = input("Введите целое число: ")
    try:
        number = int(user_input)
    except ValueError:
        print("Ошибка:", user_input, "не является целым числом.")
        
    else:
        print("Вы ввели число:",number)
        if number % 2 == 0:
            print("Число" ,number, " является четным.")
        else:
            print("Число",number," является нечетным.")     
    finally:
        print("Программа завершена.")

if __name__ == "__main__":
    check_even_number()

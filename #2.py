
def read_file(file_name):
    file = None
    try:
        file = open(file_name, 'r')
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("Ошибка: Файл", file_name, "не найден.")
    except IOError:
        print("Произошла непредвиденная ошибка:")
    finally:
        if file is not None:
            file.close()
            print("Файл",file_name," успешно закрыт.")

if __name__ == "__main__":
    read_file("Diagram_1.txt")

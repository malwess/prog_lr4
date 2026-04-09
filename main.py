def read_set_from_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read().strip().split()
        return set(data)

def set_calculator(file1, file2):
    A = read_set_from_file(file1)
    B = read_set_from_file(file2)

    while True:
        print("\nМножество A:", A)
        print("Множество B:", B)

        print("\nВыберите операцию:")
        print("1 - Объединение (A ∪ B)")
        print("2 - Пересечение (A ∩ B)")
        print("3 - Разность (A - B)")
        print("4 - Разность (B - A)")
        print("5 - Симметрическая разность (A Δ B)")
        print("0 - Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            print("Результат:", A | B)
        elif choice == '2':
            print("Результат:", A & B)
        elif choice == '3':
            print("Результат:", A - B)
        elif choice == '4':
            print("Результат:", B - A)
        elif choice == '5':
            print("Результат:", A ^ B)
        elif choice == '0' or choice.lower() == 'exit':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

# пример вызова функции
set_calculator('set1.txt', 'set2.txt')
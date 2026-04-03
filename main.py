def set_calculator():
    # Вспомогательная функция для чтения множества из файла
    def read_set(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # Предполагается, что элементы разделены пробелами или переводами строки
                data = f.read().split()
                return set(data)
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
            return set()

    while True:
        path1 = input("Введите путь к первому файлу: ")
        if path1.lower() in ['0', 'exit']:
            break
        path2 = input("Введите путь ко второму файлу: ")
        if path2.lower() in ['0', 'exit']:
            break

        A = read_set(path1)
        B = read_set(path2)

        print(f"\nМножество А: {A}")
        print(f"Множество В: {B}")

        print("\nВыберите операцию:")
        print("1 - Объединение (A ∪ B)")
        print("2 - Пересечение (A ∩ B)")
        print("3 - Разность (A \\ B)")
        print("4 - Симметрическая разность (A △ B)")
        print("0 - Выход")

        choice = input("Ваш выбор: ")

        if choice == '0' or choice.lower() == 'exit':
            print("Выход из программы.")
            break

        if choice == '1':
            result = A.union(B)
            operation = "Объединение"
        elif choice == '2':
            result = A.intersection(B)
            operation = "Пересечение"
        elif choice == '3':
            result = A.difference(B)
            operation = "Разность"
        elif choice == '4':
            result = A.symmetric_difference(B)
            operation = "Симметрическая разность"
        else:
            print("Некорректный выбор, попробуйте снова.")
            continue

        print(f"\nРезультат ({operation}): {result}\n")

# Вызов функции
# set_calculator()
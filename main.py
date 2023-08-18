import csv
import os


# Функция для загрузки данных из файла
def load_contacts(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            contacts = [contact for contact in reader]
            return contacts
    except FileNotFoundError:
        return []


# Функция для сохранения данных в файл
def save_contacts(filename, contacts):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['Фамилия', 'Имя', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)


# Функция для вывода записей постранично
def display_contacts(contacts, page_size, page_number):
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    for index, contact in enumerate(contacts[start_index:end_index], start=start_index + 1):
        print(f"{index}. {contact['Фамилия']} {contact['Имя']} {contact['Отчество']}")
        print(f"   Организация: {contact['Организация']}")
        print(f"   Рабочий телефон: {contact['Рабочий телефон']}")
        print(f"   Личный телефон: {contact['Личный телефон']}")
        print()


# Функция для добавления новой записи
def add_contact(contacts):
    contact = {}
    contact['Фамилия'] = input("Фамилия: ")
    contact['Имя'] = input("Имя: ")
    contact['Отчество'] = input("Отчество: ")
    contact['Организация'] = input("Организация: ")
    contact['Рабочий телефон'] = input("Рабочий телефон: ")
    contact['Личный телефон'] = input("Личный телефон: ")
    contacts.append(contact)
    print("Запись добавлена")


# Функция для поиска записей
def search_contacts(contacts):
    search_term = input("Введите ключевое слово для поиска: ")
    results = []
    for contact in contacts:
        if (search_term.lower() in contact['Фамилия'].lower() or
                search_term.lower() in contact['Имя'].lower() or
                search_term.lower() in contact['Отчество'].lower() or
                search_term.lower() in contact['Организация'].lower() or
                search_term in contact['Рабочий телефон'] or
                search_term in contact['Личный телефон']):
            results.append(contact)
    return results


# Основной код
def main():
   def main():
    filename = input("Введите имя файла (по умолчанию contacts.csv): ")
    if not filename:
        filename = 'contacts.csv'
    
    if not os.path.exists(filename):
        with open(filename, 'w', newline=''):
            pass
    
    
    contacts = load_contacts(filename)
    if os.path.exists(filename):
        contacts = load_contacts(filename)

        while True:
            print("Выберите действие:")
            print("1. Вывод записей постранично")
            print("2. Добавление новой записи")
            print("3. Поиск записей")
            print("4. Выход")

            choice = input("Введите номер действия: ")

            if choice == '1':
                page_size = 5
                page_number = int(input("Введите номер страницы: "))
                display_contacts(contacts, page_size, page_number)
            elif choice == '2':
                add_contact(contacts)
                save_contacts(filename, contacts)
            elif choice == '3':
                results = search_contacts(contacts)
                if results:
                    print("Результаты поиска:")
                    for index, result in enumerate(results, start=1):
                        print(f"{index}. {result['Фамилия']} {result['Имя']} {result['Отчество']}")
                        print(f"   Организация: {result['Организация']}")
                        print(f"   Рабочий телефон: {result['Рабочий телефон']}")
                        print(f"   Личный телефон: {result['Личный телефон']}")
                        print()
                else:
                    print("Ничего не найдено.")
            elif choice == '4':
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите действие из списка.")
    else:
        print("Файла не существует")


if __name__ == '__main__':
    main()

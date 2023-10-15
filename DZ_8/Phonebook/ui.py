from logger import *

def user_interface():
    with open('Phonebook.txt', 'a', encoding='utf-8'):  # создаем файл, если его нет
        pass
    cmd = None
    while cmd != '6':
        print('Меню:\n'
              '1. Запись контакта\n'
              '2. Ввести данные на экран\n'
              '3. Поиск контакта\n'
              '4. Изменение контакта\n'
              '5. Удаление контакта\n'
              '6. Выход')
        cmd = input('Введите номер операции: ')
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')
        match cmd:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                change_contact()
            case '5':
                delete_contact()
            case '6':
                print('До свидания!')
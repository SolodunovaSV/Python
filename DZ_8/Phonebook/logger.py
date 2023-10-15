from data_create import *

def input_contact():
    name = name_data()
    surname = surname_data()
    patronymic = patronymic_data()
    phone_number = phone_number_data()
    address = address_data()
    return f'{name} {surname} {patronymic}\n{phone_number}\n{address}'

def add_contact():
    contact = input_contact()
    with open('Phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(contact + '\n\n')

def read_data():
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        return data.read()
    
def print_contacts():
    data = read_data()
    print()
    print(data)

def search_contact():
    print('Варианты поиска:\n'
              '1. По имени\n'
              '2. По фамилии\n'
              '3. По отчеству\n'
              '4. По номеру телефона\n'
              '5. По адресу')
    choice = input('Выберите вариант поиска: ')
    i_choice = int(choice) - 1
    search = input('Введите данные для поиска: ')
    data_str = read_data().rstrip()
    if search not in data_str:
        print('Совпадений не найдено')
    else:
        # print([data_str])
        data_lst = data_str.split('\n\n')
        # print(data_lst)
        for contact_str in data_lst:
            contact_lst = contact_str.replace('\n', ' ').split()
            if search in contact_lst[i_choice]:
                # print(contact_lst)
                print(contact_str)
                print()


def change_contact():
    print('Введите данные, которые необходимо изменить:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес\n')
    index = int(input('Выберите данные: ')) - 1
    searched = input('Введите данные, которые необходимо изменить: ').title()
    replacement = input('Введите новые данные: ').title()
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        data = data.read().strip().split('\n\n')
    new_data = []
    my_check = False
    for item in data:
        contact_info = item.replace('\n', ' ').split()
        if len(contact_info) >= index + 1:
            if contact_info[index] == searched:
                my_check = True
                contact_info[index] = replacement
                new_data.append(
                    f'{contact_info[0]} {contact_info[1]} {contact_info[2]}\n{contact_info[3]}\n{contact_info[4]}\n')
            else:
                new_data.append(item)
        else:
            new_data.append(item)
    if not my_check:
        print('Совпадений не найдено.')
    with open('Phonebook.txt', 'w', encoding='utf-8') as data:
        data.write('\n'.join(new_data))
    print('Данные сохранены')


def delete_contact():
    print('Выбертите вариант удаления:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес\n'
          '6. Удалить контакт целиком')

    index = int(input('Выберите вариант: ')) - 1
    searched = input('Введите данные для поиска: ').title()
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        data = data.read().strip().split('\n\n')
    new_data = []
    for item in data:
        if index == 5 and searched in item:
            continue  
        contact_info = item.replace('\n', ' ').split()
        if len(contact_info) >= index + 1:  
            field_to_delete = contact_info[index]
            if searched == field_to_delete and index != 5:
                contact_info[index] = 'None'
                new_data.append(f'{contact_info[0]} {contact_info[1]} {contact_info[2]}\n{contact_info[3]}\n{contact_info[4]}\n')
            else:
                new_data.append(item)
        else:
            new_data.append(item)
    with open('Phonebook.txt', 'w', encoding='utf-8') as data:
        data.write('\n'.join(new_data))
    print('Данные удалены')
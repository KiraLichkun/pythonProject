import random, csv
from string import ascii_letters, digits


def create_password():  # Функция для создания паролей
    letter_digit = ascii_letters + digits
    password = ''.join(random.choices(letter_digit, k=8))
    return password


def create_login(name):  # Функция для создания логинов
    name = name.split()
    return f'{name[0]}_{name[1][0]}{name[2][0]}'


with open('students.csv') as file:
    reader = csv.DictReader(file, delimiter=',')  # Создаём объект для чтения файла
    reader = list(reader)
    for person in reader:
        person['login'] = create_login(person['Name'])
        person['password'] = create_password()

with open('students_password.csv', 'w') as file:  # Сохраняем данные в новый файл
    names = ['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password']
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writerows(reader)

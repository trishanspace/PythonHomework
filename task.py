# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. 
# Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе

# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller


# phone_book = {123: ('Нехаев', "Михаил", "8900111", "друг"),
#             124: ("Петров", "Сергей", "8901222", "враг")}
phone_book = {}

def menu(data: dict):
    while True:
        print('Выберите действие: ')
        print('1 - создать новую запись')
        print('2 - распечатать содержимое справочника')
        print('3 - импортировать данные с текстового файла')
        
        get = input('Введите действие: ')
        if get == '':
            print('До свидания!')
            break
        elif get == '1':
            data = create(data, get_data())
        elif get == '2':
            print_phone_book(data)
        elif get == '3':
            name_file = get_file_name()
            batch_data = get_batch_data(name_file)
            data = batch_create(data, batch_data)
        else:
            print('Некорректный ввод данных, введите ещё раз: ')
def create(data: dict) -> dict: # добавляет запись в существующую телефонную книгу
    return data

def print_phone_book(data: dict) -> None:
    for key, values in data.items():
        print(f'Идентификатор: {key}, {values}')

def get_data() -> tuple: # запрашивает данные у пользователя
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    discription = input('Введите описание: ')
    return (surname, name, phone, discription)

def get_file_name() -> str:
    return input('Введите имя файла: ')
def get_batch_data(file: str) -> list:
    lst = []
    with open('data08_1.txt', 'r', encoding='utf-8') as surname:
        for line in file:
            temp = tuple(line.strip().split('#'))
            lst.append(temp)
    return lst

def batch_create(data: dict, batch_data) -> dict:
    
    for elem in batch_data:
        data = create(data, elem)
    return data

def select_surname (lst, surname):
    return ((lambda x, y, z, w: f'{x} {y} {z} {w}') (x, y, z, w) for x, y, z, w in lst if x [0][0][1] == surname [0][1])

menu(phone_book)
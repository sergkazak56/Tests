import copy

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def search_doc_in_base(doc_list, doc_num):
    if doc_list:
        for doc in doc_list:
            if doc['number'] == doc_num:
                return doc
    return False

def search_doc_in_dir(dir_list, doc_num):
    if dir_list:
        for shelf, numbers in dir_list.items():
            if doc_num in numbers:
                return shelf
    return False

def add_doc(doc_list, dir_list,  doc_type='', doc_num='', doc_owner='', doc_shelf=''):
    if not search_doc_in_base(doc_list, doc_num):
        if dir_list.get(doc_shelf) is not None:
            if doc_type.strip() and doc_num.strip() and doc_owner.strip() and doc_shelf.strip():
                doc_list.append({"type": doc_type, "number": doc_num, "name": doc_owner})
                dir_list[doc_shelf].append(doc_num)
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def delete_doc(doc_list, dir_list, doc_num):
    doc = search_doc_in_base(doc_list, doc_num)
    if doc:
        doc_list.remove(doc)
        shelf = search_doc_in_dir(dir_list, doc_num)
        if shelf:
            dir_list[shelf].remove(doc_num)
        return f'Документ № {doc_num} удален из базы и хранилища.'
    else:
        return 'Такого номера документа нет в базе!'

# def print_name(doc_list, doc_num):
#     ''' Функция печатает имя владельца по номеру документа в базе.
#         Входной параметр:
#         1. doc_list - база, организованная в виде списка словарей с ключами:
#             "type"    - тип документа
#             "number"  - номер документа
#             "name"    - имя и фамилия владельца
#     '''
#     doc = search_doc_in_base(doc_list, doc_num)
#     if doc:
#         return f'\nВладелец документа № {doc_num} - {doc["name"]}.'
#     else:
#         return f'\nВладелец документа № {doc_num} не найден в базе!'
#
# def print_shelf(dir_list):
#     ''' Функция печатает номер полки, где хранится документ.
#         Входной параметр:
#         1. dir_list - хранилище, организованное в виде словаря.
#             Ключи     - наименования полок
#             Значения  - список номеров документов на полке
#     '''
#     doc_num = input('\nВведите номер документа: ')
#     shelf = search_doc_in_dir(dir_list, doc_num)
#     if shelf:
#         print(f'\nДокумент № {doc_num} хранится на полке № {shelf}.')
#     else:
#         print(f'\nДокумент № {doc_num} не найден в хранилище!')
#
# def print_doc_listing(doc_list):
#     ''' Функция печатает список всех документов в виде таблицы:
#         Тип:            Номер:            Владелец:
#         Входной параметр:
#         1. doc_list - база, организованная в виде списка словарей с ключами:
#             "type"    - тип документа
#             "number"  - номер документа
#             "name"    - имя и фамилия владельца
#     '''
#     if doc_list:
#         print('\nСписок всех документов базы:')
#         print('\nТип:\t\t\t\tНомер:\t\t\t\tВладелец:')
#         for doc in doc_list:
#             print(f'{doc["type"]}', end=(20 - len(doc["type"])) * " ")
#             print(f'{doc["number"]}', end=(20 - len(doc["number"])) * " ")
#             print(doc["name"])
#     else:
#         print('\nВ базе нет ни одного документа!')
#
# def print_dir_listing(dir_list):
#     ''' Функция печатает списки документов в хранилище в виде таблицы:
#         Полка №:            Номера документов:
#         Входной параметр:
#         1. dir_list - хранилище, организованное в виде словаря.
#             Ключи     - наименования полок
#             Значения  - список номеров документов на полке
#     '''
#     if dir_list:
#         print('\nСписок всех документов хранилища:')
#         print('\nПолка №:\t\tНомера документов:')
#         for shelf, numbers in dir_list.items():
#             print(f'{shelf}', end=(16 - len(shelf)) * " ")
#             print(numbers)
#     else:
#         print('\nВ хранилище нет ни одного документа!')
#
# def move_doc(dir_list):
#     ''' Функция перемещает документ в хранилище с одной полки на другую по номеру.
#         Входные параметры:
#         1. dir_list - хранилище, организованное в виде словаря.
#             Ключи     - наименования полок
#             Значения  - список номеров документов на полке
#         Возвращает измененный: dir_list
#     '''
#     doc_num = input('\nВведите номер документа: ')
#     old_shelf = search_doc_in_dir(dir_list, doc_num)
#     if old_shelf:
#         new_shelf = input('На какую полку переместить документ? ')
#         if dir_list.get(new_shelf) is not None:
#             dir_list[new_shelf].append(doc_num)
#             dir_list[old_shelf].remove(doc_num)
#             print(f'\nДокумент № {doc_num} перемещен полку № {new_shelf} в хранилище.')
#         else:
#             print('\nУказанной полки нет в хранилище!')
#     else:
#         print('\nВы пытаетесь переместить несуществующий документ!')
#     return dir_list
#
# def add_shelf(dir_list):
#     ''' Функция добавляет новую полку в хранилище.
#         Входные параметры:
#         1. dir_list - хранилище, организованное в виде словаря.
#             Ключи     - наименования полок
#             Значения  - список номеров документов на полке
#         Возвращает измененный: dir_list
#     '''
#     new_shelf = input('\nВведите номер новой полки: ')
#     if new_shelf.strip(' '):
#         if dir_list.get(new_shelf) is None:
#             dir_list[new_shelf] = []
#             print(f'\nНовая полка № {new_shelf} добавлена в хранилище.')
#         else:
#             print('\nТакая полка уже есть в хранилище!')
#     else:
#         print('\nИмя полки не может быть пустым!')
#     return dir_list
#
# def print_base(old_docs, new_docs, old_dirs, new_dirs):
#     ''' Функция выводит на печать в виде таблиц старую и измененную
#         базы и хранилища документов.
#         Входные параметры:
#         1. old_docs, new_docs - старая и измененная базы, организованные
#         в виде списков словарей с ключами:
#             "type"    - тип документа
#             "number"  - номер документа
#             "name"    - имя и фамилия владельца
#         2. old_dirs, new_dirs - старое и измененное хранилища,
#         организованные в виде словарей.
#             Ключи     - наименования полок
#             Значения  - список номеров документов на полке
#     '''
#     print()
#     print(60 * '-')
#     print('СТАРАЯ БАЗА ДОКУМЕНТОВ:')
#     print_doc_listing(old_docs)
#     print(60 * '-')
#     print('ИЗМЕНЕННАЯ БАЗА ДОКУМЕНТОВ:')
#     print_doc_listing(new_docs)
#     print(60 * '-')
#     print('СТАРОЕ ХРАНИЛИЩЕ ДОКУМЕНТОВ:')
#     print_dir_listing(old_dirs)
#     print(60 * '-')
#     print('ИЗМЕНЕННОЕ ХРАНИЛИЩЕ ДОКУМЕНТОВ:')
#     print_dir_listing(new_dirs)
#     print(60 * '-')
#
# def database_query(doc_list, dir_list):
#     ''' Функция выполняет введенную пользователем команду для изменения или
#         запроса базы или хранилища документов. Список команд выводится
#         на терминал.
#         Входные параметры:
#         1. doc_list - база, организованная в виде списка словарей с ключами:
#             "type"    - тип документа
#             "number"  - номер документа
#             "name"    - имя и фамилия владельца
#         2. dir_list - хранилище, организованное в виде словаря.
#             Ключи     - наименования полок
#             Значения  - список номеров документов на полке
#         Возвращает измененные: doc_list, dir_list
#     '''
#     doc_list_copy = doc_list.copy()
#     dir_list_copy = copy.deepcopy(dir_list)  # любое другое копирование вложенного словаря типа
#     # dir_list_copy=dir_list.copy() или # dir_list_copy={key: val for key, val in dir_list.item()}
#     # и даже через собственные функции при изменении оригинала изменяет и копию и наоборот
#     while True:
#         print('''Введите одну из следующих команд для работы с документами:
#         p – запрос имени владельца документа;
#         s – запрос полки, на которой хранится документ хранилище;
#         l – запрос списка всех документов в базе;
#         a – добавление нового документа в базу и в хранилище;
#         d – удаление документа из базы и из хранилища;
#         m – перемещение документа на другую полку в хранилище;
#         as – добавление новой полки в хранилище;
#         br - прервать выполнение команд''')
#         method = input('\nКоманда: ')
#         if method == 'p':
#             print_name(doc_list, doc_num)
#         elif method == 's':
#             print_shelf(dir_list)
#         elif method == 'l':
#             print_doc_listing(doc_list)
#         elif method == 'a':
#             doc_list, dir_list = add_doc(doc_list, dir_list)
#         elif method == 'd':
#             doc_list, dir_list = delete_doc(doc_list, dir_list)
#         elif method == 'm':
#             dir_list = move_doc(dir_list)
#         elif method == 'as':
#             dir_list = add_shelf(dir_list)
#         elif method == 'br':
#             break
#         else:
#             print('\nНекорректная команда')
#         if input('\nХотите повторить запрос? (да - y/нет - n) ') != 'n':
#             continue
#         else:
#             break
#     if input('\nПоказать сравнение старых и измененных данных? (да - y/нет - n) ') != 'n':
#         print_base(doc_list_copy, doc_list, dir_list_copy, dir_list)
#     return doc_list, dir_list
#
# def main():
#     print('ЗАДАЧИ № 1 и № 2\n')
#     print('*************************************************\n')
#     documents, directories = database_query(documents, directories)
#     print('\n*************************************************\n')
#
# if __name__ == '__main__':
#     print(search_doc_in_base(documents, '11-2'))
#     print(search_doc_in_dir(directories, ''))
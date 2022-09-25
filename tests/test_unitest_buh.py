# Решение задания № 1
import unittest
from buh import search_doc_in_base, search_doc_in_dir, add_doc, delete_doc, documents, directories
from parameterized import parameterized

class TestFunctions(unittest.TestCase):

    # Тестирование функции поиска документа по номеру
    @parameterized.expand(
        [
            (documents, '11-2', {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'}),
            (documents, '10006', {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}),
            (documents, '2222222', False),
            (documents, '3333333', True), # провальный тест
            (documents, '10006', '"type": "insurance", "number": "10006", "name": "Аристарх Павлов"')  # провальный тест
        ]
    )
    def test_search_doc_in_base(self, doc_list, doc_num, result):
        fun_result = search_doc_in_base(doc_list, doc_num)
        self.assertEqual(fun_result, result)

    # Тестирование функции поиска номера полки, где хранится документ
    @parameterized.expand(
        [
            (directories, '11-2', '1'),
            (directories, '10006', '2'),
            (directories, '', False),
            (directories, '3333333', True),  # провальный тест
            (directories, '10006', '3')  # провальный тест
        ]
    )
    def test_search_doc_in_dir(self, dir_list, doc_num, result):
        fun_result = search_doc_in_dir(dir_list, doc_num)
        self.assertEqual(fun_result, result)

    # Тестирование функции добавления документа в базу
    @parameterized.expand(
        [
            (documents, directories,  "passport", "5615 333333", "Иванов Иван", "3"),
            (documents, directories, "noname", "1234", "Петров Петр", "2"),
            (documents, directories, "noname", "1234", "Петров Петр", "2"),
            (documents, directories, "passport", "2207 876234", "Сидоров Сидор", "1"),
            (documents, directories, "noname", "1234", "Петров Петр", "2")
        ]
    )
    def test_add_doc(self, doc_list, dir_list, doc_type, doc_num, doc_owner, doc_shelf):
        fun_result = add_doc(doc_list, dir_list, doc_type, doc_num, doc_owner, doc_shelf)
        self.assertIsInstance(fun_result, bool)

# Пробовал функцию "test_delete_doc" прописать в классе "class TestFunctions", однако на какое бы место я ее не ставил,
# она исполнялась первой, удаляла данные из списков и тесты по остальным функциям сыпались.
# Пришлось вынести ее в отдельный класс.
class TestDeleteFunction(unittest.TestCase):
    # Тестирование функции удаления документа из базы
    @parameterized.expand(
        [
            (documents, directories,  '11-2', 'Документ № 11-2 удален из базы и хранилища.'),
            (documents, directories, '10006', 'Документ № 10006 удален из базы и хранилища.'),
            (documents, directories, '', False), # провальный тест
            (documents, directories, '3333333', 'Такого номера документа нет в базе!'),
            (documents, directories, '10006', 8)  # провальный тест
        ]
    )
    def test_delete_doc(self, doc_list, dir_list, doc_num, result):
        fun_result = delete_doc(doc_list, dir_list, doc_num)
        self.assertEqual(fun_result, result)





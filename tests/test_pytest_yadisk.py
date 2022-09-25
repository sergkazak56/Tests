# Решение задания № 2
import pytest
from ya_disk import create_folder, check_folder, delete_folder, HEADERS

create_list = [
    ('new_folder1', HEADERS, 201),
    ('new_folder2', HEADERS, 201),
    ('new_folder1', HEADERS, 409)
]

check_list = [
    ('new_folder1', HEADERS, 'new_folder1'),
    ('new_folder2', HEADERS, 'new_folder2'),
    ('new_folder1', HEADERS, 'new_folder1'),
    ('new_folder3', HEADERS, False) # здесь должна быть ошибка при проверке типа данных
]

delete_list = [
    ('new_folder1', HEADERS, 204),
    ('new_folder2', HEADERS, 204),
    ('new_folder1', HEADERS, 404),
]


class TestYaDisk:

    @pytest.mark.parametrize("folder_name, headers, result", create_list)
    def test_create_folder(self, folder_name, headers, result):
        get_result = create_folder(folder_name, headers)
        assert get_result == result

    @pytest.mark.parametrize("folder_name, headers, result", check_list)
    def test_check_folder(self, folder_name, headers, result):
        get_result = check_folder(folder_name, headers)
        assert get_result == result
        assert isinstance(get_result, str)      # or isinstance(get_result, bool)

    @pytest.mark.parametrize("folder_name, headers, result", delete_list)
    def test_delete_folder(self, folder_name, headers, result):
        get_result = delete_folder(folder_name, headers)
        assert get_result == result
        assert isinstance(get_result, int)
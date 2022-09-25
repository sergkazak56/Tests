import requests

TOKEN = '*********************' # Здесь должен быть ваш ТОКЕН для ЯндексДиска
YA_DISK_URL = 'https://cloud-api.yandex.net/v1/disk/resources'
HEADERS = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(TOKEN)
    }

def create_folder(folder_name, headers):
    """
    Функция создание папки в корневом каталоге Яндекс диска
    :param folder_name: имя создаваемой папки
    :param headers: заголовки запроса
    :return: request_put.status_code: код успешности или неуспешности создания новой папки
    """
    url = f'{YA_DISK_URL}?path={folder_name}'
    request_put = requests.put(url , headers=headers)
    return request_put.status_code

def check_folder(folder_name, headers):
    """
    Функция проверки наличия папки корневом каталоге Яндекс диска
    :param folder_name: имя создаваемой папки
    :param headers: заголовки запроса
    :return: json с именем и типом объекта, если он в наличие и False, если объект отсутствует
    """
    url = f'{YA_DISK_URL}?path={folder_name}'
    response_get = requests.get(url, headers=headers)
    if response_get.ok:
        return response_get.json().get('name')
    else:
        return False

def delete_folder(folder_name, headers):
    """
    Функция удаления папки в корневом каталоге Яндекс диска
    :param folder_name: имя создаваемой папки
    :param headers: заголовки запроса
    :return: request_put.status_code: код успешности или неуспешности удаления папки
    """
    url = f'{YA_DISK_URL}?path={folder_name}'
    request_put = requests.delete(url , headers=headers)
    return request_put.status_code

def main():
    folder_name = 'new_folder'
    print(create_folder(folder_name, HEADERS))
    print(check_folder(folder_name, HEADERS))
    print(delete_folder(folder_name, HEADERS))

if __name__ == '__main__':
    main()


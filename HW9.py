# ЗАДАЧА 1

import requests as rq
# url = "https://superheroapi.com/api/2619421814940190/"
# hulk = url + "search/Hulk"
# capitan = url + "search/Captain America"
# thanos = url + 'search/Thanos'
# hulk_data = (int(rq.get(hulk).json()['results'][0]['powerstats']['intelligence']), 'hulk')
# capitan_data = (int(rq.get(capitan).json()['results'][0]['powerstats']['intelligence']), 'capitan')
# thanos_data = (int(rq.get(thanos).json()['results'][0]['powerstats']['intelligence']),'thanos')
# hero_list = [hulk_data, capitan_data, thanos_data]
# print(sorted(hero_list, reverse = True)[0][1])

# # print (f'Hulk inteligence is {hulk_int}, Capitan America intelligence is {capitan_int}, Thanos intelligence is {thanos_int}',)

# ЗАДАЧА 2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        create_folder = '/v1/disk/resources'
        url = 'https://cloud-api.yandex.net:443'
        myheaders = {"Authorization": f"OAuth {self.token}"}
        rq.put(f'{url + create_folder}?path=test_folder' , headers = myheaders)
        upload = '/v1/disk/resources/upload'
        result = rq.get(f'{url+upload}?path=test_folder/{file_path}', headers = myheaders)
        url2 = (result.json()['href'])
        rq.put(url2, files = {'file':open(file_path, encoding = 'utf-8')})
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'finalfile.txt'
    token = 'AQAAAAAgbfjgAADLW5KUMW4yhES_u6DINqCtVh4'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
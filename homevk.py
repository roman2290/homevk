import requests
import pprint
import json
from tqdm import trange, tqdm
from time import sleep



class VK:
    # Получени токена
    def __init__(self, access_token, user_id, owner_id, version='5.131'):
        self.owner_id = owner_id
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()
    
    # Получение и закрузка фото с профиля
    def foto_project(self, owner_id, offset = 0, count = 4):
        self.offset = offset,
        self.count = count,
        self.owner_id = owner_id
        url_vk = 'https://api.vk.com/method/photos.get'
        params_vk = {
                'owner_id': owner_id,
                'count': count,
                'photo_sizes': 0,
                'album_id': 'profile',
                'extended': 1,
                'offset': offset}
        response = requests.get(url_vk, params={**self.params, **params_vk, **headers})
        image_vk = response.json()['response']['items'][3]['sizes'][3]['url'][3]
        for file in response:
            image_vk = file['sizes'][-1]['url']
            file_name = image_vk.split('/')[-1]

        with open('image.jpg', 'wb') as f:
            response = requests.get(file_name)
            f.write(response.content)
        return response


class Yandex:
    #создаие папки на ядиске
    def __init__(self, path):
        self.path = path
   
    def foto_yandex_disk(self):
        url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {"path": 'Image'}
        headers = {"Authorization": "OAuth y0_AgAAAAAOk2cQAADLWwAAAAEDecVcAACa71RZu3dKkKhY9AElp54ZOVdl0w"}
        response = requests.put(url_create_folder, params=params, headers=headers)
        print(response.json())
    
    def foto_upload(self, foto_folder):
        self.foto_folder = foto_folder
        self.params = {'foto_folder': self.foto_folder}
        url_load = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {"path": f'{"Image"}/{foto_folder}'}
        response = requests.get(url_load, params=params, headers=headers)
        with open('image.jpg', 'rb') as f:
            url_upload = response.json()['href']
            requests.put(url_upload, files={'file': f})
        
        for img in tqdm(url_upload):
            print(img)
        
        
        
        
        
    
 

access_token = 'token'
headers = {'Authorization' :''}
user_id = 75476193
owner_id = 75476193 
vk = VK(access_token, user_id, owner_id)
token = ''

headers = {'Authorization': f'OAuth {token}'}




foto_folder = {'Image'}
url_upload = {'Image'}
Image = {'Image'}
file_name = ('Image')
path={f'Image/{foto_folder}'}
yandex = Yandex(path)
foto_folder = ['href']

pprint.pprint(yandex.foto_yandex_disk())
print(yandex.foto_upload(foto_folder))
pprint.pprint(vk.users_info())
pprint.pprint(vk.foto_project(owner_id, count = 4))

  


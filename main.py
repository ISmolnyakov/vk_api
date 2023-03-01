from pprint import pprint
from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests

with open('token.txt', 'r') as file:
    token = file.readlines()

with open('user_token.txt', 'r') as u_file:
    user_token = u_file.readlines()

vk = vk_api.VkApi(token=token)
vk_user = vk_api.VkApi(token=user_token)
longpoll = VkLongPoll(vk)
vk._auth_token()


def find_city():
    params = {'access_token': token,
              'v': '5.131',
              'user_ids': 15055184,
              'fields': 'city'}
    result = vk.method("users.get", params)
    user_city = result[0]['city']['title']
    return user_city


def get_user_sex():
    params = {'access_token': token,
              'v': '5.131',
              'user_ids': 15055184,
              'fields': 'sex'}
    req = vk.method("users.get", params)
    if req[0]['sex'] == 2:
        opposite_sex = 1
    elif req[0]['sex'] == 1:
        opposite_sex = 2
    else:
        return f'Error'
    return opposite_sex

def get_photo():
    params = {'access_token': user_token,
              'v': '5.131',
              'owner_id': 15055184,
              'album_id': 'profile',
              'extended': 1,
              }
    req = vk_user.method("photos.get", params)
    # pprint(req)
    photo_info = {}
    for i in range(req['count']):
        # photo_info[f'''{req['items'][i]['id']} likes'''] = req['items'][i]['likes']['count']
        # photo_info[f'''{req['items'][i]['id']} info'''] = req['items'][i]['sizes'][-1]
        photo_info[req['items'][i]['id']] = f'''likes {req['items'][i]['likes']['count']}, {req['items'][i]['sizes'][-1]}'''
    pprint(photo_info)
    return req

find_city()
# get_photo()
get_user_sex()
# def write_msg(user_id, message):
#     vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})


# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW:
#
#         if event.to_me:
#             request = event.text
#
#             if request == "привет":
#                 write_msg(event.user_id, f"Хай, {event.user_id}")
#             elif request == "пока":
#                 write_msg(event.user_id, "Пока((")
#             else:
#                 write_msg(event.user_id, "Не поняла вашего ответа...")

# def get_sex(user_id):
#         params = {'access_token': user_token,
#                   'user_ids': user_id,
#                   'fields': 'sex',
#                   'v': '5.131'}
#         get_s = vk.method('users.get', params)
#         response = get_s.json()
#         try:
#             information_list = response['response']
#             for i in information_list:
#                 if i.get('sex') == 2:
#                     find_sex = 1
#                     return find_sex
#                 elif i.get('sex') == 1:
#                     find_sex = 2
#                     return find_sex
#         except KeyError:
#             self.write_msg(user_id, 'Ошибка получения токена, введите токен в переменную - user_token')

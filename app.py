from vk_api import VkApi
from config import settings
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests
vk_session = VkApi(token=settings['vk_access_token'])
longpoll = VkBotLongPoll(vk_session, 209504247)
for event in longpoll.listen():
    elements = event.object.get("attachments", [])
    c = []

    try:
        for el in elements:
            c.append(el.get('photo').get('sizes')[-1].get("url"))
    except KeyError:
        print()
    files_photo = {}
    for i in c:
        photo = requests.get(''.join(i))
        files_photo['file'+str(i)] = ('img'+str(i)+'.jpg', photo.content, 'image/png')
    print(len(files_photo))
    new_dict = {}
    for i in files_photo:
        new_dict['files'] = files_photo.items()
    print(new_dict)
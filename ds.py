from vk_api import VkApi
from config import settings
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests

vk_session = VkApi(token=settings['vk_access_token'])
longpoll = VkBotLongPoll(vk_session, 209504247)# id группы вконтакте
for event in longpoll.listen():
    print(event.type)
    print(event.object)
    text =event.object['text']
    print(text)

    video = event.object.get("attachments", [])
    print(video)
    c =[]
    try:
        for el in range(len(video)):
            attachments_el = video[el]
            attachments_el1 = attachments_el['photo']
            attachments_el2 = attachments_el1['sizes']
            attachments_el3 = attachments_el2[-1]
            attachments_el4 = attachments_el3['url']
            c.append(attachments_el4)
    except KeyError:
        r = requests.post(
            'https://discord.com/api/v9/channels/919633591472898078/messages',
            headers={
                'Authorization': 'Bot OTE5Mjc3MzgyNjE4MjAyMjMz.YbTdxw.u8A5OLkUzZl9vgxlzJLaMsigZLU'
            },
            data={
                'content': (text)
            },

        )
        print(r.status_code, r.json())
        continue
    except:
        continue

    print(c)


    photo = requests.get(''.join(c))

    r = requests.post(
        'https://discord.com/api/v9/channels/919633591472898078/messages',
        headers={
            'Authorization': 'Bot OTE5Mjc3MzgyNjE4MjAyMjMz.YbTdxw.u8A5OLkUzZl9vgxlzJLaMsigZLU'
        },
        data={
            'content': (text)
        },

        files={
            'file1': (
            'img1.jpg',
            photo.content,
            'image/png'
            ),
            'file2': (
            'img2.jpg',
            photo.content,
            'image/png'
            )
            }
    )


    print(r.status_code, r.json())

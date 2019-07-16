import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

token = "insert_here"

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            if request == "Привет":
                write_msg(event.user_id, "Хай")
            elif request == "Пока":
                write_msg(event.user_id, "Пока")
            else:
                write_msg(event.user_id, "Непонятно")

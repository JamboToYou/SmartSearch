import vk
from access_data import data

sess = vk.Session(access_token=data['access_token'])
vkApi = vk.API(sess)

def send_message(user_id, message):
    vkApi.messages.send(user_id=user_id, message=message, v=5.73)

"""
обернуть в функции методы api а именно
get_posts
если что я скажу еще
"""
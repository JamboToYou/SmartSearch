import vk

sess = vk.Session(access_token='17e584f856cadd64eb3aa7acb3537fdbcea60479ef87cd05f05123a34dbe8f41e344f9502def91c13d544')
vkApi = vk.API(sess)

def send_message(user_id, message):
    vkApi.messages.send(user_id=user_id, message=message, v=5.73)
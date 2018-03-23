import vk

#sess = vk.Session(access_token='17e584f856cadd64eb3aa7acb3537fdbcea60479ef87cd05f05123a34dbe8f41e344f9502def91c13d544')
sess = vk.AuthSession(app_id=6389848, user_login='89913970602', user_password='Xs(f*84F2i1r9%n')
vkApi = vk.API(sess)

print(vkApi.wall.get(domain='emtech', v=5.73)['items'][0]['text'])
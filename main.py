# coding=utf-8
import unparse
from dbmanager import execute

linkses = unparse.get_links('habrahabr.ru','android')
views = ("Android","Java","C++","C#","Swift")


def create_view_for_links(links):
    view=""
    for key,value in links.items():
        view += "{}\n{}\n".format(key, value)
    return view

def create_view_for_views(view):
    result=""
    for i in range(0,len(view)):
        result+= views[i]+"\n"
    return result


##############################

def create_view_add_user(user_id):
    r = execute("add_user",user_id=user_id)
    if(r==1):
        return "Добавление пользователя прошло успешно"
    elif(r==0):
        return "Ошибка добавления пользователя"

def create_view_add_category(category_name):
    r = execute("add_category", category_name=category_name)
    if (r==1):
        return "Добавление категории прошло успешно"
    elif(r==0):
        return "Ошибка добавления категории"

def create_view_subscribe_to_category(category_id, user_id):
    r = execute("subscribe_to_category", category_id=category_id, user_id=user_id)
    if (r == 1):
        return "Подписка на категорию прошла успешно"
    elif (r == 0):
        return "Ошибка подписки на категорию"

subsc_err = "Укажите ID категории"

def create_view_add_content(category_id, source, user_id):
    r = execute("add_content", category_id=category_id, source=source)
    if (r==1):
        return "Добавление содержания прошло успешно"
    elif(r==0):
        return "Ошибка добавления содержания"


def create_view_get_categories():
    view = ""
    result = execute("get_categories")
    for cortege in result:
        view+="{}. {}\n".format(str(cortege[0]), cortege[1])
    return view

def create_view_content_of_category(category_id):
    view = {}

    view_string = ""

    result = execute("get_content_of_category",category_id=category_id)
    keyword = execute("get_category_name_by_id", category_id=category_id)[0][0]
    for content in result:
        view = dict(view, **unparse.get_links(content[0], keyword))

    for key,value in view.items():
        view_string+="{}.\n {}\n".format(key,value)

    return view_string


##############################


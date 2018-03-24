# coding=utf-8

from dbmanager import execute

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
    if r == 1:
        return "Подписка на категорию прошла успешно"
    else:
        return "Ошибка подписки на категорию"

subsc_err = "Укажите ID категории"

def create_view_add_content(category_id, source, user_id):
    r = execute("add_content_from_user", category_id=category_id, source=source, user_id=user_id)
    if (r==1):
        return "Добавление содержания прошло успешно"
    elif(r==0):
        return "Ошибка добавления содержания"

adderr = "Не введен один из параметров"

def create_view_get_categories():
    view = ""
    result = execute("get_categories")
    for cortege in result:
        view+="{}. {}\n".format(str(cortege[0]), cortege[1])
    return view

def create_view_content_of_category(category_id):
    """
    view = {"--Заголовки":"Ссылки"}

    view_string = ""

    keyword = execute("get_category_name_by_id", category_id=category_id)
    if keyword == ():
        return "Нет категории с таким ID"

    keyword = keyword[0][0]

    result = execute("get_content_of_category",category_id=category_id)
    if result == ():
        return "У этой категории пока нет контента"

    for content in result:
        view = dict(view, **unparse.get_links(content[0], keyword))

    for key,value in view.items():
        view_string += "--{}.\n {}\n".format(key,value)

    return view_string
    """
    result = execute("get_content_of_category", category_id=category_id)
    if result == ():
        return "Нет ресурсов"

    view = ''

    for cont in result:
        view += '{}\n'.format(cont[0])

    return view

cntctgerr = "Не указан ID категории"

def create_view_leave_from_category(user_id, category_id):
    view = ""
    result = execute("leave_from_category", category_id = category_id,user_id = user_id )
    if result == 1:
        view += "Успешно удалено"
    else:
        view += "Вы не подписаны на эту категорию"
    return view

leaveerr = "Не указан ID категории"

def create_view_delete_source(content_id, user_id, category_id):
    view = ""
    result = execute("delete_source", content_id=content_id, user_id=user_id, category_id=category_id)
    if result == 1:
        view += "Успешно удалено"
    else:
        view += "Ошибка удаления"
    return view

delerr = "Не указан один из параметров"

def create_view_form_digest(source_dict):
    view = ""

    for title, url in source_dict.items():
        view += "{}\n{}\n".format(title, url)

    return view
##############################


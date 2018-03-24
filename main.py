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

def create_view_get_categories():
    view = ""
    result = execute("get_categories")
    for cortege in result:
        view+="{}. {}".format(str(cortege[0]), cortege[1])
    return view

def create_view_content_of_category(category_id):
    view = ""
    result = execute("get_content_of_category",category_id=category_id)
    for cortege in result:
        view+="{}. {}".format(str(cortege[0]),cortege[1])
    return view

def create_view_subscribe_to_category(category_id, user_id):
    view = ""
    result = execute("subscribe_to_category", category_id=category_id, user_id=user_id)
    for cortege in result:
        view += "{}. {}".format(str(cortege[0]), cortege[1], cortege[2])
    return view

##############################


def main():

if __name__ == '__main__':
    main()

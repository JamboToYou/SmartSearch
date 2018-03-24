import requests
from dbmanager import execute
import vk_module
import main

def search():
    cat_list = execute("get_categories")
    for cat in cat_list:
        cat_users = execute("get_category_subscribers", category_id=cat[0])
        if cat_users == ():
            continue
        cont_corts = execute("get_content_of_category", category_id=cat[0])
        if cont_corts == ():
            continue
        cont_list = []
        for cont in cont_corts:
            cont_list.append(cont[0])
        search_result = requests.post('https://andreytyu.pythonanywhere.com/getLinks', json={"get_links":True, "site":cont_list, "keyword":cat[1]})

        view = main.create_view_form_digest(search_result.json())

        for user in cat_users:
            vk_module.send_message(user[0], view)

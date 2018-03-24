import pymysql
from access_data import data


def add_user(c, user_id):
    result = c.execute("INSERT INTO Users(user_id) VALUES(%s)", user_id)
    return result

def add_category(c, category_name):
    result = c.execute("INSERT INTO Categories(category_name) VALUES(%s)", category_name)
    return result

def subscribe_to_category(c, category_id, user_id):
    result = c.execute("INSERT INTO CategoriesList(user_id, category_id) VALUES(%s, %s)", (user_id, category_id))
    return result

def add_content(c, category_id, source):
    result = c.execute("INSERT INTO Content(source, category_id) VALUES(%s, %s)", (source, category_id))
    return result

def get_users(c):
    c.execute("SELECT user_id FROM Users")
    result = c.fetchall()
    return result

def get_categories(c):
    c.execute("SELECT category_id, category_name FROM Categories")
    result = c.fetchall()
    return result

def get_category_subscribers(c, category_id):
    c.execute("SELECT user_id FROM CategoryList WHERE category_id = %s", category_id)
    result = c.fetchall()
    return result

def get_content_of_category(c, category_id):
    c.execute("SELECT source FROM Content WHERE category_id = %s", category_id)
    result = c.fetchall()
    return result

#Андрей, посмотри, солнышко
def get_category_name_by_id(c, category_id):
    c.execute("SELECT name FROM Category WHERE category_id = %s", category_id)
    result = c.fetchall()
    return result
def leave_from_category(c, category_id, user_id):
    result = c.execute("DELETE FROM CategoryList WHERE user_id = %s AND category_id = %s",(user_id, category_id))
    return result
def delete_source(c,content_id,user_id,category_id):
    result = c.execute("")
    return result
methods = \
    {
        "add_user" : add_user,
        "add_category" : add_category,
        "subscribe_to_category" : subscribe_to_category,
        "add_content" : add_content,
        "get_users" : get_users,
        "get_categories" : get_categories,
        "get_category_subscribers" : get_category_subscribers,
        "get_content_of_category" : get_content_of_category,
        "get_category_name_by_id" : get_category_name_by_id,
        "leave_from_category" : leave_from_category,
        "delete_source" : delete_source
    }

def execute(method_name, **kwargs):
    with pymysql.connect(host=data['db_host'], user=data['user_login'], password=data['user_password'], db=data['db_name']) as c:
        result = None
        try:
            result = methods[method_name](c, **kwargs)
        except:
            raise
        finally:
            return result

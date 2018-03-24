import pymysql
from access_data import data


def add_user(c, user_id):
    result = c.execute("INSERT INTO Users(user_id) VALUES(%s)", user_id)
    return result

def add_category(c, category_name):
    result = c.execute("INSERT INTO Categories(category_name) VALUES(%s)", category_name)
    return result


methods = \
    {
        "add_user" : add_user,
        "add_category" : add_category
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

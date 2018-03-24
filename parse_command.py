# -*- coding: utf-8 -*-
import main
"""
1) Список тем для подписок /categorylist
2) Присоединиться к рассылке /join <id>
3) Добавить ресурс /addsource
4) Отписаться от дайджеста /leave <id>
5) Список источников /sourcelist <id>
6) удалить ресурс /deletesource <id_source>
"""
def parse_command(msg_obj):
    body = msg_obj["body"]
    usr_id = msg_obj["user_id"]
    if(body[0] == '/'):
        command_container = body[1:].split()
        command = command_container[0]
        if command == 'categorylist':
            return main.create_view_get_categories()
        elif command == 'join':
            try:
                category_id = command_container[1]
                return main.create_view_subscribe_to_category(category_id, usr_id)
            except:
                return main.subsc_err
        elif command == 'addsource':
            try:
                source = command_container[1]
                return main.create_view_add_content(source, )
            except:
                raise
        elif command == 'leave':
            #TODO
        elif command == 'sourcelist':
            category_id = command_container[1]
            return main.create_view_content_of_category(category_id)
        elif command == 'deletesource':
            #TODO


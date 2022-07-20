
import db


def generate_menu(db_file, menu_file):
    db_data = db.read_db_json(db_file)
    menus = ''

    for data in db_data:
        menus += '{}\n'.format(data)

    with open(menu_file, 'w') as am:
        am.write(menus)

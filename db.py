
import os
import json
import yaml


class Database:

    def __init__(self, db_file):
        if not os.path.isdir(os.path.dirname(db_file)):
            make_directory(os.path.dirname(db_file))

        if not os.path.isfile(db_file):
            json_data = json.dumps({}, indent=4)
            with open(db_file, 'w') as file:
                file.write(json_data)


def make_directory(path):
    os.makedirs(path)


def ingest_to_json(file, is_expression_node, *data):
    json_data = read_db_json(file)
    if is_expression_node:
        json_data.update(expression_dictionary_data(*data))
    else:
        json_data.update(animation_dictionary_data(*data))
    write_db_json(file, json_data)


def read_db_json(file):
    with open(file, 'r') as db:
        return json.load(db)


def write_db_json(json_file, json_data):
    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)


def remove_db_json(file, key):
    json_data = read_db_json(file)
    del json_data[key]
    write_db_json(file, json_data)


def animation_dictionary_data(*data):
    data = data[0]
    knob_dict = {data[0]: {
                     'expression': data[1],
                     'knobs': data[2]
                    }
                 }

    return knob_dict


def expression_dictionary_data(*data):
    data = data[0]
    knob_dict = {
            data[0]: {
                'temp_name0': data[1],
                'temp_name1': data[2],
                'temp_name2': data[3],
                'temp_name3': data[4],
                'temp_expr0': data[5],
                'temp_expr1': data[6],
                'temp_expr2': data[7],
                'temp_expr3': data[8],
                'expr0': data[9],
                'expr1': data[10],
                'expr2': data[11],
                'expr3': data[12],
                'knobs': data[13]
            }
        }

    return knob_dict


def load_yaml(file):
    with open(file, 'r') as kt:
        return yaml.load(kt, Loader=yaml.FullLoader)


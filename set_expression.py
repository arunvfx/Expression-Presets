
import os
import db

import nuke


class SetExpression:

    def __init__(self, item_selected, db_file, menu_file, is_expression_node):
        self.menu_item = item_selected
        self.menu_item_clicked = self.menu_item.split('/')[-1]

        self.is_expression_node = is_expression_node
        self.config = db.load_yaml('{}/preferences/config.yaml'.format(os.path.dirname(__file__)))
        self.db_file = db_file
        self.menu_file = menu_file

        self.knob_available = db.load_yaml(eval(self.config['KNOB_TYPES']))
        self.db = db.read_db_json(self.db_file)

        if self.is_expression_node:
            self.set_expression_node()
        else:
            self.expression = self.db[self.menu_item]['expression']
            self.query_node_knob()

    def set_expression(self, node, knob):
        index = SetExpression.query_knob_index()
        if node[knob].hasExpression(index=index):
            if index == -1:
                expression_exists = node[knob].animation(0).expression()
            else:
                expression_exists = node[knob].animation(index).expression()
            node[knob].setExpression(
                '{} + {}'.format(expression_exists, self.expression, index)
            )
        else:
            node[knob].setExpression(self.expression, index)

    @staticmethod
    def query_knob_index():
        try:
            index = """
            set thisanimation [animations]
            if {[llength $thisanimation] > 1} {
                return "-1"
            } else {
                return [lsearch [in [join [lrange [split [in $thisanimation {animations}] .] 0 end-1] .] {animations}] $thisanimation]
            }
            """
            index = int(nuke.tcl(index))
        except RuntimeError:
            index = -1

        return index

    def create_knobs(self, new_knob_name, knob_name, node):
        group = False
        for index, db_key in enumerate(self.db[self.menu_item]):
            if index == 0 and self.db[self.menu_item]['knobs']:
                self.create_tab(node)
                group_begin = nuke.Tab_Knob(new_knob_name, '{} : {}'.format(knob_name, self.menu_item_clicked), nuke.TABBEGINGROUP)
                node.addKnob(group_begin)
                group = True
            self.add_knobs(new_knob_name, node, self.db[self.menu_item][db_key])

        divider = nuke.Text_Knob('div_{}'.format(new_knob_name), '', '')
        if group:
            group_sin_end = nuke.Tab_Knob(
                new_knob_name, '{} : {}_end'.format(knob_name, self.menu_item_clicked), nuke.TABENDGROUP
            )
            node.addKnob(group_sin_end)
            node.addKnob(divider)

    def create_tab(self, node):
        if not 'WAVES_TAB' in node.knobs().keys():
            tab = nuke.Tab_Knob('WAVES_TAB', 'Controller')
            node.addKnob(tab)

    def validate_knob(self, node, knob_name, item_selected):
        existing_knobs = [k for k in node.knobs().keys()
                          if k.startswith('{}_{}_'.format(knob_name, item_selected))]
        if existing_knobs:
            max_sin = max(existing_knobs)
            return max_sin[:-2] + str(int(max_sin[-2:]) + 1).zfill(2)
        else:
            return '{}_{}_01'.format(knob_name, item_selected)

    def query_node_knob(self):
        node = nuke.thisNode()
        knob_name = nuke.thisKnob().name()
        new_knob_name = self.validate_knob(node, knob_name, self.menu_item_clicked.lower().strip().replace(' ', '_'))
        self.create_knobs(new_knob_name, knob_name, node)
        self.set_expression(node, knob_name)

    def add_knobs(self, new_knob_name, node, db_value):
        if isinstance(db_value, list) and db_value:
            for value in db_value:
                knob = None
                if self.is_expression_node:
                    updated_knob_name = value[1]
                else:
                    updated_knob_name = '{}_{}'.format(value[1], new_knob_name)

                if value[2] in self.knob_available['Range']:
                    knob = eval(self.knob_available['Knobs'][value[2]].format(updated_knob_name, value[0]))
                    node.addKnob(knob)
                    range_split = value[-1].split('-')
                    knob.setRange(int(range_split[0]), int(range_split[1]))
                    knob.setDefaultValue([int(range_split[0])])

                elif value[2] in self.knob_available['Vector']:
                    knob = eval(self.knob_available['Knobs'][value[2]].format(updated_knob_name, value[0]))
                    node.addKnob(knob)

                elif value[2] in self.knob_available['Strings']:
                    data_to_load = None
                    if value[2] in 'Python Script Button':
                        data_to_load = """{}""".format(value[-1])
                    elif value[2] in 'Pulldown Choice':
                        data_to_load = value[-1].split('\n')
                    knob = eval(self.knob_available['Knobs'][value[2]].format(
                        updated_knob_name, value[0], data_to_load)
                    )
                    node.addKnob(knob)

                if value[3]:
                    knob.setFlag(nuke.STARTLINE)
                else:
                    knob.clearFlag(nuke.STARTLINE)

                if not self.is_expression_node:
                    if value[2] in ('RGB Color Knob', 'RGBA Color Knob'):
                        self.expression = self.expression.replace(value[1], updated_knob_name)
                    else:
                        self.expression = '({})'.format(
                            self.expression.replace(value[1], updated_knob_name)
                        )

    # ----------------------------------- EXPRESSION NODE -------------------------------
    def set_expression_node(self):
        node = nuke.selectedNode()
        if node.Class() == 'Expression':
            for knob in ('temp_name0', 'temp_name1', 'temp_name2', 'temp_name3', 'temp_expr0', 'temp_expr1',
                         'temp_expr2', 'temp_expr3', 'expr0', 'expr1', 'expr2', 'expr3'):
                node[knob].setValue(self.db[self.menu_item][knob])

            self.create_knobs('', '', node)
        else:
            nuke.message('Select Expression Node to apply expressions!')








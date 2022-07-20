import os
import sys
sys.path.append(r'C:\Python37\Lib\site-packages')
import nuke
import db
import expressions
import set_expression
import remove_expression
import importlib as imp


def query_animation_menu():
    imp.reload(set_expression)
    imp.reload(expressions)
    imp.reload(remove_expression)

    config = db.load_yaml('{}/preferences/config.yaml'.format(os.path.dirname(__file__)).replace('\\', '/'))
    if nuke.thisNode().Class() == 'Expression':
        db_file = eval(config['DB_EXPRESSION']).replace('\\', '/')
        menu_file = eval(config['MENU_EXPRESSION']).replace('\\', '/')
    else:
        db_file = eval(config['DB_ANIMATION']).replace('\\', '/')
        menu_file = eval(config['MENU_ANIMATION']).replace('\\', '/')

    properties_expression = nuke.menu('Properties')
    if nuke.thisNode().Class() == 'Expression':
        properties_expression.addCommand('Clear Expressions', 'remove_expression.clear_expression_node()')
        properties_expression.addSeparator()
        properties_expression.addCommand(
            'Expression_menu', 'expressions.ExpressionWidget("{}", "{}", is_expression_node=True)'.format(
                db_file, menu_file)
        )
    else:
        properties_expression.removeItem('Expression_menu')
        properties_expression.removeItem('Clear Expressions')

    anim = nuke.menu("Animation")
    anim.addSeparator()
    anim.addCommand('Clear Expression and Knobs', 'remove_expression.remove_knob_expression()')
    anim.addSeparator()
    anim.addCommand('Add Expression', 'expressions.ExpressionWidget("{}", "{}")'.format(db_file, menu_file))
    anim.addSeparator()

    if os.path.exists(menu_file):
        with open(menu_file, 'r') as file:
            lines = file.readlines()
        for line in lines:
            if nuke.thisNode().Class() == 'Expression':
                properties_expression.addCommand(
                    line.strip(),
                    'set_expression.SetExpression("{}", "{}", "{}", is_expression_node=True)'.format(
                        line.strip(), db_file, menu_file)
                )
            else:
                anim.addCommand(
                    line.strip(),
                    'set_expression.SetExpression("{}", "{}", "{}", is_expression_node=False)'.format(
                        line.strip(), db_file, menu_file)
                )


nuke.addOnUserCreate(query_animation_menu)



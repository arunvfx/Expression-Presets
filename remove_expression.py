import re
import nuke
import set_expression


def remove_knob_expression():
    is_confirmed = nuke.ask('Are you sure you want to delete this animation?')

    if is_confirmed:
        node = nuke.thisNode()
        knob_name = nuke.thisKnob().name()
        index = set_expression.SetExpression.query_knob_index()
        knob_suffix = []
        expression = ''

        if node[knob_name].hasExpression(index=index):
            if index == -1:
                for ind in range(5):
                    try:
                        expression += node[knob_name].animation(ind).expression()
                    except AttributeError:
                        break
            else:
                expression = node[knob_name].animation(index).expression()
                for ind in range(5):
                    expression_temp = ''
                    if node[knob_name].hasExpression(index=ind) and not ind == index:
                        expression_temp = node[knob_name].animation(ind).expression()
                    if expression == expression_temp:
                        expression = ''
                        break

            content = re.split("[\(*-+%?\)/:<>=<==>=^&|!!\&&]", expression)
            for item in content:
                if item.strip() and len(item.split('_')) > 1:
                    knob_suffix.append(item.split('_', 1)[1].strip())

        knob_suffix = list(set(knob_suffix))

        if node[knob_name].hasExpression(index=index):
            current_frame_value = node[knob_name].value()
            node[knob_name].clearAnimated(index=index)
            node[knob_name].setValue(current_frame_value)

        if knob_suffix:
            for k in node.knobs():
                if len(k.split('_')) > 1 and k.split('_', 1)[1].strip() in knob_suffix:
                    node.removeKnob(node.knob(k))
                elif k in knob_suffix:
                    for i in range(2):
                        node.removeKnob(node.knob(k))


def clear_expression_node():
    node = nuke.selectedNode()
    for _knob in ('temp_name0', 'temp_name1', 'temp_name2', 'temp_name3', 'temp_expr0', 'temp_expr1', 'temp_expr2',
                  'temp_expr3', 'expr0', 'expr1', 'expr2', 'expr3'):
        node[_knob].setValue('')
        # node.removeKnob(node.knob(_knob))

import os
import sys
sys.path.append(r'C:\Python37\Lib\site-packages')
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import db
from ui import ui_loader as ui
import generate_menu
# from ui.expression import Ui_SmartExpressions
from ui.add_knobs import Knobs

import nuke
if nuke.NUKE_VERSION_MAJOR > 12:
    from importlib import reload

reload(generate_menu)


class ExpressionWidget(QWidget):

    def __init__(self, db_file, menu_file, is_expression_node=False, parent=None):
        QWidget.__init__(self, parent)
        # self.setupUi(self)
        ui.load_ui(os.path.join(os.path.dirname(__file__), 'ui/expression.ui').replace('\\', '/'), self)
        reload(db)

        self.is_expression_node = is_expression_node
        self.config = db.load_yaml('{}/preferences/config.yaml'.format(os.path.dirname(__file__)))
        self.db_file = db_file
        self.menu_file = menu_file
        self.expression_node_knobs = ('temp_name0', 'temp_name1', 'temp_name2', 'temp_name3', 'temp_expr0',
                                      'temp_expr1', 'temp_expr2', 'temp_expr3', 'expr0', 'expr1', 'expr2', 'expr3')

        self.ui_default()
        self.signal_ops()
        self.knob_types_menu()
        self.db = db.Database(self.db_file)
        self.show()

    def ui_default(self):

        if self.is_expression_node:
            self.frame_expression.hide()
            self.frame_expression_node.show()
            self.fill_expression_widget()
        else:
            self.frame_expression_node.hide()
            self.frame_expression.show()

        self.frame_right.hide()
        self.btn_clear.setIcon(QIcon('{}/icons/clear.png'.format(os.path.dirname(__file__))))
        self.btn_clear.setIconSize(QSize(20, 20))
        self.btn_save.setIcon(QIcon('{}/icons/save.png'.format(os.path.dirname(__file__))))
        self.btn_save.setIconSize(QSize(20, 20))
        self.btn_close.setIcon(QIcon('{}/icons/close.png'.format(os.path.dirname(__file__))))
        self.btn_close.setIconSize(QSize(18, 18))
        self.btn_edit.setIcon(QIcon('{}/icons/edit.png'.format(os.path.dirname(__file__))))
        self.btn_edit.setIconSize(QSize(20, 20))
        self.btn_delete.setIcon(QIcon('{}/icons/delete.png'.format(os.path.dirname(__file__))))
        self.btn_delete.setIconSize(QSize(20, 20))
        self.btn_remove_knob.setIcon(QIcon('{}/icons/minus.png'.format(os.path.dirname(__file__))))
        self.btn_remove_knob.setIconSize(QSize(20, 20))
        self.btn_add_knob.setIcon(QIcon('{}/icons/plus.png'.format(os.path.dirname(__file__))))
        self.btn_add_knob.setIconSize(QSize(20, 20))
        self.btn_expression_list.setIcon(QIcon('{}/icons/arrow.png'.format(os.path.dirname(__file__))))
        self.btn_save.setIconSize(QSize(24, 24))

    def signal_ops(self):
        self.btn_expression_list.clicked.connect(self.toggle_expressions)
        self.btn_edit.clicked.connect(self.edit_expression)
        self.btn_save.clicked.connect(self.save_expressions)
        self.btn_delete.clicked.connect(self.delete_expressions)
        self.btn_clear.clicked.connect(self.clear_expressions_ui)
        self.btn_remove_knob.clicked.connect(self.remove_knob_widget)
        self.btn_close.clicked.connect(self.close)

    def toggle_expressions(self):
        if self.frame_right.isVisible():
            self.frame_right.hide()
            self.btn_expression_list.setIcon(
                QIcon('{}/icons/arrow.png'.format(os.path.dirname(__file__)))
            )
        else:
            self.btn_expression_list.setIcon(
                QIcon('{}/icons/arrow1.png'.format(os.path.dirname(__file__)))
            )
            self.load_expressions_to_widget()
            self.frame_right.show()

    def knob_types_menu(self):
        menu = QMenu(self)
        float_point_slider = QAction('Floating Point Slider', self)
        position_2d = QAction('2d Position Knob', self)
        position_3d = QAction('3d Position Knob', self)
        width_knob = QAction('Width/Height Knob', self)
        uv_coordinate = QAction('UV Coordinate Knob', self)
        integer_knob = QAction('Integer Knob', self)
        divider = QAction('Divider', self)
        rgb_knob = QAction('RGB Color Knob', self)
        rgba_knob = QAction('RGBA Color Knob', self)
        check_box = QAction('Check Box', self)
        pyscript_btn = QAction('Python Script Button', self)
        pulldown_choice = QAction('Pulldown Choice', self)

        for knob in (float_point_slider, position_2d, position_3d, width_knob, uv_coordinate, integer_knob, divider,
                     rgb_knob, rgba_knob, check_box, pyscript_btn, pulldown_choice):
            menu.addAction(knob)

        menu.setStyleSheet('QMenu{background-color: #212121;}'
                           'QMenu::item:selected{background-color: #323232;}')

        float_point_slider.triggered.connect(lambda: self.knob_widget(float_point_slider.text()))
        position_2d.triggered.connect(lambda: self.knob_widget(position_2d.text()))
        position_3d.triggered.connect(lambda: self.knob_widget(position_3d.text()))
        width_knob.triggered.connect(lambda: self.knob_widget(width_knob.text()))
        uv_coordinate.triggered.connect(lambda: self.knob_widget(uv_coordinate.text()))
        integer_knob.triggered.connect(lambda: self.knob_widget(integer_knob.text()))
        divider.triggered.connect(lambda: self.knob_widget(divider.text()))
        rgb_knob.triggered.connect(lambda: self.knob_widget(rgb_knob.text()))
        rgba_knob.triggered.connect(lambda: self.knob_widget(rgba_knob.text()))
        check_box.triggered.connect(lambda: self.knob_widget(check_box.text()))
        pyscript_btn.triggered.connect(lambda: self.knob_widget(pyscript_btn.text()))
        pulldown_choice.triggered.connect(lambda: self.knob_widget(pulldown_choice.text()))

        self.btn_add_knob.setMenu(menu)

    def add_knob_widget(self, widget):
        item = QListWidgetItem()
        item.setSizeHint(QSize(0, 40))
        self.listWidget_knobs.addItem(item)
        self.listWidget_knobs.setItemWidget(item, widget)

    def knob_widget(self, data):
        self.add_knob_widget(Knobs(data))

    def save_expressions(self):
        # menu, enable, operations, frame_range, black_clamp, white_clamp, expressions, knobs = self.query_knob_data()
        is_expression_node = False
        if self.is_expression_node:
            is_expression_node = True
        db.ingest_to_json(self.db_file, is_expression_node, self.query_knob_data())
        generate_menu.generate_menu(self.db_file, self.menu_file)

    def query_knob_data(self):
        knob_type = ''
        knobs_list = []
        for row in range(self.listWidget_knobs.count()):
            widgets = self.listWidget_knobs.itemWidget(self.listWidget_knobs.item(row)).findChildren(QLineEdit)
            widgets.append(self.listWidget_knobs.itemWidget(self.listWidget_knobs.item(row)).findChild(QTextEdit))
            widgets.append(self.listWidget_knobs.itemWidget(self.listWidget_knobs.item(row)).findChild(QLabel))
            widgets.append(self.listWidget_knobs.itemWidget(self.listWidget_knobs.item(row)).findChild(QCheckBox))
            knob_list = []
            for widget in widgets:
                if widget.__class__.__name__ == 'NoneType':
                    continue
                elif widget.__class__.__name__ == 'QCheckBox':
                    knob_list.append(widget.isChecked())
                elif widget.__class__.__name__ == 'QTextEdit':
                    knob_list.append(widget.toPlainText())
                    # print(widget.toPlainText())
                else:
                    knob_type = widget.text()
                    knob_list.append(widget.text())
                    # print(widget.text())
            if knob_type in ('Floating Point Slider', 'RGB Color Knob', 'RGBA Color Knob',
                             'Python Script Button', 'Pulldown Choice'):
                knob_list.append(knob_list.pop(knob_list.index(knob_list[2])))

            knobs_list.append(knob_list)

        if self.is_expression_node:
            return self.lineEdit_label.text(), self.temp_name0.text(), self.temp_name1.text(), self.temp_name2.text(), \
                   self.temp_name3.text(), self.temp_expr0.text(), self.temp_expr1.text(), self.temp_expr2.text(), \
                   self.temp_expr3.text(),  self.expr0.text(), self.expr1.text(), self.expr2.text(), self.expr3.text(), \
                   knobs_list
        else:
            return self.lineEdit_label.text(), self.textEdit_expression.toPlainText(), knobs_list

    def load_expressions_to_widget(self):
        json_data = db.read_db_json(self.db_file)
        model = QStandardItemModel()
        self.listView_expressions.setModel(model)

        for key in json_data:
            model.appendRow(QStandardItem(key))

    def query_selected_expression(self):
        selected_index = self.listView_expressions.currentIndex()
        return self.listView_expressions.model().itemFromIndex(selected_index).text(), selected_index

    def edit_expression(self):
        selected_item, index = self.query_selected_expression()
        data = db.read_db_json(self.db_file)

        for key in data:
            if key == selected_item and not self.is_expression_node:
                self.textEdit_expression.clear()
                self.textEdit_expression.setText(data[key]['expression'])

            elif key == selected_item and self.is_expression_node:
                for knob in self.expression_node_knobs:
                    line_edit_widget = self.findChild(QLineEdit, knob)
                    line_edit_widget.clear()
                    line_edit_widget.setText(data[key][knob])

            if key == selected_item:
                self.lineEdit_label.clear()
                self.lineEdit_label.setText(key)
                self.listWidget_knobs.clear()
                for knob in data[key]['knobs']:
                    widgets = Knobs(knob[2], knob)
                    self.add_knob_widget(widgets)

    def delete_expressions(self):
        selected_item, row = self.query_selected_expression()
        self.listView_expressions.model().removeRow(row.row())
        db.remove_db_json(self.db_file, selected_item)
        generate_menu.generate_menu(self.db_file, self.menu_file)

    def clear_expressions_ui(self):
        self.textEdit_expression.clear()
        self.lineEdit_label.clear()
        self.listWidget_knobs.clear()

        if self.is_expression_node:
            for knob in self.expression_node_knobs:
                line_edit_widget = self.findChild(QLineEdit, knob)
                line_edit_widget.clear()

    def remove_knob_widget(self):
        selected_items = self.listWidget_knobs.selectedItems()
        for item in selected_items:
            self.listWidget_knobs.takeItem(self.listWidget_knobs.row(item))

    # ------------------------------ EXPRESSION -----------------------------------
    def fill_expression_widget(self):
        node = nuke.selectedNode()
        for knob in self.expression_node_knobs:
            if isinstance(node[knob].value(), str):
                line_edit_widget = self.findChild(QLineEdit, knob)
                line_edit_widget.setText(node[knob].value())

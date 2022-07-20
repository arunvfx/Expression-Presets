# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'expression.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SmartExpressions(object):
    def setupUi(self, SmartExpressions):
        if not SmartExpressions.objectName():
            SmartExpressions.setObjectName(u"SmartExpressions")
        SmartExpressions.resize(1138, 538)
        SmartExpressions.setStyleSheet(u"background-color: #323232;\n"
"color: #cccccc;")
        self.verticalLayout = QVBoxLayout(SmartExpressions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(SmartExpressions)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_left = QFrame(self.frame)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setFrameShape(QFrame.NoFrame)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.frame_radio = QFrame(self.frame_left)
        self.frame_radio.setObjectName(u"frame_radio")
        self.frame_radio.setFrameShape(QFrame.NoFrame)
        self.frame_radio.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_radio)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.radioButton_common = QRadioButton(self.frame_radio)
        self.radioButton_common.setObjectName(u"radioButton_common")
        self.radioButton_common.setMaximumSize(QSize(90, 16777215))
        self.radioButton_common.setFocusPolicy(Qt.ClickFocus)
        self.radioButton_common.setChecked(True)

        self.horizontalLayout_11.addWidget(self.radioButton_common)

        self.radioButton_expression_node = QRadioButton(self.frame_radio)
        self.radioButton_expression_node.setObjectName(u"radioButton_expression_node")
        self.radioButton_expression_node.setMaximumSize(QSize(16777215, 16777215))
        self.radioButton_expression_node.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_11.addWidget(self.radioButton_expression_node)


        self.verticalLayout_5.addWidget(self.frame_radio)

        self.frame_label = QFrame(self.frame_left)
        self.frame_label.setObjectName(u"frame_label")
        self.frame_label.setMaximumSize(QSize(16777215, 35))
        self.frame_label.setFrameShape(QFrame.NoFrame)
        self.frame_label.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_label)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 12)
        self.label_label = QLabel(self.frame_label)
        self.label_label.setObjectName(u"label_label")
        self.label_label.setMinimumSize(QSize(80, 0))
        self.label_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_label)

        self.lineEdit_label = QLineEdit(self.frame_label)
        self.lineEdit_label.setObjectName(u"lineEdit_label")
        self.lineEdit_label.setMinimumSize(QSize(0, 25))
        self.lineEdit_label.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_label.setStyleSheet(u"border: None;\n"
"background-color: #212121;\n"
"border-radius: 5px;")

        self.horizontalLayout_4.addWidget(self.lineEdit_label)

        self.btn_expression_list = QPushButton(self.frame_label)
        self.btn_expression_list.setObjectName(u"btn_expression_list")
        self.btn_expression_list.setMinimumSize(QSize(24, 24))
        self.btn_expression_list.setMaximumSize(QSize(24, 24))
        self.btn_expression_list.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btn_expression_list)


        self.verticalLayout_5.addWidget(self.frame_label)

        self.frame_expression_node = QFrame(self.frame_left)
        self.frame_expression_node.setObjectName(u"frame_expression_node")
        self.frame_expression_node.setMinimumSize(QSize(0, 150))
        self.frame_expression_node.setMaximumSize(QSize(16777215, 300))
        self.frame_expression_node.setStyleSheet(u"border: 1px solid #434343;\n"
"background-color: #434343;\n"
"border-radius: 5px;")
        self.frame_expression_node.setFrameShape(QFrame.NoFrame)
        self.frame_expression_node.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_expression_node)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 12)
        self.frame_temp_expr = QFrame(self.frame_expression_node)
        self.frame_temp_expr.setObjectName(u"frame_temp_expr")
        self.frame_temp_expr.setMaximumSize(QSize(16777215, 140))
        self.frame_temp_expr.setFrameShape(QFrame.NoFrame)
        self.frame_temp_expr.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_temp_expr)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.expr2 = QLineEdit(self.frame_temp_expr)
        self.expr2.setObjectName(u"expr2")
        self.expr2.setMinimumSize(QSize(0, 25))
        self.expr2.setStyleSheet(u"border: None;\n"
"background-color: #212121;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.expr2, 2, 4, 1, 1)

        self.temp_name3 = QLineEdit(self.frame_temp_expr)
        self.temp_name3.setObjectName(u"temp_name3")
        self.temp_name3.setMinimumSize(QSize(0, 25))
        self.temp_name3.setMaximumSize(QSize(100, 16777215))
        self.temp_name3.setStyleSheet(u"border: None;\n"
"background-color: #212121;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.temp_name3, 3, 0, 1, 1)

        self.label_2 = QLabel(self.frame_temp_expr)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame_temp_expr)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)

        self.temp_expr3 = QLineEdit(self.frame_temp_expr)
        self.temp_expr3.setObjectName(u"temp_expr3")
        self.temp_expr3.setMinimumSize(QSize(0, 25))
        self.temp_expr3.setStyleSheet(u"border: None;\n"
"background-color: #212121;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.temp_expr3, 3, 2, 1, 1)

        self.expr1 = QLineEdit(self.frame_temp_expr)
        self.expr1.setObjectName(u"expr1")
        self.expr1.setMinimumSize(QSize(0, 25))
        self.expr1.setStyleSheet(u"border: None;\n"
"background-color: #212121;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.expr1, 1, 4, 1, 1)

        self.expr3 = QLineEdit(self.frame_temp_expr)
        self.expr3.setObjectName(u"expr3")
        self.expr3.setMinimumSize(QSize(0, 25))
        self.expr3.setStyleSheet(u"border: None;\n"
"background-color: #212121;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.expr3, 3, 4, 1, 1)

        self.temp_expr0 = QLineEdit(self.frame_temp_expr)
        self.temp_expr0.setObjectName(u"temp_expr0")
        self.temp_expr0.setMinimumSize(QSize(0, 25))
        self.temp_expr0.setStyleSheet(u"border: None;\n"
"background-color: #212121;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.temp_expr0, 0, 2, 1, 1)

        self.temp_name0 = QLineEdit(self.frame_temp_expr)
        self.temp_name0.setObjectName(u"temp_name0")
        self.temp_name0.setMinimumSize(QSize(0, 25))
        self.temp_name0.setMaximumSize(QSize(100, 16777215))
        self.temp_name0.setStyleSheet(u"border: None;\n"
"background-color: #212121;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.temp_name0, 0, 0, 1, 1)

        self.expr0 = QLineEdit(self.frame_temp_expr)
        self.expr0.setObjectName(u"expr0")
        self.expr0.setMinimumSize(QSize(0, 25))
        self.expr0.setStyleSheet(u"border: None;\n"
"background-color: #212121;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.expr0, 0, 4, 1, 1)

        self.label = QLabel(self.frame_temp_expr)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.temp_expr1 = QLineEdit(self.frame_temp_expr)
        self.temp_expr1.setObjectName(u"temp_expr1")
        self.temp_expr1.setMinimumSize(QSize(0, 25))
        self.temp_expr1.setStyleSheet(u"border: None;\n"
"background-color: #212121;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.temp_expr1, 1, 2, 1, 1)

        self.temp_name2 = QLineEdit(self.frame_temp_expr)
        self.temp_name2.setObjectName(u"temp_name2")
        self.temp_name2.setMinimumSize(QSize(0, 25))
        self.temp_name2.setMaximumSize(QSize(100, 16777215))
        self.temp_name2.setStyleSheet(u"border: None;\n"
"background-color: #212121;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.temp_name2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame_temp_expr)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.temp_name1 = QLineEdit(self.frame_temp_expr)
        self.temp_name1.setObjectName(u"temp_name1")
        self.temp_name1.setMinimumSize(QSize(0, 25))
        self.temp_name1.setMaximumSize(QSize(100, 16777215))
        self.temp_name1.setStyleSheet(u"border: None;\n"
"background-color: #212121;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.temp_name1, 1, 0, 1, 1)

        self.temp_expr2 = QLineEdit(self.frame_temp_expr)
        self.temp_expr2.setObjectName(u"temp_expr2")
        self.temp_expr2.setMinimumSize(QSize(0, 25))
        self.temp_expr2.setStyleSheet(u"border: None;\n"
"background-color: #212121;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.temp_expr2, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_temp_expr)


        self.verticalLayout_5.addWidget(self.frame_expression_node)

        self.frame_expression = QFrame(self.frame_left)
        self.frame_expression.setObjectName(u"frame_expression")
        self.frame_expression.setMaximumSize(QSize(16777215, 100))
        self.frame_expression.setFrameShape(QFrame.NoFrame)
        self.frame_expression.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_expression)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_expression = QLabel(self.frame_expression)
        self.label_expression.setObjectName(u"label_expression")

        self.horizontalLayout.addWidget(self.label_expression)

        self.textEdit_expression = QTextEdit(self.frame_expression)
        self.textEdit_expression.setObjectName(u"textEdit_expression")
        self.textEdit_expression.setStyleSheet(u"background-color: #212121;\n"
"color: #ffffff;\n"
"border-radius: 6px;")
        self.textEdit_expression.setFrameShape(QFrame.NoFrame)
        self.textEdit_expression.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.textEdit_expression)


        self.verticalLayout_5.addWidget(self.frame_expression)

        self.frame_body = QFrame(self.frame_left)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setStyleSheet(u"")
        self.frame_body.setFrameShape(QFrame.NoFrame)
        self.frame_body.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_body)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_body_left = QFrame(self.frame_body)
        self.frame_body_left.setObjectName(u"frame_body_left")
        self.frame_body_left.setFrameShape(QFrame.NoFrame)
        self.frame_body_left.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_body_left)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_knobs = QFrame(self.frame_body_left)
        self.frame_knobs.setObjectName(u"frame_knobs")
        self.frame_knobs.setStyleSheet(u"QFrame{background-color: #434343; border-radius: 5px;}")
        self.frame_knobs.setFrameShape(QFrame.NoFrame)
        self.frame_knobs.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_knobs)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 6, 3, 0)
        self.frame_knob_label = QFrame(self.frame_knobs)
        self.frame_knob_label.setObjectName(u"frame_knob_label")
        self.frame_knob_label.setMinimumSize(QSize(0, 25))
        self.frame_knob_label.setMaximumSize(QSize(16777215, 16777215))
        self.frame_knob_label.setFrameShape(QFrame.NoFrame)
        self.frame_knob_label.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_knob_label)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_knob = QLabel(self.frame_knob_label)
        self.label_knob.setObjectName(u"label_knob")
        self.label_knob.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_knob.setFont(font)
        self.label_knob.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_knob)

        self.btn_add_knob = QToolButton(self.frame_knob_label)
        self.btn_add_knob.setObjectName(u"btn_add_knob")
        self.btn_add_knob.setMinimumSize(QSize(24, 24))
        self.btn_add_knob.setMaximumSize(QSize(24, 24))
        self.btn_add_knob.setStyleSheet(u"QToolButton{\n"
"background-color: #434343;\n"
"border:None;\n"
"}\n"
"QToolButton:pressed{\n"
"background-color: #212121;\n"
"border:None;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QMenu{\n"
"background-color: #212121;\n"
"border:None;\n"
"}")
        self.btn_add_knob.setPopupMode(QToolButton.InstantPopup)

        self.horizontalLayout_5.addWidget(self.btn_add_knob)

        self.btn_remove_knob = QPushButton(self.frame_knob_label)
        self.btn_remove_knob.setObjectName(u"btn_remove_knob")
        self.btn_remove_knob.setMinimumSize(QSize(24, 24))
        self.btn_remove_knob.setMaximumSize(QSize(24, 24))
        self.btn_remove_knob.setStyleSheet(u"QPushButton{\n"
"background-color: #434343;\n"
"}")
        self.btn_remove_knob.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_remove_knob)


        self.verticalLayout_4.addWidget(self.frame_knob_label)

        self.frame_knobs_attr = QFrame(self.frame_knobs)
        self.frame_knobs_attr.setObjectName(u"frame_knobs_attr")
        self.frame_knobs_attr.setMaximumSize(QSize(16777215, 16777215))
        self.frame_knobs_attr.setFrameShape(QFrame.NoFrame)
        self.frame_knobs_attr.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_knobs_attr)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 6)
        self.scrollArea_knobs = QScrollArea(self.frame_knobs_attr)
        self.scrollArea_knobs.setObjectName(u"scrollArea_knobs")
        self.scrollArea_knobs.setFrameShape(QFrame.NoFrame)
        self.scrollArea_knobs.setFrameShadow(QFrame.Plain)
        self.scrollArea_knobs.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 578, 83))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.listWidget_knobs = QListWidget(self.scrollAreaWidgetContents_2)
        self.listWidget_knobs.setObjectName(u"listWidget_knobs")
        self.listWidget_knobs.setFocusPolicy(Qt.ClickFocus)
        self.listWidget_knobs.setStyleSheet(u"QWidget{background-color: #323232; border: None;}")
        self.listWidget_knobs.setFrameShape(QFrame.NoFrame)
        self.listWidget_knobs.setFrameShadow(QFrame.Plain)
        self.listWidget_knobs.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget_knobs.setDragEnabled(True)
        self.listWidget_knobs.setDragDropMode(QAbstractItemView.InternalMove)
        self.listWidget_knobs.setDefaultDropAction(Qt.IgnoreAction)
        self.listWidget_knobs.setAlternatingRowColors(True)
        self.listWidget_knobs.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listWidget_knobs.setItemAlignment(Qt.AlignTop|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.listWidget_knobs)

        self.scrollArea_knobs.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_8.addWidget(self.scrollArea_knobs)


        self.verticalLayout_4.addWidget(self.frame_knobs_attr)


        self.verticalLayout_3.addWidget(self.frame_knobs)


        self.horizontalLayout_2.addWidget(self.frame_body_left)


        self.verticalLayout_5.addWidget(self.frame_body)

        self.frame_save = QFrame(self.frame_left)
        self.frame_save.setObjectName(u"frame_save")
        self.frame_save.setMinimumSize(QSize(0, 0))
        self.frame_save.setMaximumSize(QSize(16777215, 16777215))
        self.frame_save.setFrameShape(QFrame.NoFrame)
        self.frame_save.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_save)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_clear = QPushButton(self.frame_save)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(120, 30))
        self.btn_clear.setMaximumSize(QSize(140, 16777215))
        self.btn_clear.setFocusPolicy(Qt.ClickFocus)
        self.btn_clear.setStyleSheet(u"QPushButton{\n"
"border: 1px solid #212121;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #212121;\n"
"border: 1px solid #212121;\n"
"border-radius: 4px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_clear)

        self.btn_save = QPushButton(self.frame_save)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(120, 30))
        self.btn_save.setMaximumSize(QSize(140, 16777215))
        self.btn_save.setFocusPolicy(Qt.ClickFocus)
        self.btn_save.setStyleSheet(u"QPushButton{\n"
"border: 1px solid #212121;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #212121;\n"
"border: 1px solid #212121;\n"
"border-radius: 4px;\n"
"}")
        self.btn_save.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btn_save)

        self.btn_close = QPushButton(self.frame_save)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(120, 30))
        self.btn_close.setMaximumSize(QSize(140, 16777215))
        self.btn_close.setFocusPolicy(Qt.ClickFocus)
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"border: 1px solid #212121;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #212121;\n"
"border: 1px solid #212121;\n"
"border-radius: 4px;\n"
"}")
        self.btn_close.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.verticalLayout_5.addWidget(self.frame_save)


        self.horizontalLayout_6.addWidget(self.frame_left)

        self.frame_right = QFrame(self.frame)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setMinimumSize(QSize(200, 0))
        self.frame_right.setMaximumSize(QSize(500, 16777215))
        self.frame_right.setStyleSheet(u"QFrame{background-color: #434343; border-radius: 5px;}")
        self.frame_right.setFrameShape(QFrame.NoFrame)
        self.frame_right.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_right)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.frame_expressions_btns = QFrame(self.frame_right)
        self.frame_expressions_btns.setObjectName(u"frame_expressions_btns")
        self.frame_expressions_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_expressions_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_expressions_btns)
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.label_expressions = QLabel(self.frame_expressions_btns)
        self.label_expressions.setObjectName(u"label_expressions")

        self.horizontalLayout_7.addWidget(self.label_expressions)

        self.btn_edit = QPushButton(self.frame_expressions_btns)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setMinimumSize(QSize(24, 24))
        self.btn_edit.setMaximumSize(QSize(24, 24))
        self.btn_edit.setFocusPolicy(Qt.ClickFocus)
        self.btn_edit.setStyleSheet(u"")
        self.btn_edit.setFlat(True)

        self.horizontalLayout_7.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.frame_expressions_btns)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(24, 24))
        self.btn_delete.setMaximumSize(QSize(24, 24))
        self.btn_delete.setFocusPolicy(Qt.ClickFocus)
        self.btn_delete.setStyleSheet(u"")
        self.btn_delete.setFlat(True)

        self.horizontalLayout_7.addWidget(self.btn_delete)


        self.verticalLayout_6.addWidget(self.frame_expressions_btns)

        self.frame_list_expressions = QFrame(self.frame_right)
        self.frame_list_expressions.setObjectName(u"frame_list_expressions")
        self.frame_list_expressions.setMinimumSize(QSize(0, 0))
        self.frame_list_expressions.setFrameShape(QFrame.NoFrame)
        self.frame_list_expressions.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_list_expressions)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 0, 2, 2)
        self.scrollArea_expressions = QScrollArea(self.frame_list_expressions)
        self.scrollArea_expressions.setObjectName(u"scrollArea_expressions")
        self.scrollArea_expressions.setFocusPolicy(Qt.ClickFocus)
        self.scrollArea_expressions.setFrameShape(QFrame.NoFrame)
        self.scrollArea_expressions.setFrameShadow(QFrame.Plain)
        self.scrollArea_expressions.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 492, 465))
        self.horizontalLayout_9 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.listView_expressions = QListView(self.scrollAreaWidgetContents)
        self.listView_expressions.setObjectName(u"listView_expressions")
        self.listView_expressions.setFocusPolicy(Qt.ClickFocus)
        self.listView_expressions.setStyleSheet(u"QListView{background-color: #212121; border: None;}\n"
"QListView:item{height: 25px;}")
        self.listView_expressions.setFrameShape(QFrame.NoFrame)
        self.listView_expressions.setFrameShadow(QFrame.Plain)
        self.listView_expressions.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView_expressions.setDefaultDropAction(Qt.IgnoreAction)
        self.listView_expressions.setAlternatingRowColors(True)
        self.listView_expressions.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_9.addWidget(self.listView_expressions)

        self.scrollArea_expressions.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_10.addWidget(self.scrollArea_expressions)


        self.verticalLayout_6.addWidget(self.frame_list_expressions)


        self.horizontalLayout_6.addWidget(self.frame_right)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(SmartExpressions)

        QMetaObject.connectSlotsByName(SmartExpressions)
    # setupUi

    def retranslateUi(self, SmartExpressions):
        SmartExpressions.setWindowTitle(QCoreApplication.translate("SmartExpressions", u"Expressions", None))
        self.radioButton_common.setText(QCoreApplication.translate("SmartExpressions", u"Common", None))
        self.radioButton_expression_node.setText(QCoreApplication.translate("SmartExpressions", u"Expression Node", None))
        self.label_label.setText(QCoreApplication.translate("SmartExpressions", u"      Label   ", None))
        self.btn_expression_list.setText("")
        self.label_2.setText(QCoreApplication.translate("SmartExpressions", u" = ", None))
        self.label_4.setText(QCoreApplication.translate("SmartExpressions", u" = ", None))
        self.label.setText(QCoreApplication.translate("SmartExpressions", u" = ", None))
        self.label_3.setText(QCoreApplication.translate("SmartExpressions", u" = ", None))
        self.label_expression.setText(QCoreApplication.translate("SmartExpressions", u"Expression ", None))
        self.label_knob.setText(QCoreApplication.translate("SmartExpressions", u"Knobs", None))
        self.btn_add_knob.setText("")
        self.btn_remove_knob.setText("")
        self.btn_clear.setText(QCoreApplication.translate("SmartExpressions", u"     Clear", None))
        self.btn_save.setText(QCoreApplication.translate("SmartExpressions", u"     Save", None))
        self.btn_close.setText(QCoreApplication.translate("SmartExpressions", u"     Close", None))
        self.label_expressions.setText(QCoreApplication.translate("SmartExpressions", u"Expressions", None))
        self.btn_edit.setText("")
        self.btn_delete.setText("")
    # retranslateUi


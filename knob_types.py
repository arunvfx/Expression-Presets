
import os
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class Knobs(QFrame):

    def __init__(self, knob_selected_name):
        super(Knobs, self).__init__()
        self.layout = QHBoxLayout()
        self.label = QLineEdit()
        self.knob_name = QLineEdit()
        self.knob_type = QLabel()
        self.range = QLineEdit()
        self.btn_remove = QPushButton('x')
        self.label.setMaximumWidth(150)
        self.knob_name.setMaximumWidth(150)
        self.range.setMaximumWidth(150)
        self.knob_type.setMinimumWidth(200)

        self.btn_remove.setMinimumSize(24, 24)
        self.btn_remove.setMaximumSize(24, 24)

        self.knob_type.setText(knob_selected_name)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.knob_name)
        self.layout.addWidget(self.knob_type)
        self.layout.addWidget(self.range)
        self.layout.addWidget(self.btn_remove)
        self.setMinimumHeight(50)
        self.knob_type.setAlignment(Qt.AlignCenter)
        self.setStyleSheet('QWidget{background-color: #323232;}')
        self.setLayout(self.layout)

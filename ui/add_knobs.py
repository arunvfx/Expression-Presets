
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class Knobs(QWidget):

    def __init__(self, knob_type_selected, *args, parent=None):
        super(Knobs, self).__init__(parent)
        if args:
            self.args = args[0]
        else:
            self.args = None

        self.layout = QHBoxLayout()
        self.knob_label = QLineEdit()
        self.knob_name = QLineEdit()
        self.knob_type = QLabel()
        self.chkbox_new_line = QCheckBox()
        self.chkbox_new_line.setChecked(True)

        self.knob_label.setFixedWidth(150)
        self.knob_label.setMinimumHeight(24)
        self.knob_name.setFixedWidth(150)
        self.knob_name.setMinimumHeight(24)
        self.knob_type.setMinimumWidth(200)
        self.knob_type.setText(knob_type_selected)

        self.layout.addWidget(self.knob_label)
        self.layout.addWidget(self.knob_name)
        self.layout.addWidget(self.knob_type)
        self.knob_picker(knob_type_selected)
        self.layout.addWidget(self.chkbox_new_line)

        self.knob_type.setAlignment(Qt.AlignCenter)
        self.knob_label.setPlaceholderText('Label')
        self.knob_name.setPlaceholderText('Knob_Name')

        self.setStyleSheet('QLineEdit{background-color: #212121; border:None;'
                           'border-radius: 5px;}'
                           'QTextEdit{background-color: #212121; border:None;'
                           'border-radius: 5px;}'
                           'QLabel{background:None; border: None;}'
                           'QCheckBox{background:None; border: None;}')

        self.setLayout(self.layout)

        if self.args:
            self.knob_label.setText(self.args[0])
            self.knob_name.setText(self.args[1])

    def knob_picker(self, knob_type_selected):
        if self.args:
            self.chkbox_new_line.setChecked(self.args[3])

        if knob_type_selected in ('Floating Point Slider', 'RGB Color Knob',
                                  'RGBA Color Knob'):
            self.frame_range = QLineEdit()
            self.frame_range.setFixedWidth(150)
            self.frame_range.setMinimumHeight(24)
            self.frame_range.setPlaceholderText('Set Range (ex: 0-1)')
            self.layout.addWidget(self.frame_range)
            if self.args:
                self.frame_range.setText(self.args[-1])
            else:
                self.frame_range.setText('0-1')

        elif knob_type_selected in ('2d Position Knob', '3d Position Knob',
                                    'Width/Height Knob', 'UV Coordinate Knob',
                                    'Integer Knob', 'divider', 'Check Box'):
            self.frame_dummy = QFrame()
            self.frame_dummy.setFixedWidth(150)
            self.frame_dummy.setFrameShape(QFrame.NoFrame)
            self.frame_dummy.setFrameShadow(QFrame.Plain)
            self.layout.addWidget(self.frame_dummy)
            self.frame_dummy.setStyleSheet('QFrame{background: None;}')

        elif knob_type_selected in ('Python Script Button', 'Pulldown Choice'):
            self.script = QTextEdit()
            self.script.setStyleSheet('QTextEdit{border: None;}')
            if knob_type_selected == 'Python Script Button':
                self.script.setPlaceholderText('Enter Python Script')
            if knob_type_selected == 'Pulldown Choice':
                self.script.setPlaceholderText('Enter Pulldown Choice Menu')
            self.layout.addWidget(self.script)

            if self.args:
                self.script.setText(self.args[-1])


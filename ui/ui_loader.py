
from PySide2.QtCore import QMetaObject
from PySide2.QtUiTools import QUiLoader


class UiLoader(QUiLoader):

    def __init__(self, base_instance, custom_widget=None):
        QUiLoader.__init__(self, base_instance)
        self.base_instance = base_instance
        self.customWidget = custom_widget

    def createWidget(self, class_name, parent=None, name=''):
        """
        Function that is called for each widget defined in ui file,
        overridden here to populate base_instance instead.
        """

        if parent is None and self.base_instance:
            return self.base_instance

        else:
            if class_name in self.availableWidgets():
                widget = QUiLoader.createWidget(self, class_name, parent, name)
                print('sdfsdf', widget)

            else:
                try:
                    widget = self.custom_widget[class_name](parent)

                except (TypeError, KeyError) as e:
                    raise Exception(
                        'No custom widget ' + class_name + ' found in custom_widget param of UiLoader __init__.')

            if self.base_instance:
                setattr(self.base_instance, name, widget)

            return widget


def load_ui(ui_file, base_instance=None, custom_widget=None, working_directory=None):
    print(base_instance, custom_widget)
    loader = UiLoader(base_instance, custom_widget)
    print(loader)
    if working_directory is not None:
        loader.setWorkingDirectory(working_directory)

    widget = loader.load(ui_file)
    print(widget)
    QMetaObject.connectSlotsByName(widget)
    return widget


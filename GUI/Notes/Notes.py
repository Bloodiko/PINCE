from PyQt6.QtWidgets import QWidget

from .NotesWidget import Ui_widget_Notes


class NotesWidget(QWidget, Ui_widget_Notes):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()

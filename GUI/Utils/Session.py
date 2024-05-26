import enum
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from PyQt6.QtCore import pyqtSignal, QObject

from tr.tr import TranslationConstants as tr
from libpince import typedefs, utils


class DataChanged(enum.Flag):
    NONE = 0
    CHEAT_TABLE = 1
    BOOKMARKS = 2
    NOTES = 4
    ALL = CHEAT_TABLE | BOOKMARKS | NOTES


class Session(QObject):
    """
    Stores the current cheat table and other data.
    """

    file_loaded_signal = pyqtSignal(name="fileLoaded")

    def __init__(self):
        super().__init__()
        self.cheat_table = []
        self.bookmarks = []
        self.notes = ""
        self.version = 1
        self.data_changed = DataChanged.NONE

    def pushButton_Save_clicked(self):
        file_path, _ = QFileDialog.getSaveFileName(self, tr.SAVE_PCT_FILE, None, tr.FILE_TYPES_PCT)
        if not file_path:
            return

        file_path = utils.append_file_extension(file_path, "pct")
        if not utils.save_file(self.get_data(), file_path):
            QMessageBox.information(self, tr.ERROR, tr.FILE_SAVE_ERROR)

    def pushButton_Open_clicked(self):
        file_paths, _ = QFileDialog.getOpenFileNames(self, tr.OPEN_PCT_FILE, None, tr.FILE_TYPES_PCT)
        if not file_paths:
            return
        for file_path in file_paths:
            content = utils.load_file(file_path)
            if content is None:
                QMessageBox.information(None, tr.ERROR, tr.FILE_LOAD_ERROR.format(file_path))
                break

            if type(content) is list:
                # assume old format, only cheat table address list
                self.cheat_table = content
                self.bookmarks = []
                self.notes = ""
            else:
                if "version" in content and content["version"] < self.version:
                    content = self.upgrade(content)
                for key in content:
                    if key in self.__dict__:
                        self.__dict__[key] = content[key]
            self.file_loaded_signal.emit()

    def get_data(self):
        return {"cheat_table": self.cheat_table, "bookmarks": self.bookmarks, "notes": self.notes}

    def upgrade(self, data: dict):
        # not yet needed
        # call the corresponding upgrade function(s) and return the upgraded data
        return data


session = Session()


def reset_session():
    global session
    session = Session()


def get_session():
    return session

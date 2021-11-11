import socket
import sys
import json

from PyQt5.QtWidgets import QFileDialog, QMainWindow
from PyQt5 import QtWidgets
from PyQt5 import uic
from Help import Help
from WFile import WFile
from calculations import get_files_list, get_folders_content, eq_rating, sort_key


class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.folder_path = ''
        self.file_path = ''
        self.search_string = ''
        self.b_file = False
        self.b_dir = False
        self.actionhelp.triggered.connect(self.help_clicked)
        self.btn_add_ip.clicked.connect(self.openFileNameDialog)
        self.btn_directory_dialog.clicked.connect(self.openDirectoryDialog)

    def btn_search_clicked(self):
        search_str = self.textEdit_search.toPlainText()
        if self.b_file:
            one_file = WFile(self.file_path)
            eq_rating([one_file], search_str)
            self.plainTextEdit_result.insertPlainText(f'{one_file.path} - {one_file.eq_rate}\n')
        elif self.b_dir:
            files = get_files_list(get_folders_content(self.folder_path))
            eq_rating(files, search_str)
            result = [[file.path, file.eq_rate] for file in sorted(files, key=sort_key, reverse=True)]
            for file in files:
                self.plainTextEdit_result.insertPlainText(f'{file.path} - {file.eq_rate}\n')

    def help_clicked(self):
        dial = Help(self)
        dial.show()

    def openFileNameDialog(self):
        self.b_file = True
        self.b_dir = False
        self.file_path = QFileDialog.getOpenFileName(self)[0]
        #self.plainTextEdit_result.insertPlainText(self.file_path)

    def openDirectoryDialog(self):
        self.b_file = False
        self.b_dir = True
        self.folder_path = QFileDialog.getExistingDirectory(self)
        #self.plainTextEdit_result.insertPlainText(self.folder_path)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = SearchWindow()
    window.show()
    app.exec()

from PyQt5 import QtWidgets
from PyQt5 import uic


class Help(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent=parent)
        uic.loadUi("helpWindow.ui", self)
        self.textBrowserHelp.setText("""
        Folder path - a string for selecting a folder with documents 
        Search string - search query string
        Work algorithm: 
        1. Enter relative path to folder with documents 
        2. Enter a search query 
        3. Press button
        4. A list of documents relevant to the query will be displayed. 
        """)

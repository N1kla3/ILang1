from PyQt5 import QtWidgets
from PyQt5 import uic


class stat_structure():
    def __init__(self):
        self.first = 0


class Statistics(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent=parent)
        uic.loadUi("helpWindow.ui", self)
        self.textBrowserHelp.setText("""
        STATISTICS
        """)

    def SetMetric(self, metric):
        pass

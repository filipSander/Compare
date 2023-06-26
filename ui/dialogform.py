from PySide6.QtWidgets import QDialog
from ui.base.paramsForm import Ui_Dialog
from .widget import FWidget


class DialogWin(QDialog):
    
    def __init__(self):
        super(DialogWin, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.counter_id: int = 0
        self.files = []

    def addFile(self, fileName, rows):
        file_row = FWidget(fileName, self.counter_id)
        file_row.addRows(rows)
        self.ui.verticalLayout_3.addWidget(file_row)
        self.files.append(file_row)
        self.counter_id += 1

    def Clear(self):
        self.files = []
        while self.ui.verticalLayout_3.count() > 0:
            item = self.ui.verticalLayout_3.takeAt(0)
            item.widget().deleteLater()
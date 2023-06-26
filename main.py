import os
from PySide6.QtWidgets import QApplication
from ui.base.mainForm import showDialog
from ui.mainform import MainWindow
from ui.dialogform import DialogWin

import sys
app = QApplication()

Dialog = DialogWin()
MainWindow = MainWindow()

MainWindow.ui.btn_start.clicked.connect(lambda: test(MainWindow.ui.label.files))
MainWindow.ui.btn_settings.clicked.connect(lambda: test(MainWindow.ui.label.files))
Dialog.ui.buttonBox.rejected.connect(lambda: accept(1))
Dialog.ui.buttonBox.accepted.connect(lambda: accept(1))
Dialog.closeEvent = lambda event: accept(event)

t = [
    ['74AUP1T34GM',  'Nexperia',	'248',	'$0,12', 	'NXP',	'13+',	'XSON6',	'248pcs in stock'],
    ['74AUP1T34GM',  'Nexperia',	'248',	'$0,12', 	'NXP',	'13+',	'XSON6',	'248pcs in stock'],
    ['74AUP1T34GM',  'Nexperia',	'248',	'$0,12', 	'NXP',	'13+',	'XSON6',	'248pcs in stock'],
]

def test(files):
    length = len(files)
    if length == 0:
        showDialog("Файлы для сравнения не выбранны или не соответствуют типу xls, вернитьсь к главному окну и выберите их.")   
        return
    if length != len(Dialog.files):
        Dialog.Clear()
        for f in files:
            Dialog.addFile(os.path.basename(f), t)
    MainWindow.hide()
    Dialog.show()

def accept(event):
    MainWindow.show()

if __name__ == "__main__":
    MainWindow.show()
    sys.exit(app.exec())



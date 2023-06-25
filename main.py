import os
from PyQt5 import QtWidgets

from desing import Ui_MainWindow, showDialog

def test(files):
    if len(files) == 0:
        showDialog("Файлы для сравнения не выбранны или не соответствуют типу xls, вернитьсь к главному окну и выберите их.")
        return
    print("asdasd")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_start.clicked.connect(lambda: test(ui.label.files))
    MainWindow.show()
    sys.exit(app.exec_())



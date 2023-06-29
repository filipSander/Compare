import os
from PySide6.QtWidgets import QApplication
from func import checkFileStructure, compare, writeFile
from ui.base.mainForm import showDialog
from ui.mainform import MainWindow
from ui.dialogform import DialogWin
import sys



app = QApplication()
Dialog = DialogWin()
MainWindow = MainWindow()

MainWindow.ui.btn_start.clicked.connect(lambda: test(MainWindow.ui.label.files, True))
MainWindow.ui.btn_settings.clicked.connect(lambda: test(MainWindow.ui.label.files, False))
Dialog.ui.buttonBox.rejected.connect(lambda: accept(1))
Dialog.ui.buttonBox.accepted.connect(lambda: accept(1))
Dialog.closeEvent = lambda event: accept(event)



def test(files, senderButIsStart):
    length = len(files)
    if length == 0:
        showDialog("Файлы для сравнения не выбранны или не соответствуют типу xls, вернитьсь к главному окну и выберите их.")   
        return
   
    if length != len(Dialog.files):
        Dialog.Clear()
        for path in files:
            Dialog.addFile(os.path.basename(path), checkFileStructure(path))
    
    if fileParamsNotSelected() and senderButIsStart:
        showDialog("Параметры файла(ов) не заданны.")   
        MainWindow.hide()
        Dialog.show()
    elif senderButIsStart:
        data = compare(files, Dialog.files)
        if len(data) < 2:
            showDialog("Параметры файла(ов) заданны неправильно.")
            return
        try:
            writeFile(data) 
            showDialog("Готово!")  
        except Exception as ex:
             showDialog("При записи файла произошла ошибка. Не открывайте файлы exel во время работы программы. Описание ошибки" + str(ex)) 
        
    if not senderButIsStart:
        MainWindow.hide()
        Dialog.show()

def fileParamsNotSelected():
    for file in Dialog.files:
        if file.name == -1 or file.price == -1:
            return True
    return False

def accept(event):
    MainWindow.show()

if __name__ == "__main__":
    MainWindow.show()
    sys.exit(app.exec())
import os
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        MainWindow.setMaximumSize(QtCore.QSize(400, 500))
        MainWindow.setStyleSheet("""
        QWidget{
			color: white;
			background-color: #121212;
			font-family: Rubik;
			border-radius: 6px;
			position: absolute;
		}
        """)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(80, 420, 241, 51))
        self.btn_start.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_start.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(16)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet("""
        QPushButton{
			left: calc(50% - 30px);
			background-color: transparent;
			border-radius: 6px;

		}
		QPushButton:hover{
			background-color: #666;
		}
		QPushButton:pressed{
			background-color: #888;
		}
        """)
        self.btn_start.setFlat(True)
        self.btn_start.setObjectName("btn_start")
        self.label = lableWidget("label",self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 100, 300, 280))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("centralwidget")
        self.label.setStyleSheet("""
        QLabel{
                border-radius: 12px;
                border: 2px dashed  white;
        }
        """)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "cmp"))
        self.btn_start.setText(_translate("MainWindow", "Выполнить сравнение"))
        self.btn_start.setShortcut(_translate("MainWindow", "Return"))
        self.label.setText(_translate("MainWindow", "Перетащите файлы или \n" + "  папку сюда.."))

class lableWidget(QtWidgets.QLabel):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setAcceptDrops(True)
        self.files = []

    def dropEvent(self, event) -> None:
        if event.mimeData().hasUrls():
            for f in event.mimeData().urls():
                try:
                    os.listdir(f.toLocalFile())
                except Exception as ex:
                    print(ex)

                self.addfile(f.toLocalFile())

    def addfile(self, path):
        if not path in self.files:
            self.files.append(path)
            str = ''
            for s in self.files:
                str += os.path.basename(s) + '\n';
            self.setText(str)


    def dragEnterEvent(self, event) -> None:
        if event.mimeData().hasUrls():
            event.accept()
            self.files = []
        else:
            event.ignore()
    
    def dragMoveEvent(self, event) -> None:
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
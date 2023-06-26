
import os
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QMessageBox, QLabel, QPushButton,
    QWidget)

def showDialog(msg):
    msgBox = QMessageBox()
    msgBox.setText(msg)
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setStyleSheet("""
    QMessageBox{
        color: white;
        background-color: #121212;
        font-family: Rubik;
        border-radius: 6px;
    }
    QLabel{
        color: white;
        font-family: Rubik;
    }
    QPushButton{
        color: white;
        width: 60px;
        height: 30px;
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
    msgBox.setWindowTitle("Внимание")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.show()
    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('OK clicked')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QSize(400, 500))
        MainWindow.setMaximumSize(QSize(400, 500))
        MainWindow.setStyleSheet(u"QWidget{\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	border-radius: 6px;\n"
"	position: absolute;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(80, 420, 241, 51))
        self.btn_start.setMinimumSize(QSize(0, 0))
        self.btn_start.setMaximumSize(QSize(300, 100))
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(16)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet(u"\n"
"QPushButton{\n"
"    left: calc(50% - 30px);\n"
"	background-color: transparent;\n"
"	border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #888;\n"
"}")
        self.btn_start.setFlat(True)

        self.btn_settings = QPushButton(self.centralwidget)
        self.btn_settings.setObjectName(u"btn_start")
        self.btn_settings.setGeometry(QRect(130, 20, 241, 51))
        self.btn_settings.setMinimumSize(QSize(0, 0))
        self.btn_settings.setMaximumSize(QSize(150, 100))
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(16)
        self.btn_settings.setFont(font)
        self.btn_settings.setStyleSheet(u"\n"
"QPushButton{\n"
"    left: calc(50% - 30px);\n"
"	background-color: transparent;\n"
"	border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #888;\n"
"}")
        self.btn_settings.setFlat(True)
        self.label = lableWidget("label",self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 100, 301, 281))
        font1 = QFont()
        font1.setFamilies([u"Rubik"])
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"        QLabel{\n"
"                border-radius: 12px;\n"
"                border: 2px dashed  white;\n"
"        }")
        self.label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"cmp", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Параметры", None))
#if QT_CONFIG(shortcut)
#if QT_CONFIG(shortcut)
        self.btn_start.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0442\u0430\u0449\u0438\u0442\u0435 \u0444\u0430\u0439\u043b\u044b \u0438\u043b\u0438 \n"
"  \u043f\u0430\u043f\u043a\u0443 \u0441\u044e\u0434\u0430..", None))
    # retranslateUi

class lableWidget(QLabel):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setAcceptDrops(True)
        self.files = []

    def dropEvent(self, event) -> None:
        if event.mimeData().hasUrls():
            for f in event.mimeData().urls():
                try:
                    for file in os.listdir(f.toLocalFile()):
                        self.addfile(f.toLocalFile() + "/" + file)
                except Exception as ex:
                    self.addfile(f.toLocalFile())
      

    def addfile(self, path):
        fileName, fileExt = os.path.splitext(path)
        if not path in self.files and fileExt == '.xls':
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

    


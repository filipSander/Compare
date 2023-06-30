from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    Qt)
from PySide6.QtWidgets import (QDialogButtonBox,
    QScrollArea, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 600)
        Dialog.setStyleSheet(u"    QDialog{\n"
"        color: white;\n"
"        background-color: #121212;\n"
"        font-family: Rubik;\n"
"        border-radius: 6px;\n"
"    }\n"
"\n"
"    QLabel{\n"
"        color: white;\n"
"        font-family: Rubik;\n"
"    }\n"
"    QPushButton{\n"
"        color: white;\n"
"        width: 60px;\n"
"        height: 30px;\n"
"        background-color: transparent;\n"
"        border-radius: 6px;\n"
"    }\n"
"    QPushButton:hover{\n"
"        background-color: #666;\n"
"    }\n"
"    QPushButton:pressed{\n"
"        background-color: #888;\n"
"    }")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"        background: #121212;\n"
" }\n"
"QWidget{\n"
"        background: #121212;\n"
" }\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 751, 451))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Выберите параметры | Зеленный - название, красный - цена", None))
    # retranslateUi


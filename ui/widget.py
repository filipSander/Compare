from PySide6.QtWidgets import (QWidget, QPushButton)
from ui.base.fileWidget import Ui_Form


class FWidget(QWidget):

    def __init__(self, title: str, id_widget: int, parent=None):
        super(FWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.groupBox.setTitle(title)
        self.ui.groupBox.setStyleSheet("""
        QGroupBox{
            border: 1px solid rgba(255, 255, 255, 0.1);;
        }
        """)
        self.buttons = []
        self.name = -1
        self.price = -1

    def addRows(self, rows):
        for i in range(0, len(rows)):
            for j in range(0, len(rows[i])):
                btn = Button(rows[i][j], j)     
                btn.setObjectName(f'{j}')          
                btn.clicked.connect(self.ceilClick)
                self.ui.layout.addWidget(btn, i, j)    
                self.buttons.append(btn)  

    def ceilClick(self):
        sending_button = self.sender()
        id = int(sending_button.objectName())

        if self.name < 0 and id != self.price:
            for b in self.buttons:
                if b.rows ==  id:
                    b.setStyleSheet("""
                    QPushButton{
                        background-color: rgba(7, 105, 12, 0.3);
                        border-radius: 6px;
                    }
                    """)  
            self.name = id
            return

        if self.price < 0 and id != self.name:
            for b in self.buttons:
                if b.rows == id:
                    b.setStyleSheet("""
                    QPushButton{
                        background-color: rgba(105, 7, 20, 0.3);
                        border-radius: 6px;
                    }
                    """)  
            self.price = id
            return
        
        for b in self.buttons:
            self.name = -1
            self.price = -1
            b.setStyleSheet("""
            QPushButton{
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

class Button(QPushButton):
   def __init__(self, text, row):                 
        super(Button, self).__init__()
        self.rows = row
        self.setText(text)                          
        
        self.setStyleSheet("""
        QPushButton{
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
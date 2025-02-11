# ch 6.2.1 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, 
                             QComboBox)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore # 모듈 추가가

class View(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)
        
        self.btn1 = QPushButton('Message', self)
        self.btn2 = QPushButton('Clear', self)
        
        self.le1=QLineEdit('0',self) # 라인 에디트1 추가
        self.le1.setAlignment(QtCore.Qt.AlignRight) # 라인 에디트1 문자열 배치 설정
        
        self.le2=QLineEdit('0',self) # 라인 에디트2 추가
        self.le2.setAlignment(QtCore.Qt.AlignRight) # 라인 에디트2 문자열 배치 설정
        
        self.cb = QComboBox(self) # 콤보 박스 추가
        self.cb.addItems(['+', '-', '*', '/']) # 콤보 박스 항목 추가(연산자로 사용)
        
        hbox_formular = QHBoxLayout() # 새로 정의한 위벳을 QHBoxLayout에 위치
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular) # hbox_formular 배치치
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()
        
    def activateMessage(self):
        self.te1.appendPlainText("Button clicked!")
        
    def clearMessage(self):
        self.te1.clear()
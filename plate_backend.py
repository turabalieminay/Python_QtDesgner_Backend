from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1450, 800)
        Form.setMaximumSize(QtCore.QSize(1920, 1080))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QWidget {\n"
"    background: qradialgradient(\n"
"        cx: 0.5, cy: 0.5, radius: 1,\n"
"        fx: 0.5, fy: 0.5,\n"
"        stop: 0 #4682B4, /* Ortada koyu mavi (SteelBlue) */\n"
"        stop: 0.3 #4169E1, /* Daha koyu mavi (Royal Blue) */\n"
"        stop: 0.6 #6A0DAD, /* Koyu mor */\n"
"        stop: 1 #4B0082 /* Dış kenarlarda çok koyu mor (İndigo) */\n"
"    );\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 100, 611, 631))
        self.label.setStyleSheet("QLabel {\n"
"    background-color: #f0f0f0; /* Arka plan rengi */\n"
"    border: 2px solid #555;    /* Kenarlık kalınlığı ve rengi */\n"
"    color: #333;               /* Metin rengi */\n"
"    font-size: 16px;           /* Metin boyutu */\n"
"    padding: 10px;             /* İç boşluk */\n"
"}\n"
"")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(1270, 100, 161, 521))
        self.tableWidget.setMaximumSize(QtCore.QSize(161, 16777215))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    background-color: #ffffff; /* Beyaz arka plan */\n"
"    gridline-color: #dcdcdc; /* Izgara çizgileri */\n"
"    border: 1px solid #dcdcdc;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f0f0f0; /* Başlık arka planı */\n"
"    padding: 4px;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"}\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 247, 28))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(159)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(640, 100, 611, 631))
        self.label_2.setStyleSheet("QLabel {\n"
"    background-color: #f0f0f0; /* Arka plan rengi */\n"
"    border: 2px solid #555;    /* Kenarlık kalınlığı ve rengi */\n"
"    color: #333;               /* Metin rengi */\n"
"    font-size: 16px;           /* Metin boyutu */\n"
"    padding: 10px;             /* İç boşluk */\n"
"}\n"
"")
        self.label_2.setText("")
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1280, 690, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(-1)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #F44336; /* Yeşil renk */\n"
"    color: white;\n"
"    border: 1px solid #4CAF50;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E53935; /* Hover rengi */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D32F2F; /* Basılı rengi */\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1280, 640, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(-1)
        font.setItalic(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50; /* Yeşil renk */\n"
"    color: white;\n"
"    border: 1px solid #4CAF50;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Hover rengi */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #388E3C; /* Basılı rengi */\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(530, 20, 361, 61))
        self.label_3.setStyleSheet("QLabel {\n"
"    font: bold 28px Arial; /* Kalın ve büyük yazı tipi */\n"
"    color: rgba(255, 255, 255, 0.8); /* Hafif şeffaf beyaz metin */\n"
"    text-align: center; /* Metin ortalama */\n"
"    border: 1px solid #ffffff; /* Beyaz kenarlık */\n"
"    border-radius: 0px; /* Köşe yuvarlaklığı */\n"
"    padding: 10px; /* İç kenar boşluğu */\n"
"    background-color: rgba(0, 0, 0, 0.2); /* Hafif şeffaf arka plan */\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "PLAKA    "))
        self.pushButton_2.setText(_translate("Form", "DURDUR"))
        self.pushButton_3.setText(_translate("Form", "BAŞLAT"))
        self.label_3.setText(_translate("Form", "PLAKA TANIMA SİSTEMİ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


















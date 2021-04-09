# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChainReactiontest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 421)
        MainWindow.setStyleSheet("color:rgb(255, 255, 255);\n"
                                 "background-color:gray;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 50, 351, 346))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cellButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)


        self.cellButton_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../figures/draw-green-rectangle.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cellButton_1.setIcon(icon)
        self.cellButton_1.setIconSize(QtCore.QSize(100, 100))
        self.cellButton_1.setObjectName("cellButton_1")
        self.cellButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cellButton_8.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../figures/draw-blue-rectangle.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cellButton_8.setIcon(icon1)
        self.cellButton_8.setIconSize(QtCore.QSize(100, 100))
        self.cellButton_8.setObjectName("cellButton_8")
        self.cellButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cellButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../figures/draw-blue-circle.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cellButton_2.setIcon(icon2)
        self.cellButton_2.setIconSize(QtCore.QSize(100, 100))
        self.cellButton_2.setObjectName("cellButton_2")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cellButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cellButton_9.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../figures/draw-orange-circle.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cellButton_9.setIcon(icon3)
        self.cellButton_9.setIconSize(QtCore.QSize(100, 100))
        self.cellButton_9.setObjectName("cellButton_9")
        self.cellButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cellButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../figures/draw-orange-rectangle.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cellButton_4.setIcon(icon4)
        self.cellButton_4.setIconSize(QtCore.QSize(100, 100))
        self.cellButton_4.setObjectName("cellButton_4")
       
        self.cellButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cellButton_6.setText("")
        self.cellButton_6.setIcon(icon3)
        self.cellButton_6.setIconSize(QtCore.QSize(100, 100))
        self.cellButton_6.setObjectName("cellButton_6")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.cellButton_3 = QtWidgets.QPushButton("3",self.gridLayoutWidget)
        
        self.cellButton_3.setWindowIconText("123124")
        self.cellButton_3.setIcon(icon4)
        self.cellButton_3.setIconSize(QtCore.QSize(100, 100))
        self.cellButton_3.setObjectName("cellButton_3")
        self.cellButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cellButton_5.setText("")
        self.cellButton_5.setIcon(icon2)
        self.cellButton_5.setIconSize(QtCore.QSize(100, 100))
        self.cellButton_5.setObjectName("cellButton_5")
        self.cellButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cellButton_7.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../figures/draw-green-circle.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cellButton_7.setIcon(icon5)
        self.cellButton_7.setIconSize(QtCore.QSize(100, 100))
        self.cellButton_7.setObjectName("cellButton_7")
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.restartButton = QtWidgets.QPushButton(self.centralwidget)
        self.restartButton.setGeometry(QtCore.QRect(0, 10, 101, 31))
        self.restartButton.setObjectName("restartButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(300, 20, 81, 23))
        self.nextButton.setObjectName("nextButton")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(220, 20, 81, 23))
        self.prevButton.setObjectName("prevButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 0, 51, 21))
        self.label.setObjectName("label")
        self.levelLabel = QtWidgets.QLabel(self.centralwidget)
        self.levelLabel.setGeometry(QtCore.QRect(270, 0, 47, 21))
        self.levelLabel.setObjectName("levelLabel")
        self.successMoveLabel = QtWidgets.QLabel(self.centralwidget)
        self.successMoveLabel.setGeometry(QtCore.QRect(130, 20, 91, 20))
        self.successMoveLabel.setText("")
        self.successMoveLabel.setObjectName("successMoveLabel")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(110, 20, 47, 13))
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)

        self.horizontalLayout_3.addWidget(self.cellButton_1)
        self.horizontalLayout_3.addWidget(self.cellButton_2)
        self.horizontalLayout_3.addWidget(self.cellButton_3)
        self.horizontalLayout_2.addWidget(self.cellButton_4)
        self.horizontalLayout_2.addWidget(self.cellButton_5)
        self.horizontalLayout_2.addWidget(self.cellButton_6)
        self.horizontalLayout_1.addWidget(self.cellButton_7)
        self.horizontalLayout_1.addWidget(self.cellButton_8)
        self.horizontalLayout_1.addWidget(self.cellButton_9)

        self.set_minimum_font()
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # используется текст с мин размером шрифта для работы с sender меньше функций будет
    # графический текст нам не нужен
    def set_minimum_font(self):
        self.cellButton_1.setStyleSheet("color:gray;")
        self.cellButton_1.setText("00")
        self.cellButton_1.setFont(QtGui.QFont("MS Shell Dlg 2", 1))

        self.cellButton_2.setStyleSheet("color:gray;")
        self.cellButton_2.setText("01")
        self.cellButton_2.setFont(QtGui.QFont("MS Shell Dlg 2", 1))

        self.cellButton_3.setStyleSheet("color:gray;")
        self.cellButton_3.setText("02")
        self.cellButton_3.setFont(QtGui.QFont("MS Shell Dlg 2", 1))

        self.cellButton_4.setStyleSheet("color:gray;")
        self.cellButton_4.setText("10")
        self.cellButton_4.setFont(QtGui.QFont("MS Shell Dlg 2", 1))

        self.cellButton_5.setStyleSheet("color:gray;")
        self.cellButton_5.setText("11")
        self.cellButton_5.setFont(QtGui.QFont("MS Shell Dlg 2", 1))

        self.cellButton_6.setStyleSheet("color:gray;")
        self.cellButton_6.setText("12")
        self.cellButton_6.setFont(QtGui.QFont("MS Shell Dlg 2", 1))

        self.cellButton_7.setStyleSheet("color:gray;")
        self.cellButton_7.setText("20")
        self.cellButton_7.setFont(QtGui.QFont("MS Shell Dlg 2", 1))

        self.cellButton_8.setStyleSheet("color:gray;")
        self.cellButton_8.setText("21")
        self.cellButton_8.setFont(QtGui.QFont("MS Shell Dlg 2", 1))

        self.cellButton_9.setStyleSheet("color:gray;")
        self.cellButton_9.setText("22")
        self.cellButton_9.setFont(QtGui.QFont("MS Shell Dlg 2", 1))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.restartButton.setText(_translate("MainWindow", "Перезапустить"))
        self.nextButton.setText(_translate("MainWindow", "Следующий"))
        self.prevButton.setText(_translate("MainWindow", "Предыдущий"))
        self.label.setText(_translate("MainWindow", "Уровень:"))
        self.levelLabel.setText(_translate("MainWindow", "1"))
        self.label_12.setText(_translate("MainWindow", "Ход:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

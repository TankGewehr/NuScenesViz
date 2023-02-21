# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NuScenes-Viz.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.setEnabled(True)
        form.resize(1923, 1010)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form.sizePolicy().hasHeightForWidth())
        form.setSizePolicy(sizePolicy)
        form.setStyleSheet("background-color: rgb(145, 145, 145);\n"
"")
        self.widget = QtWidgets.QWidget(form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1921, 1011))
        self.widget.setObjectName("widget")
        self.all_layout = QtWidgets.QVBoxLayout(self.widget)
        self.all_layout.setContentsMargins(0, 0, 0, 0)
        self.all_layout.setSpacing(0)
        self.all_layout.setObjectName("all_layout")
        self.label_layout_1 = QtWidgets.QHBoxLayout()
        self.label_layout_1.setSpacing(0)
        self.label_layout_1.setObjectName("label_layout_1")
        self.left_front_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_front_label.sizePolicy().hasHeightForWidth())
        self.left_front_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.left_front_label.setFont(font)
        self.left_front_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.left_front_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.left_front_label.setLineWidth(1)
        self.left_front_label.setAlignment(QtCore.Qt.AlignCenter)
        self.left_front_label.setObjectName("left_front_label")
        self.label_layout_1.addWidget(self.left_front_label)
        self.front_center_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.front_center_label.sizePolicy().hasHeightForWidth())
        self.front_center_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.front_center_label.setFont(font)
        self.front_center_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.front_center_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.front_center_label.setLineWidth(1)
        self.front_center_label.setAlignment(QtCore.Qt.AlignCenter)
        self.front_center_label.setObjectName("front_center_label")
        self.label_layout_1.addWidget(self.front_center_label)
        self.right_front_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_front_label.sizePolicy().hasHeightForWidth())
        self.right_front_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.right_front_label.setFont(font)
        self.right_front_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.right_front_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.right_front_label.setLineWidth(1)
        self.right_front_label.setAlignment(QtCore.Qt.AlignCenter)
        self.right_front_label.setObjectName("right_front_label")
        self.label_layout_1.addWidget(self.right_front_label)
        self.label_layout_1.setStretch(0, 1)
        self.label_layout_1.setStretch(1, 1)
        self.label_layout_1.setStretch(2, 1)
        self.all_layout.addLayout(self.label_layout_1)
        self.label_layout_2 = QtWidgets.QHBoxLayout()
        self.label_layout_2.setSpacing(0)
        self.label_layout_2.setObjectName("label_layout_2")
        self.left_back_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_back_label.sizePolicy().hasHeightForWidth())
        self.left_back_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.left_back_label.setFont(font)
        self.left_back_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.left_back_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.left_back_label.setLineWidth(1)
        self.left_back_label.setAlignment(QtCore.Qt.AlignCenter)
        self.left_back_label.setObjectName("left_back_label")
        self.label_layout_2.addWidget(self.left_back_label)
        self.back_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_label.sizePolicy().hasHeightForWidth())
        self.back_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.back_label.setFont(font)
        self.back_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.back_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.back_label.setLineWidth(1)
        self.back_label.setAlignment(QtCore.Qt.AlignCenter)
        self.back_label.setObjectName("back_label")
        self.label_layout_2.addWidget(self.back_label)
        self.right_back_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_back_label.sizePolicy().hasHeightForWidth())
        self.right_back_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.right_back_label.setFont(font)
        self.right_back_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.right_back_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.right_back_label.setLineWidth(1)
        self.right_back_label.setAlignment(QtCore.Qt.AlignCenter)
        self.right_back_label.setObjectName("right_back_label")
        self.label_layout_2.addWidget(self.right_back_label)
        self.label_layout_2.setStretch(0, 1)
        self.label_layout_2.setStretch(1, 1)
        self.label_layout_2.setStretch(2, 1)
        self.all_layout.addLayout(self.label_layout_2)
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.button_layout.setContentsMargins(80, 5, 80, 5)
        self.button_layout.setSpacing(80)
        self.button_layout.setObjectName("button_layout")
        self.load_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_button.sizePolicy().hasHeightForWidth())
        self.load_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.load_button.setFont(font)
        self.load_button.setMouseTracking(False)
        self.load_button.setStyleSheet("border-style:none;\n"
"border:1px solid #C0DCF2;\n"
"color:#386487;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);")
        self.load_button.setObjectName("load_button")
        self.button_layout.addWidget(self.load_button)
        self.rand_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rand_button.sizePolicy().hasHeightForWidth())
        self.rand_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rand_button.setFont(font)
        self.rand_button.setMouseTracking(False)
        self.rand_button.setStyleSheet("border-style:none;\n"
"border:1px solid #C0DCF2;\n"
"color:#386487;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);")
        self.rand_button.setObjectName("rand_button")
        self.button_layout.addWidget(self.rand_button)
        self.prev_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_button.sizePolicy().hasHeightForWidth())
        self.prev_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.prev_button.setFont(font)
        self.prev_button.setMouseTracking(False)
        self.prev_button.setStyleSheet("border-style:none;\n"
"border:1px solid #C0DCF2;\n"
"color:#386487;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);")
        self.prev_button.setObjectName("prev_button")
        self.button_layout.addWidget(self.prev_button)
        self.next_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.next_button.setFont(font)
        self.next_button.setMouseTracking(False)
        self.next_button.setStyleSheet("border-style:none;\n"
"border:1px solid #C0DCF2;\n"
"color:#386487;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);")
        self.next_button.setObjectName("next_button")
        self.button_layout.addWidget(self.next_button)
        self.lidar_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lidar_button.sizePolicy().hasHeightForWidth())
        self.lidar_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lidar_button.setFont(font)
        self.lidar_button.setMouseTracking(False)
        self.lidar_button.setStyleSheet("border-style:none;\n"
"border:1px solid #C0DCF2;\n"
"color:#386487;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);")
        self.lidar_button.setObjectName("lidar_button")
        self.button_layout.addWidget(self.lidar_button)
        self.exit_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setMouseTracking(False)
        self.exit_button.setStyleSheet("border-style:none;\n"
"border:1px solid #C0DCF2;\n"
"color:#386487;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);")
        self.exit_button.setObjectName("exit_button")
        self.button_layout.addWidget(self.exit_button)
        self.button_layout.setStretch(0, 1)
        self.button_layout.setStretch(1, 1)
        self.button_layout.setStretch(2, 1)
        self.button_layout.setStretch(3, 1)
        self.button_layout.setStretch(4, 1)
        self.button_layout.setStretch(5, 1)
        self.all_layout.addLayout(self.button_layout)
        self.all_layout.setStretch(0, 10)
        self.all_layout.setStretch(1, 10)
        self.all_layout.setStretch(2, 1)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "NuScenes-Viz"))
        self.left_front_label.setText(_translate("form", "Left Front"))
        self.front_center_label.setText(_translate("form", "Front Center"))
        self.right_front_label.setText(_translate("form", "Right Front"))
        self.left_back_label.setText(_translate("form", "Left Back"))
        self.back_label.setText(_translate("form", "Back & Lidar"))
        self.right_back_label.setText(_translate("form", "Right Back"))

        self.load_button.setText(_translate("form", "Load"))
        self.rand_button.setText(_translate("form", "Rand"))
        self.prev_button.setText(_translate("form", "Prev"))
        self.next_button.setText(_translate("form", "Next"))
        self.lidar_button.setText(_translate("form", "Lidar"))
        self.exit_button.setText(_translate("form", "Clear and Exit"))


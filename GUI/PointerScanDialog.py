# Form implementation generated from reading ui file 'PointerScanDialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(386, 390)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_Address = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_Address.setObjectName("lineEdit_Address")
        self.horizontalLayout.addWidget(self.lineEdit_Address)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox_Depth = QtWidgets.QSpinBox(parent=Dialog)
        self.spinBox_Depth.setMinimum(1)
        self.spinBox_Depth.setProperty("value", 3)
        self.spinBox_Depth.setObjectName("spinBox_Depth")
        self.horizontalLayout.addWidget(self.spinBox_Depth)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinBox_ScanRangeStart = QtWidgets.QSpinBox(parent=Dialog)
        self.spinBox_ScanRangeStart.setMaximum(16777215)
        self.spinBox_ScanRangeStart.setDisplayIntegerBase(16)
        self.spinBox_ScanRangeStart.setObjectName("spinBox_ScanRangeStart")
        self.horizontalLayout_2.addWidget(self.spinBox_ScanRangeStart)
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.spinBox_ScanRangeEnd = QtWidgets.QSpinBox(parent=Dialog)
        self.spinBox_ScanRangeEnd.setSuffix("")
        self.spinBox_ScanRangeEnd.setMaximum(16777215)
        self.spinBox_ScanRangeEnd.setProperty("value", 1000)
        self.spinBox_ScanRangeEnd.setDisplayIntegerBase(16)
        self.spinBox_ScanRangeEnd.setObjectName("spinBox_ScanRangeEnd")
        self.horizontalLayout_2.addWidget(self.spinBox_ScanRangeEnd)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_Path = QtWidgets.QCheckBox(parent=Dialog)
        self.checkBox_Path.setObjectName("checkBox_Path")
        self.horizontalLayout_7.addWidget(self.checkBox_Path)
        self.lineEdit_Path = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_Path.setEnabled(True)
        self.lineEdit_Path.setText("")
        self.lineEdit_Path.setDragEnabled(False)
        self.lineEdit_Path.setReadOnly(True)
        self.lineEdit_Path.setClearButtonEnabled(False)
        self.lineEdit_Path.setObjectName("lineEdit_Path")
        self.horizontalLayout_7.addWidget(self.lineEdit_Path)
        self.pushButton_PathBrowse = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_PathBrowse.setEnabled(False)
        self.pushButton_PathBrowse.setObjectName("pushButton_PathBrowse")
        self.horizontalLayout_7.addWidget(self.pushButton_PathBrowse)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(parent=Dialog)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.spinBox_ScanLRangeStart = QtWidgets.QSpinBox(parent=Dialog)
        self.spinBox_ScanLRangeStart.setMaximum(16777215)
        self.spinBox_ScanLRangeStart.setProperty("value", 0)
        self.spinBox_ScanLRangeStart.setDisplayIntegerBase(16)
        self.spinBox_ScanLRangeStart.setObjectName("spinBox_ScanLRangeStart")
        self.horizontalLayout_3.addWidget(self.spinBox_ScanLRangeStart)
        self.label_9 = QtWidgets.QLabel(parent=Dialog)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.spinBox_ScanLRangeEnd = QtWidgets.QSpinBox(parent=Dialog)
        self.spinBox_ScanLRangeEnd.setMaximum(16777215)
        self.spinBox_ScanLRangeEnd.setProperty("value", 0)
        self.spinBox_ScanLRangeEnd.setDisplayIntegerBase(16)
        self.spinBox_ScanLRangeEnd.setObjectName("spinBox_ScanLRangeEnd")
        self.horizontalLayout_3.addWidget(self.spinBox_ScanLRangeEnd)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.spinBox_Node = QtWidgets.QSpinBox(parent=Dialog)
        self.spinBox_Node.setMinimum(0)
        self.spinBox_Node.setProperty("value", 0)
        self.spinBox_Node.setObjectName("spinBox_Node")
        self.horizontalLayout_4.addWidget(self.spinBox_Node)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.lineEdit_Last = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_Last.setObjectName("lineEdit_Last")
        self.horizontalLayout_5.addWidget(self.lineEdit_Last)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(parent=Dialog)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.spinBox_Max = QtWidgets.QSpinBox(parent=Dialog)
        self.spinBox_Max.setMaximum(1000)
        self.spinBox_Max.setProperty("value", 0)
        self.spinBox_Max.setObjectName("spinBox_Max")
        self.horizontalLayout_6.addWidget(self.spinBox_Max)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.checkBox_Cycle = QtWidgets.QCheckBox(parent=Dialog)
        self.checkBox_Cycle.setObjectName("checkBox_Cycle")
        self.verticalLayout.addWidget(self.checkBox_Cycle)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pointer Scan"))
        self.label.setText(_translate("Dialog", "Address"))
        self.label_2.setText(_translate("Dialog", "Depth"))
        self.label_3.setText(_translate("Dialog", "Scan Range"))
        self.spinBox_ScanRangeStart.setPrefix(_translate("Dialog", "0x"))
        self.label_4.setText(_translate("Dialog", "<->"))
        self.spinBox_ScanRangeEnd.setPrefix(_translate("Dialog", "0x"))
        self.checkBox_Path.setText(_translate("Dialog", "Save Results To File"))
        self.pushButton_PathBrowse.setText(_translate("Dialog", "Browse"))
        self.label_11.setText(_translate("Dialog", "Optional Parameters (0 or empty will use defaults)"))
        self.label_5.setText(_translate("Dialog", "Last Offset Scan Range"))
        self.spinBox_ScanLRangeStart.setPrefix(_translate("Dialog", "0x"))
        self.label_9.setText(_translate("Dialog", "<->"))
        self.spinBox_ScanLRangeEnd.setPrefix(_translate("Dialog", "0x"))
        self.label_6.setText(_translate("Dialog", "Minimum Chain Length"))
        self.label_7.setText(_translate("Dialog", "Last Offset Value"))
        self.label_8.setText(_translate("Dialog", "Max Results"))
        self.checkBox_Cycle.setText(_translate("Dialog", "Solve Circular References"))

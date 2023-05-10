# Form implementation generated from reading ui file 'SelectProcess.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        MainWindow.resize(443, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_SearchProcess = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_SearchProcess.setObjectName("lineEdit_SearchProcess")
        self.horizontalLayout.addWidget(self.lineEdit_SearchProcess)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget_ProcessTable = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_ProcessTable.sizePolicy().hasHeightForWidth())
        self.tableWidget_ProcessTable.setSizePolicy(sizePolicy)
        self.tableWidget_ProcessTable.setAutoFillBackground(False)
        self.tableWidget_ProcessTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget_ProcessTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_ProcessTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_ProcessTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_ProcessTable.setWordWrap(False)
        self.tableWidget_ProcessTable.setObjectName("tableWidget_ProcessTable")
        self.tableWidget_ProcessTable.setColumnCount(3)
        self.tableWidget_ProcessTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ProcessTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ProcessTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget_ProcessTable.setHorizontalHeaderItem(2, item)
        self.tableWidget_ProcessTable.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget_ProcessTable.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ProcessTable.verticalHeader().setVisible(False)
        self.tableWidget_ProcessTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget_ProcessTable)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_Open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.horizontalLayout_2.addWidget(self.pushButton_Open)
        self.pushButton_Close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.horizontalLayout_2.addWidget(self.pushButton_Close)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_CreateProcess = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CreateProcess.setObjectName("pushButton_CreateProcess")
        self.horizontalLayout_3.addWidget(self.pushButton_CreateProcess)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Please select a Process"))
        self.label.setText(_translate("MainWindow", "Name of the Process:"))
        self.tableWidget_ProcessTable.setSortingEnabled(True)
        item = self.tableWidget_ProcessTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.tableWidget_ProcessTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget_ProcessTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Process Name"))
        self.pushButton_Open.setToolTip(_translate("MainWindow", "Attach to the selected process"))
        self.pushButton_Open.setText(_translate("MainWindow", "Open"))
        self.pushButton_Close.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_CreateProcess.setToolTip(_translate("MainWindow", "Open an executable"))
        self.pushButton_CreateProcess.setText(_translate("MainWindow", "Create Process[F1]"))

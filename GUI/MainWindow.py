# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget_AddressTable = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_AddressTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.treeWidget_AddressTable.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)
        self.treeWidget_AddressTable.setDefaultDropAction(QtCore.Qt.DropAction.MoveAction)
        self.treeWidget_AddressTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.treeWidget_AddressTable.setIndentation(12)
        self.treeWidget_AddressTable.setExpandsOnDoubleClick(False)
        self.treeWidget_AddressTable.setObjectName("treeWidget_AddressTable")
        self.gridLayout.addWidget(self.treeWidget_AddressTable, 3, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinAndMaxSize)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_MemoryView = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_MemoryView.setEnabled(False)
        self.pushButton_MemoryView.setObjectName("pushButton_MemoryView")
        self.horizontalLayout_8.addWidget(self.pushButton_MemoryView)
        spacerItem = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.pushButton_CopyToAddressTable = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CopyToAddressTable.setText("")
        self.pushButton_CopyToAddressTable.setObjectName("pushButton_CopyToAddressTable")
        self.horizontalLayout_8.addWidget(self.pushButton_CopyToAddressTable)
        self.pushButton_CleanAddressTable = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CleanAddressTable.setText("")
        self.pushButton_CleanAddressTable.setObjectName("pushButton_CleanAddressTable")
        self.horizontalLayout_8.addWidget(self.pushButton_CleanAddressTable)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.pushButton_RefreshAdressTable = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_RefreshAdressTable.setText("")
        self.pushButton_RefreshAdressTable.setObjectName("pushButton_RefreshAdressTable")
        self.horizontalLayout_8.addWidget(self.pushButton_RefreshAdressTable)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.pushButton_AddAddressManually = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AddAddressManually.setEnabled(False)
        self.pushButton_AddAddressManually.setObjectName("pushButton_AddAddressManually")
        self.horizontalLayout_8.addWidget(self.pushButton_AddAddressManually)
        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_AttachProcess = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_AttachProcess.sizePolicy().hasHeightForWidth())
        self.pushButton_AttachProcess.setSizePolicy(sizePolicy)
        self.pushButton_AttachProcess.setText("")
        self.pushButton_AttachProcess.setObjectName("pushButton_AttachProcess")
        self.horizontalLayout_5.addWidget(self.pushButton_AttachProcess)
        self.pushButton_Open = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Open.sizePolicy().hasHeightForWidth())
        self.pushButton_Open.setSizePolicy(sizePolicy)
        self.pushButton_Open.setText("")
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.horizontalLayout_5.addWidget(self.pushButton_Open)
        self.pushButton_Save = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Save.sizePolicy().hasHeightForWidth())
        self.pushButton_Save.setSizePolicy(sizePolicy)
        self.pushButton_Save.setText("")
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.horizontalLayout_5.addWidget(self.pushButton_Save)
        self.pushButton_Wiki = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Wiki.setText("")
        self.pushButton_Wiki.setObjectName("pushButton_Wiki")
        self.horizontalLayout_5.addWidget(self.pushButton_Wiki)
        self.pushButton_About = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_About.setText("")
        self.pushButton_About.setObjectName("pushButton_About")
        self.horizontalLayout_5.addWidget(self.pushButton_About)
        self.label_SelectedProcess = QtWidgets.QLabel(self.centralwidget)
        self.label_SelectedProcess.setObjectName("label_SelectedProcess")
        self.horizontalLayout_5.addWidget(self.label_SelectedProcess)
        self.label_InferiorStatus = QtWidgets.QLabel(self.centralwidget)
        self.label_InferiorStatus.setText("")
        self.label_InferiorStatus.setObjectName("label_InferiorStatus")
        self.horizontalLayout_5.addWidget(self.label_InferiorStatus)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_5.addWidget(self.progressBar)
        self.pushButton_Console = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Console.setText("")
        self.pushButton_Console.setObjectName("pushButton_Console")
        self.horizontalLayout_5.addWidget(self.pushButton_Console)
        self.pushButton_Settings = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Settings.sizePolicy().hasHeightForWidth())
        self.pushButton_Settings.setSizePolicy(sizePolicy)
        self.pushButton_Settings.setText("")
        self.pushButton_Settings.setObjectName("pushButton_Settings")
        self.horizontalLayout_5.addWidget(self.pushButton_Settings)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_MatchCount = QtWidgets.QLabel(self.centralwidget)
        self.label_MatchCount.setObjectName("label_MatchCount")
        self.verticalLayout_6.addWidget(self.label_MatchCount)
        self.tableWidget_valuesearchtable = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_valuesearchtable.setEnabled(True)
        self.tableWidget_valuesearchtable.setAutoFillBackground(False)
        self.tableWidget_valuesearchtable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget_valuesearchtable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_valuesearchtable.setAlternatingRowColors(True)
        self.tableWidget_valuesearchtable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableWidget_valuesearchtable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_valuesearchtable.setShowGrid(False)
        self.tableWidget_valuesearchtable.setObjectName("tableWidget_valuesearchtable")
        self.tableWidget_valuesearchtable.setColumnCount(3)
        self.tableWidget_valuesearchtable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_valuesearchtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_valuesearchtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_valuesearchtable.setHorizontalHeaderItem(2, item)
        self.tableWidget_valuesearchtable.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_valuesearchtable.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_valuesearchtable.verticalHeader().setVisible(False)
        self.tableWidget_valuesearchtable.verticalHeader().setDefaultSectionSize(23)
        self.tableWidget_valuesearchtable.verticalHeader().setMinimumSectionSize(20)
        self.verticalLayout_6.addWidget(self.tableWidget_valuesearchtable)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.QWidget_Toolbox = QtWidgets.QWidget(self.centralwidget)
        self.QWidget_Toolbox.setEnabled(False)
        self.QWidget_Toolbox.setObjectName("QWidget_Toolbox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.QWidget_Toolbox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_NewFirstScan = QtWidgets.QPushButton(self.QWidget_Toolbox)
        self.pushButton_NewFirstScan.setObjectName("pushButton_NewFirstScan")
        self.horizontalLayout_6.addWidget(self.pushButton_NewFirstScan)
        self.pushButton_NextScan = QtWidgets.QPushButton(self.QWidget_Toolbox)
        self.pushButton_NextScan.setObjectName("pushButton_NextScan")
        self.horizontalLayout_6.addWidget(self.pushButton_NextScan)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.pushButton_UndoScan = QtWidgets.QPushButton(self.QWidget_Toolbox)
        self.pushButton_UndoScan.setObjectName("pushButton_UndoScan")
        self.horizontalLayout_6.addWidget(self.pushButton_UndoScan)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.widget_Scan = QtWidgets.QWidget(self.QWidget_Toolbox)
        self.widget_Scan.setObjectName("widget_Scan")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_Scan)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_3 = QtWidgets.QWidget(self.widget_Scan)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_Bits = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_Bits.setObjectName("radioButton_Bits")
        self.verticalLayout_2.addWidget(self.radioButton_Bits)
        self.radioButton_Decimal = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_Decimal.setObjectName("radioButton_Decimal")
        self.verticalLayout_2.addWidget(self.radioButton_Decimal)
        self.checkBox_Hex = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_Hex.setObjectName("checkBox_Hex")
        self.verticalLayout_2.addWidget(self.checkBox_Hex)
        self.horizontalLayout_7.addWidget(self.widget_3)
        self.lineEdit_Scan = QtWidgets.QLineEdit(self.widget_Scan)
        self.lineEdit_Scan.setObjectName("lineEdit_Scan")
        self.horizontalLayout_7.addWidget(self.lineEdit_Scan)
        self.label_Between = QtWidgets.QLabel(self.widget_Scan)
        self.label_Between.setObjectName("label_Between")
        self.horizontalLayout_7.addWidget(self.label_Between)
        self.lineEdit_Scan2 = QtWidgets.QLineEdit(self.widget_Scan)
        self.lineEdit_Scan2.setObjectName("lineEdit_Scan2")
        self.horizontalLayout_7.addWidget(self.lineEdit_Scan2)
        self.verticalLayout_5.addWidget(self.widget_Scan)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget = QtWidgets.QWidget(self.QWidget_Toolbox)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox_ScanType = QtWidgets.QComboBox(self.widget)
        self.comboBox_ScanType.setObjectName("comboBox_ScanType")
        self.horizontalLayout_2.addWidget(self.comboBox_ScanType)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_ValueType = QtWidgets.QComboBox(self.widget)
        self.comboBox_ValueType.setObjectName("comboBox_ValueType")
        self.horizontalLayout.addWidget(self.comboBox_ValueType)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_ScanScope = QtWidgets.QLabel(self.widget)
        self.label_ScanScope.setObjectName("label_ScanScope")
        self.horizontalLayout_10.addWidget(self.label_ScanScope)
        self.comboBox_ScanScope = QtWidgets.QComboBox(self.widget)
        self.comboBox_ScanScope.setObjectName("comboBox_ScanScope")
        self.horizontalLayout_10.addWidget(self.comboBox_ScanScope)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_4.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.QWidget_Toolbox)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addWidget(self.widget_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9.addWidget(self.QWidget_Toolbox)
        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PINCE"))
        self.treeWidget_AddressTable.headerItem().setText(0, _translate("MainWindow", "Freeze"))
        self.treeWidget_AddressTable.headerItem().setToolTip(0, _translate("MainWindow", "Freeze the value"))
        self.treeWidget_AddressTable.headerItem().setText(1, _translate("MainWindow", "Description"))
        self.treeWidget_AddressTable.headerItem().setText(2, _translate("MainWindow", "Address"))
        self.treeWidget_AddressTable.headerItem().setText(3, _translate("MainWindow", "Type"))
        self.treeWidget_AddressTable.headerItem().setText(4, _translate("MainWindow", "Value"))
        self.pushButton_MemoryView.setText(_translate("MainWindow", "Memory View"))
        self.pushButton_CopyToAddressTable.setToolTip(_translate("MainWindow", "Copy selected items to the address table"))
        self.pushButton_CleanAddressTable.setToolTip(_translate("MainWindow", "Erase all the table contents"))
        self.pushButton_RefreshAdressTable.setToolTip(_translate("MainWindow", "Refresh the address table[R]"))
        self.pushButton_AddAddressManually.setText(_translate("MainWindow", "Add Address Manually"))
        self.pushButton_AttachProcess.setToolTip(_translate("MainWindow", "Create or attach to a process"))
        self.pushButton_Open.setToolTip(_translate("MainWindow", "Open a cheat table"))
        self.pushButton_Save.setToolTip(_translate("MainWindow", "Save current table to a file"))
        self.pushButton_Wiki.setToolTip(_translate("MainWindow", "Wiki"))
        self.pushButton_About.setToolTip(_translate("MainWindow", "About"))
        self.label_SelectedProcess.setText(_translate("MainWindow", "No Process Selected"))
        self.pushButton_Console.setToolTip(_translate("MainWindow", "Open a gdb console"))
        self.pushButton_Settings.setToolTip(_translate("MainWindow", "Configure options"))
        self.label_MatchCount.setText(_translate("MainWindow", "Match count: 0"))
        item = self.tableWidget_valuesearchtable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget_valuesearchtable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget_valuesearchtable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Previous"))
        self.pushButton_NewFirstScan.setText(_translate("MainWindow", "First Scan"))
        self.pushButton_NextScan.setText(_translate("MainWindow", "Next Scan"))
        self.pushButton_UndoScan.setText(_translate("MainWindow", "Undo Scan"))
        self.radioButton_Bits.setText(_translate("MainWindow", "B&its"))
        self.radioButton_Decimal.setText(_translate("MainWindow", "&Decimal"))
        self.checkBox_Hex.setText(_translate("MainWindow", "Hex"))
        self.label_Between.setText(_translate("MainWindow", "<->"))
        self.label.setText(_translate("MainWindow", "Scan Type:"))
        self.label_2.setText(_translate("MainWindow", "Value Type:"))
        self.label_ScanScope.setText(_translate("MainWindow", "Scan Scope:"))

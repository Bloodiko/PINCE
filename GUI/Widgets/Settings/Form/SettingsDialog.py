# Form implementation generated from reading ui file 'Widgets/Settings/Form/SettingsDialog.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(884, 633)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget_Options = QtWidgets.QListWidget(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_Options.sizePolicy().hasHeightForWidth())
        self.listWidget_Options.setSizePolicy(sizePolicy)
        self.listWidget_Options.setMaximumSize(QtCore.QSize(130, 16777215))
        self.listWidget_Options.setObjectName("listWidget_Options")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Options.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Options.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Options.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Options.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Options.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Options.addItem(item)
        self.horizontalLayout_2.addWidget(self.listWidget_Options)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=Dialog)
        self.stackedWidget.setMinimumSize(QtCore.QSize(500, 500))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_AutoUpdateAddressTable = QtWidgets.QCheckBox(parent=self.page)
        self.checkBox_AutoUpdateAddressTable.setObjectName("checkBox_AutoUpdateAddressTable")
        self.verticalLayout_2.addWidget(self.checkBox_AutoUpdateAddressTable)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.QWidget_UpdateInterval = QtWidgets.QWidget(parent=self.page)
        self.QWidget_UpdateInterval.setObjectName("QWidget_UpdateInterval")
        self.horizontalLayout_UpdateInterval = QtWidgets.QHBoxLayout(self.QWidget_UpdateInterval)
        self.horizontalLayout_UpdateInterval.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_UpdateInterval.setObjectName("horizontalLayout_UpdateInterval")
        self.label = QtWidgets.QLabel(parent=self.QWidget_UpdateInterval)
        self.label.setMinimumSize(QtCore.QSize(102, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_UpdateInterval.addWidget(self.label)
        self.spinBox_UpdateInterval = QtWidgets.QSpinBox(parent=self.QWidget_UpdateInterval)
        self.spinBox_UpdateInterval.setMinimum(100)
        self.spinBox_UpdateInterval.setMaximum(10000)
        self.spinBox_UpdateInterval.setSingleStep(100)
        self.spinBox_UpdateInterval.setObjectName("spinBox_UpdateInterval")
        self.horizontalLayout_UpdateInterval.addWidget(self.spinBox_UpdateInterval)
        self.label_2 = QtWidgets.QLabel(parent=self.QWidget_UpdateInterval)
        self.label_2.setText("ms")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_UpdateInterval.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.QWidget_UpdateInterval)
        self.LockInterval = QtWidgets.QWidget(parent=self.page)
        self.LockInterval.setObjectName("LockInterval")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.LockInterval)
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_12 = QtWidgets.QLabel(parent=self.LockInterval)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(102, 0))
        self.label_12.setBaseSize(QtCore.QSize(0, 0))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_14.addWidget(self.label_12)
        self.spinBox_FreezeInterval = QtWidgets.QSpinBox(parent=self.LockInterval)
        self.spinBox_FreezeInterval.setMinimum(100)
        self.spinBox_FreezeInterval.setMaximum(10000)
        self.spinBox_FreezeInterval.setSingleStep(100)
        self.spinBox_FreezeInterval.setObjectName("spinBox_FreezeInterval")
        self.horizontalLayout_14.addWidget(self.spinBox_FreezeInterval)
        self.label_10 = QtWidgets.QLabel(parent=self.LockInterval)
        self.label_10.setText("ms")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_14.addWidget(self.label_10)
        self.verticalLayout_3.addWidget(self.LockInterval)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(parent=self.page)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.checkBox_OutputModeAsync = QtWidgets.QCheckBox(parent=self.page)
        self.checkBox_OutputModeAsync.setObjectName("checkBox_OutputModeAsync")
        self.horizontalLayout_3.addWidget(self.checkBox_OutputModeAsync)
        self.checkBox_OutputModeCommand = QtWidgets.QCheckBox(parent=self.page)
        self.checkBox_OutputModeCommand.setObjectName("checkBox_OutputModeCommand")
        self.horizontalLayout_3.addWidget(self.checkBox_OutputModeCommand)
        self.checkBox_OutputModeCommandInfo = QtWidgets.QCheckBox(parent=self.page)
        self.checkBox_OutputModeCommandInfo.setObjectName("checkBox_OutputModeCommandInfo")
        self.horizontalLayout_3.addWidget(self.checkBox_OutputModeCommandInfo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_9 = QtWidgets.QLabel(parent=self.page)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_12.addWidget(self.label_9)
        self.lineEdit_AutoAttach = QtWidgets.QLineEdit(parent=self.page)
        self.lineEdit_AutoAttach.setObjectName("lineEdit_AutoAttach")
        self.horizontalLayout_12.addWidget(self.lineEdit_AutoAttach)
        self.checkBox_AutoAttachRegex = QtWidgets.QCheckBox(parent=self.page)
        self.checkBox_AutoAttachRegex.setObjectName("checkBox_AutoAttachRegex")
        self.horizontalLayout_12.addWidget(self.checkBox_AutoAttachRegex)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(parent=self.page)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.comboBox_Language = QtWidgets.QComboBox(parent=self.page)
        self.comboBox_Language.setObjectName("comboBox_Language")
        self.horizontalLayout_13.addWidget(self.comboBox_Language)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_11 = QtWidgets.QLabel(parent=self.page)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.comboBox_Logo = QtWidgets.QComboBox(parent=self.page)
        self.comboBox_Logo.setObjectName("comboBox_Logo")
        self.horizontalLayout_15.addWidget(self.comboBox_Logo)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_14 = QtWidgets.QLabel(parent=self.page)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_17.addWidget(self.label_14)
        self.comboBox_Theme = QtWidgets.QComboBox(parent=self.page)
        self.comboBox_Theme.setObjectName("comboBox_Theme")
        self.horizontalLayout_17.addWidget(self.comboBox_Theme)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.page_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.listWidget_Functions = QtWidgets.QListWidget(parent=self.page_2)
        self.listWidget_Functions.setObjectName("listWidget_Functions")
        self.verticalLayout_4.addWidget(self.listWidget_Functions)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_Hotkey = QtWidgets.QVBoxLayout()
        self.verticalLayout_Hotkey.setObjectName("verticalLayout_Hotkey")
        self.label_4 = QtWidgets.QLabel(parent=self.page_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_Hotkey.addWidget(self.label_4)
        self.lineEdit_Hotkey = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEdit_Hotkey.setReadOnly(True)
        self.lineEdit_Hotkey.setObjectName("lineEdit_Hotkey")
        self.verticalLayout_Hotkey.addWidget(self.lineEdit_Hotkey)
        self.verticalLayout_6.addLayout(self.verticalLayout_Hotkey)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.pushButton_ClearHotkey = QtWidgets.QPushButton(parent=self.page_2)
        self.pushButton_ClearHotkey.setObjectName("pushButton_ClearHotkey")
        self.horizontalLayout_4.addWidget(self.pushButton_ClearHotkey)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_5 = QtWidgets.QLabel(parent=self.page_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.radioButton_SimpleDLopenCall = QtWidgets.QRadioButton(parent=self.page_3)
        self.radioButton_SimpleDLopenCall.setObjectName("radioButton_SimpleDLopenCall")
        self.verticalLayout_7.addWidget(self.radioButton_SimpleDLopenCall)
        self.radioButton_AdvancedInjection = QtWidgets.QRadioButton(parent=self.page_3)
        self.radioButton_AdvancedInjection.setEnabled(False)
        self.radioButton_AdvancedInjection.setObjectName("radioButton_AdvancedInjection")
        self.verticalLayout_7.addWidget(self.radioButton_AdvancedInjection)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(spacerItem9)
        self.gridLayout_4.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.checkBox_ShowMemoryViewOnStop = QtWidgets.QCheckBox(parent=self.page_4)
        self.checkBox_ShowMemoryViewOnStop.setObjectName("checkBox_ShowMemoryViewOnStop")
        self.verticalLayout_10.addWidget(self.checkBox_ShowMemoryViewOnStop)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(parent=self.page_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.spinBox_InstructionsPerScroll = QtWidgets.QSpinBox(parent=self.page_4)
        self.spinBox_InstructionsPerScroll.setObjectName("spinBox_InstructionsPerScroll")
        self.horizontalLayout_10.addWidget(self.spinBox_InstructionsPerScroll)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_16 = QtWidgets.QLabel(parent=self.page_4)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_19.addWidget(self.label_16)
        self.spinBox_BytesPerScroll = QtWidgets.QSpinBox(parent=self.page_4)
        self.spinBox_BytesPerScroll.setPrefix("0x")
        self.spinBox_BytesPerScroll.setMaximum(4096)
        self.spinBox_BytesPerScroll.setSingleStep(16)
        self.spinBox_BytesPerScroll.setDisplayIntegerBase(16)
        self.spinBox_BytesPerScroll.setObjectName("spinBox_BytesPerScroll")
        self.horizontalLayout_19.addWidget(self.spinBox_BytesPerScroll)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem11)
        self.verticalLayout_10.addLayout(self.horizontalLayout_19)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_10.addItem(spacerItem12)
        self.gridLayout_5.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_101 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_101.setObjectName("horizontalLayout_101")
        self.label_GDBPath = QtWidgets.QLabel(parent=self.page_5)
        self.label_GDBPath.setObjectName("label_GDBPath")
        self.horizontalLayout_101.addWidget(self.label_GDBPath)
        self.lineEdit_GDBPath = QtWidgets.QLineEdit(parent=self.page_5)
        self.lineEdit_GDBPath.setObjectName("lineEdit_GDBPath")
        self.horizontalLayout_101.addWidget(self.lineEdit_GDBPath)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_101)
        self.pushButton_GDBPath = QtWidgets.QPushButton(parent=self.page_5)
        self.pushButton_GDBPath.setObjectName("pushButton_GDBPath")
        self.horizontalLayout_11.addWidget(self.pushButton_GDBPath)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        self.checkBox_GDBLogging = QtWidgets.QCheckBox(parent=self.page_5)
        self.checkBox_GDBLogging.setObjectName("checkBox_GDBLogging")
        self.verticalLayout_11.addWidget(self.checkBox_GDBLogging)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_15 = QtWidgets.QLabel(parent=self.page_5)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_18.addWidget(self.label_15)
        self.comboBox_InterruptSignal = QtWidgets.QComboBox(parent=self.page_5)
        self.comboBox_InterruptSignal.setObjectName("comboBox_InterruptSignal")
        self.horizontalLayout_18.addWidget(self.comboBox_InterruptSignal)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem13)
        self.verticalLayout_11.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButton_HandleSignals = QtWidgets.QPushButton(parent=self.page_5)
        self.pushButton_HandleSignals.setObjectName("pushButton_HandleSignals")
        self.horizontalLayout_16.addWidget(self.pushButton_HandleSignals)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem14)
        self.verticalLayout_11.addLayout(self.horizontalLayout_16)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_11.addItem(spacerItem15)
        self.gridLayout_6.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.checkBox_JavaSegfault = QtWidgets.QCheckBox(parent=self.page_6)
        self.checkBox_JavaSegfault.setObjectName("checkBox_JavaSegfault")
        self.gridLayout_7.addWidget(self.checkBox_JavaSegfault, 0, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem16, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_ResetSettings = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_ResetSettings.setObjectName("pushButton_ResetSettings")
        self.horizontalLayout.addWidget(self.pushButton_ResetSettings)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem17)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        self.listWidget_Functions.setCurrentRow(-1)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        __sortingEnabled = self.listWidget_Options.isSortingEnabled()
        self.listWidget_Options.setSortingEnabled(False)
        item = self.listWidget_Options.item(0)
        item.setText(_translate("Dialog", "General"))
        item = self.listWidget_Options.item(1)
        item.setText(_translate("Dialog", "Hotkeys"))
        item = self.listWidget_Options.item(2)
        item.setText(_translate("Dialog", "Code Injection"))
        item = self.listWidget_Options.item(3)
        item.setText(_translate("Dialog", "Memory View"))
        item = self.listWidget_Options.item(4)
        item.setText(_translate("Dialog", "Debug"))
        item = self.listWidget_Options.item(5)
        item.setText(_translate("Dialog", "Java"))
        self.listWidget_Options.setSortingEnabled(__sortingEnabled)
        self.checkBox_AutoUpdateAddressTable.setText(_translate("Dialog", "Auto-update address table"))
        self.label.setText(_translate("Dialog", "Update Interval"))
        self.label_12.setText(_translate("Dialog", "Freeze Interval"))
        self.label_8.setText(_translate("Dialog", "GDB output:"))
        self.checkBox_OutputModeAsync.setText(_translate("Dialog", "Async"))
        self.checkBox_OutputModeCommand.setText(_translate("Dialog", "Command"))
        self.checkBox_OutputModeCommandInfo.setText(_translate("Dialog", "Command info"))
        self.label_9.setToolTip(_translate("Dialog", "On start, automatically attach to processes with name matching one of the entries\n"
"Patterns at former positions have higher priority if regex is off"))
        self.label_9.setText(_translate("Dialog", "Auto-attach to processes named"))
        self.checkBox_AutoAttachRegex.setText(_translate("Dialog", "Regex"))
        self.label_13.setText(_translate("Dialog", "Language"))
        self.label_11.setText(_translate("Dialog", "Logo"))
        self.label_14.setText(_translate("Dialog", "Theme"))
        self.label_3.setText(_translate("Dialog", "Functions"))
        self.label_4.setText(_translate("Dialog", "Hotkey"))
        self.lineEdit_Hotkey.setPlaceholderText(_translate("Dialog", "Press shortcut"))
        self.pushButton_ClearHotkey.setText(_translate("Dialog", "Clear"))
        self.label_5.setText(_translate("Dialog", "Code injection method:"))
        self.radioButton_SimpleDLopenCall.setText(_translate("Dialog", "Simp&le dlopen call"))
        self.radioButton_AdvancedInjection.setText(_translate("Dialog", "Advanced In&jection"))
        self.checkBox_ShowMemoryViewOnStop.setText(_translate("Dialog", "Bring Memory View to front when the inferior is stopped"))
        self.label_6.setText(_translate("Dialog", "Instructions shown per scroll in Disassembly View"))
        self.label_16.setText(_translate("Dialog", "Bytes shown per scroll in Hex View"))
        self.label_GDBPath.setText(_translate("Dialog", "GDB Path"))
        self.checkBox_GDBLogging.setText(_translate("Dialog", "GDB Logging"))
        self.label_15.setText(_translate("Dialog", "Interruption signal"))
        self.pushButton_HandleSignals.setText(_translate("Dialog", "Handle Signals"))
        self.checkBox_JavaSegfault.setText(_translate("Dialog", "Ignore SIGSEGV for Java processes (overrides signal settings if enabled)"))
        self.pushButton_ResetSettings.setText(_translate("Dialog", "Reset Settings"))

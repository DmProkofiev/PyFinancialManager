# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1059, 750)
        icon = QIcon()
        icon.addFile(u"Resources/FIBERFMico.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        self.tabWidget.setFont(font)
        self.tabDashboard = QWidget()
        self.tabDashboard.setObjectName(u"tabDashboard")
        self.verticalLayout_5 = QVBoxLayout(self.tabDashboard)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frameBalance = QFrame(self.tabDashboard)
        self.frameBalance.setObjectName(u"frameBalance")
        self.verticalLayout_2 = QVBoxLayout(self.frameBalance)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_balance_title = QLabel(self.frameBalance)
        self.label_balance_title.setObjectName(u"label_balance_title")

        self.verticalLayout_2.addWidget(self.label_balance_title)

        self.label_balance_value = QLabel(self.frameBalance)
        self.label_balance_value.setObjectName(u"label_balance_value")
        self.label_balance_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_balance_value)


        self.gridLayout.addWidget(self.frameBalance, 0, 0, 1, 1)

        self.frameExpenses = QFrame(self.tabDashboard)
        self.frameExpenses.setObjectName(u"frameExpenses")
        self.verticalLayout_3 = QVBoxLayout(self.frameExpenses)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_expenses_title = QLabel(self.frameExpenses)
        self.label_expenses_title.setObjectName(u"label_expenses_title")

        self.verticalLayout_3.addWidget(self.label_expenses_title)

        self.label_expenses_value = QLabel(self.frameExpenses)
        self.label_expenses_value.setObjectName(u"label_expenses_value")
        self.label_expenses_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_expenses_value)


        self.gridLayout.addWidget(self.frameExpenses, 0, 1, 1, 1)

        self.frameIncomes = QFrame(self.tabDashboard)
        self.frameIncomes.setObjectName(u"frameIncomes")
        self.verticalLayout_4 = QVBoxLayout(self.frameIncomes)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_incomes_title = QLabel(self.frameIncomes)
        self.label_incomes_title.setObjectName(u"label_incomes_title")

        self.verticalLayout_4.addWidget(self.label_incomes_title)

        self.label_incomes_value = QLabel(self.frameIncomes)
        self.label_incomes_value.setObjectName(u"label_incomes_value")
        self.label_incomes_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_incomes_value)


        self.gridLayout.addWidget(self.frameIncomes, 1, 0, 1, 1)

        self.frameObligations = QFrame(self.tabDashboard)
        self.frameObligations.setObjectName(u"frameObligations")
        self.verticalLayout_6 = QVBoxLayout(self.frameObligations)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_obligations_title = QLabel(self.frameObligations)
        self.label_obligations_title.setObjectName(u"label_obligations_title")

        self.verticalLayout_6.addWidget(self.label_obligations_title)

        self.label_obligations_value = QLabel(self.frameObligations)
        self.label_obligations_value.setObjectName(u"label_obligations_value")
        self.label_obligations_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_obligations_value)


        self.gridLayout.addWidget(self.frameObligations, 1, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.labelStatistics = QLabel(self.tabDashboard)
        self.labelStatistics.setObjectName(u"labelStatistics")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setBold(True)
        self.labelStatistics.setFont(font1)
        self.labelStatistics.setStyleSheet(u"font-size: 16px; font-weight: bold; margin-top: 10px;")

        self.verticalLayout_5.addWidget(self.labelStatistics)

        self.tableMonthStatistics = QTableWidget(self.tabDashboard)
        if (self.tableMonthStatistics.columnCount() < 4):
            self.tableMonthStatistics.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableMonthStatistics.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableMonthStatistics.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableMonthStatistics.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableMonthStatistics.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableMonthStatistics.setObjectName(u"tableMonthStatistics")
        self.tableMonthStatistics.setFont(font)
        self.tableMonthStatistics.setAlternatingRowColors(True)
        self.tableMonthStatistics.horizontalHeader().setVisible(True)
        self.tableMonthStatistics.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_5.addWidget(self.tableMonthStatistics)

        self.tabWidget.addTab(self.tabDashboard, "")
        self.tabIncomes = QWidget()
        self.tabIncomes.setObjectName(u"tabIncomes")
        self.verticalLayout_8 = QVBoxLayout(self.tabIncomes)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayoutIncome = QHBoxLayout()
        self.horizontalLayoutIncome.setObjectName(u"horizontalLayoutIncome")
        self.btnIncomePrevMonth = QPushButton(self.tabIncomes)
        self.btnIncomePrevMonth.setObjectName(u"btnIncomePrevMonth")
        self.btnIncomePrevMonth.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayoutIncome.addWidget(self.btnIncomePrevMonth)

        self.labelIncomeCurrentMonth = QLabel(self.tabIncomes)
        self.labelIncomeCurrentMonth.setObjectName(u"labelIncomeCurrentMonth")
        self.labelIncomeCurrentMonth.setFont(font)
        self.labelIncomeCurrentMonth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayoutIncome.addWidget(self.labelIncomeCurrentMonth)

        self.btnIncomeNextMonth = QPushButton(self.tabIncomes)
        self.btnIncomeNextMonth.setObjectName(u"btnIncomeNextMonth")
        self.btnIncomeNextMonth.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayoutIncome.addWidget(self.btnIncomeNextMonth)

        self.lineEditIncomeAmount = QLineEdit(self.tabIncomes)
        self.lineEditIncomeAmount.setObjectName(u"lineEditIncomeAmount")
        self.lineEditIncomeAmount.setFont(font)

        self.horizontalLayoutIncome.addWidget(self.lineEditIncomeAmount)

        self.lineEditIncomeDate = QLineEdit(self.tabIncomes)
        self.lineEditIncomeDate.setObjectName(u"lineEditIncomeDate")
        self.lineEditIncomeDate.setFont(font)

        self.horizontalLayoutIncome.addWidget(self.lineEditIncomeDate)

        self.comboBoxIncomeType = QComboBox(self.tabIncomes)
        self.comboBoxIncomeType.setObjectName(u"comboBoxIncomeType")
        self.comboBoxIncomeType.setFont(font)

        self.horizontalLayoutIncome.addWidget(self.comboBoxIncomeType)

        self.lineEditIncomeDesc = QLineEdit(self.tabIncomes)
        self.lineEditIncomeDesc.setObjectName(u"lineEditIncomeDesc")
        self.lineEditIncomeDesc.setFont(font)

        self.horizontalLayoutIncome.addWidget(self.lineEditIncomeDesc)

        self.btnAddIncome = QPushButton(self.tabIncomes)
        self.btnAddIncome.setObjectName(u"btnAddIncome")
        self.btnAddIncome.setFont(font)

        self.horizontalLayoutIncome.addWidget(self.btnAddIncome)

        self.btnUpdateIncome = QPushButton(self.tabIncomes)
        self.btnUpdateIncome.setObjectName(u"btnUpdateIncome")

        self.horizontalLayoutIncome.addWidget(self.btnUpdateIncome)

        self.btnDeleteIncome = QPushButton(self.tabIncomes)
        self.btnDeleteIncome.setObjectName(u"btnDeleteIncome")
        self.btnDeleteIncome.setFont(font)

        self.horizontalLayoutIncome.addWidget(self.btnDeleteIncome)


        self.verticalLayout_8.addLayout(self.horizontalLayoutIncome)

        self.tableIncomes = QTableWidget(self.tabIncomes)
        if (self.tableIncomes.columnCount() < 4):
            self.tableIncomes.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableIncomes.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableIncomes.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableIncomes.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableIncomes.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tableIncomes.setObjectName(u"tableIncomes")
        self.tableIncomes.setAlternatingRowColors(True)
        self.tableIncomes.horizontalHeader().setVisible(True)
        self.tableIncomes.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_8.addWidget(self.tableIncomes)

        self.tabWidget.addTab(self.tabIncomes, "")
        self.tabExpenses = QWidget()
        self.tabExpenses.setObjectName(u"tabExpenses")
        self.verticalLayout_7 = QVBoxLayout(self.tabExpenses)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayoutExpense = QHBoxLayout()
        self.horizontalLayoutExpense.setObjectName(u"horizontalLayoutExpense")
        self.btnExpensePrevMonth = QPushButton(self.tabExpenses)
        self.btnExpensePrevMonth.setObjectName(u"btnExpensePrevMonth")
        self.btnExpensePrevMonth.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayoutExpense.addWidget(self.btnExpensePrevMonth)

        self.labelExpenseCurrentMonth = QLabel(self.tabExpenses)
        self.labelExpenseCurrentMonth.setObjectName(u"labelExpenseCurrentMonth")
        self.labelExpenseCurrentMonth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayoutExpense.addWidget(self.labelExpenseCurrentMonth)

        self.btnExpenseNextMonth = QPushButton(self.tabExpenses)
        self.btnExpenseNextMonth.setObjectName(u"btnExpenseNextMonth")
        self.btnExpenseNextMonth.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayoutExpense.addWidget(self.btnExpenseNextMonth)

        self.lineEditExpenseAmount = QLineEdit(self.tabExpenses)
        self.lineEditExpenseAmount.setObjectName(u"lineEditExpenseAmount")

        self.horizontalLayoutExpense.addWidget(self.lineEditExpenseAmount)

        self.lineEditExpenseDate = QLineEdit(self.tabExpenses)
        self.lineEditExpenseDate.setObjectName(u"lineEditExpenseDate")
        self.lineEditExpenseDate.setFont(font)

        self.horizontalLayoutExpense.addWidget(self.lineEditExpenseDate)

        self.comboBoxExpenseType = QComboBox(self.tabExpenses)
        self.comboBoxExpenseType.setObjectName(u"comboBoxExpenseType")

        self.horizontalLayoutExpense.addWidget(self.comboBoxExpenseType)

        self.lineEditExpenseDesc = QLineEdit(self.tabExpenses)
        self.lineEditExpenseDesc.setObjectName(u"lineEditExpenseDesc")

        self.horizontalLayoutExpense.addWidget(self.lineEditExpenseDesc)

        self.btnAddExpense = QPushButton(self.tabExpenses)
        self.btnAddExpense.setObjectName(u"btnAddExpense")

        self.horizontalLayoutExpense.addWidget(self.btnAddExpense)

        self.btnUpdateExpense = QPushButton(self.tabExpenses)
        self.btnUpdateExpense.setObjectName(u"btnUpdateExpense")

        self.horizontalLayoutExpense.addWidget(self.btnUpdateExpense)

        self.btnDeleteExpense = QPushButton(self.tabExpenses)
        self.btnDeleteExpense.setObjectName(u"btnDeleteExpense")

        self.horizontalLayoutExpense.addWidget(self.btnDeleteExpense)


        self.verticalLayout_7.addLayout(self.horizontalLayoutExpense)

        self.tableExpenses = QTableWidget(self.tabExpenses)
        if (self.tableExpenses.columnCount() < 4):
            self.tableExpenses.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableExpenses.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableExpenses.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableExpenses.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableExpenses.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.tableExpenses.setObjectName(u"tableExpenses")
        self.tableExpenses.setAlternatingRowColors(True)
        self.tableExpenses.horizontalHeader().setVisible(True)
        self.tableExpenses.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_7.addWidget(self.tableExpenses)

        self.tabWidget.addTab(self.tabExpenses, "")
        self.tabObligations = QWidget()
        self.tabObligations.setObjectName(u"tabObligations")
        self.verticalLayout_9 = QVBoxLayout(self.tabObligations)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayoutInputObligation = QHBoxLayout()
        self.horizontalLayoutInputObligation.setObjectName(u"horizontalLayoutInputObligation")
        self.lineEditObligationName = QLineEdit(self.tabObligations)
        self.lineEditObligationName.setObjectName(u"lineEditObligationName")

        self.horizontalLayoutInputObligation.addWidget(self.lineEditObligationName)

        self.comboBoxObligationType = QComboBox(self.tabObligations)
        self.comboBoxObligationType.setObjectName(u"comboBoxObligationType")

        self.horizontalLayoutInputObligation.addWidget(self.comboBoxObligationType)

        self.lineEditObligationAmount = QLineEdit(self.tabObligations)
        self.lineEditObligationAmount.setObjectName(u"lineEditObligationAmount")

        self.horizontalLayoutInputObligation.addWidget(self.lineEditObligationAmount)

        self.lineEditObligationMonthlyPayment = QLineEdit(self.tabObligations)
        self.lineEditObligationMonthlyPayment.setObjectName(u"lineEditObligationMonthlyPayment")

        self.horizontalLayoutInputObligation.addWidget(self.lineEditObligationMonthlyPayment)

        self.lineEditObligationStartDate = QLineEdit(self.tabObligations)
        self.lineEditObligationStartDate.setObjectName(u"lineEditObligationStartDate")

        self.horizontalLayoutInputObligation.addWidget(self.lineEditObligationStartDate)

        self.lineEditObligationDueDate = QLineEdit(self.tabObligations)
        self.lineEditObligationDueDate.setObjectName(u"lineEditObligationDueDate")

        self.horizontalLayoutInputObligation.addWidget(self.lineEditObligationDueDate)

        self.lineEditObligationPaidAmount = QLineEdit(self.tabObligations)
        self.lineEditObligationPaidAmount.setObjectName(u"lineEditObligationPaidAmount")

        self.horizontalLayoutInputObligation.addWidget(self.lineEditObligationPaidAmount)


        self.verticalLayout_9.addLayout(self.horizontalLayoutInputObligation)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.horizontalWidget = QWidget(self.tabObligations)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditObligationDesc = QLineEdit(self.horizontalWidget)
        self.lineEditObligationDesc.setObjectName(u"lineEditObligationDesc")

        self.horizontalLayout.addWidget(self.lineEditObligationDesc)

        self.btnAddObligation = QPushButton(self.horizontalWidget)
        self.btnAddObligation.setObjectName(u"btnAddObligation")

        self.horizontalLayout.addWidget(self.btnAddObligation)

        self.btnUpdateObligation = QPushButton(self.horizontalWidget)
        self.btnUpdateObligation.setObjectName(u"btnUpdateObligation")

        self.horizontalLayout.addWidget(self.btnUpdateObligation)

        self.btnDeleteObligation = QPushButton(self.horizontalWidget)
        self.btnDeleteObligation.setObjectName(u"btnDeleteObligation")

        self.horizontalLayout.addWidget(self.btnDeleteObligation)


        self.verticalLayout_9.addWidget(self.horizontalWidget)

        self.tableObligations = QTableWidget(self.tabObligations)
        if (self.tableObligations.columnCount() < 5):
            self.tableObligations.setColumnCount(5)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableObligations.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableObligations.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableObligations.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableObligations.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableObligations.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        self.tableObligations.setObjectName(u"tableObligations")
        self.tableObligations.setAlternatingRowColors(True)
        self.tableObligations.horizontalHeader().setVisible(True)
        self.tableObligations.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_9.addWidget(self.tableObligations)

        self.tabWidget.addTab(self.tabObligations, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FIBER Financial Manager", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.frameBalance.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card", None))
        self.label_balance_title.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441", None))
        self.label_balance_title.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card-title", None))
        self.label_balance_value.setText(QCoreApplication.translate("MainWindow", u"0 \u20bd", None))
        self.frameExpenses.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card", None))
        self.label_expenses_title.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b", None))
        self.label_expenses_title.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card-title", None))
        self.label_expenses_value.setText(QCoreApplication.translate("MainWindow", u"0 \u20bd", None))
        self.frameIncomes.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card", None))
        self.label_incomes_title.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434\u044b", None))
        self.label_incomes_title.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card-title", None))
        self.label_incomes_value.setText(QCoreApplication.translate("MainWindow", u"0 \u20bd", None))
        self.frameObligations.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card", None))
        self.label_obligations_title.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430", None))
        self.label_obligations_title.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card-title", None))
        self.label_obligations_value.setText(QCoreApplication.translate("MainWindow", u"0 \u20bd", None))
        self.labelStatistics.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u043c\u0435\u0441\u044f\u0446\u0430\u043c", None))
        ___qtablewidgetitem = self.tableMonthStatistics.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446", None))
        ___qtablewidgetitem1 = self.tableMonthStatistics.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434\u044b", None))
        ___qtablewidgetitem2 = self.tableMonthStatistics.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b", None))
        ___qtablewidgetitem3 = self.tableMonthStatistics.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u044b\u0439 \u043e\u0441\u0442\u0430\u0442\u043e\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDashboard), QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043d\u0430\u043d\u0441\u044b", None))
        self.btnIncomePrevMonth.setText(QCoreApplication.translate("MainWindow", u"\u25c0", None))
        self.labelIncomeCurrentMonth.setText("")
        self.btnIncomeNextMonth.setText(QCoreApplication.translate("MainWindow", u"\u25b6", None))
        self.lineEditIncomeAmount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.lineEditIncomeDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 01.01.2025", None))
        self.lineEditIncomeDesc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.btnAddIncome.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u043e\u0445\u043e\u0434", None))
        self.btnUpdateIncome.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btnDeleteIncome.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem4 = self.tableIncomes.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        ___qtablewidgetitem5 = self.tableIncomes.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None))
        ___qtablewidgetitem6 = self.tableIncomes.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        ___qtablewidgetitem7 = self.tableIncomes.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIncomes), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434\u044b", None))
        self.btnExpensePrevMonth.setText(QCoreApplication.translate("MainWindow", u"\u25c0", None))
        self.labelExpenseCurrentMonth.setText("")
        self.btnExpenseNextMonth.setText(QCoreApplication.translate("MainWindow", u"\u25b6", None))
        self.lineEditExpenseAmount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.lineEditExpenseDate.setText("")
        self.lineEditExpenseDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 01.01.2025", None))
        self.lineEditExpenseDesc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.btnAddExpense.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0441\u0445\u043e\u0434", None))
        self.btnUpdateExpense.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btnDeleteExpense.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem8 = self.tableExpenses.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        ___qtablewidgetitem9 = self.tableExpenses.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None))
        ___qtablewidgetitem10 = self.tableExpenses.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        ___qtablewidgetitem11 = self.tableExpenses.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabExpenses), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b", None))
        self.lineEditObligationName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.lineEditObligationAmount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.lineEditObligationMonthlyPayment.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0415\u0436\u0435\u043c\u0435\u0441\u044f\u0447\u043d\u044b\u0439 \u043f\u043b\u0430\u0442\u0435\u0436", None))
        self.lineEditObligationStartDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.lineEditObligationDueDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None))
        self.lineEditObligationPaidAmount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u043b\u0430\u0447\u0435\u043d\u043d\u0430\u044f \u0441\u0443\u043c\u043c\u0430", None))
        self.lineEditObligationDesc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.btnAddObligation.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnUpdateObligation.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btnDeleteObligation.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem12 = self.tableObligations.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        ___qtablewidgetitem13 = self.tableObligations.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None))
        ___qtablewidgetitem14 = self.tableObligations.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        ___qtablewidgetitem15 = self.tableObligations.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u0442\u043e\u043a", None))
        ___qtablewidgetitem16 = self.tableObligations.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabObligations), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430", None))
    # retranslateUi


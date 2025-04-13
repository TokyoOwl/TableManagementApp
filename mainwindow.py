from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QDialog)
import mainwindow_rc
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(759, 401)
        icon = QIcon()
        icon.addFile(u":/img/img/database.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(False)
        "================================================"
        self.tabDailySales = QWidget()
        self.tabDailySales.setObjectName(u"tabDailySales")
        self.gridLayout_6 = QGridLayout(self.tabDailySales)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableDailySales = QTableWidget(self.tabDailySales)
        if (self.tableDailySales.columnCount() < 6):
            self.tableDailySales.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableDailySales.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableDailySales.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableDailySales.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableDailySales.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableDailySales.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableDailySales.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableDailySales.setObjectName(u"tableDailySales")

        self.gridLayout_6.addWidget(self.tableDailySales, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabDailySales, "")
        "================================================="
        self.tabImploee = QWidget()
        self.tabImploee.setObjectName(u"tabImploees")
        self.gridLayout_7 = QGridLayout(self.tabImploee)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tableImploees = QTableWidget(self.tabImploee)
        if (self.tableImploees.columnCount() < 8):
            self.tableImploees.setColumnCount(8)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableImploees.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableImploees.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27  = QTableWidgetItem()
        self.tableImploees.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28  = QTableWidgetItem()
        self.tableImploees.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableImploees.setHorizontalHeaderItem(4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableImploees.setHorizontalHeaderItem(5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableImploees.setHorizontalHeaderItem(6, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableImploees.setHorizontalHeaderItem(7, __qtablewidgetitem32)
        self.tableImploees.setObjectName(u"tableImploees")

        self.gridLayout_7.addWidget(self.tableImploees, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabImploee, "")
        "+++++++++++++++++++++++++++++++++++++++++++++++++"
        self.tabProviders = QWidget()
        self.tabProviders.setObjectName(u"tabProviders")
        self.gridLayout_1 = QGridLayout(self.tabProviders)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.tableProviders = QTableWidget(self.tabProviders)
        if (self.tableProviders.columnCount() < 2):
            self.tableProviders.setColumnCount(2)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableProviders.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableProviders.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        self.tableProviders.setObjectName(u"tableProviders")

        self.gridLayout_1.addWidget(self.tableProviders, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabProviders, "")
        "================================================="
        self.tabSalesRes = QWidget()
        self.tabSalesRes.setObjectName(u"tabSalesRes")
        self.gridLayout_2 = QGridLayout(self.tabSalesRes)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableSalesRes = QTableWidget(self.tabSalesRes)
        if (self.tableSalesRes.columnCount() < 5):
            self.tableSalesRes.setColumnCount(5)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableSalesRes.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableSalesRes.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17= QTableWidgetItem()
        self.tableSalesRes.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableSalesRes.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableSalesRes.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        self.tableSalesRes.setObjectName(u"tableSalesRes")

        self.gridLayout_2.addWidget(self.tableSalesRes, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabSalesRes, "")
        "================================================="
        self.tabProducts = QWidget()
        self.tabProducts.setObjectName(u"tabProducts")
        self.gridLayout_5 = QGridLayout(self.tabProducts)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableProducts = QTableWidget(self.tabProducts)
        if (self.tableProducts.columnCount() < 7):
            self.tableProducts.setColumnCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        self.tableProducts.setObjectName(u"tableProducts")

        self.gridLayout_5.addWidget(self.tableProducts, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabProducts, "")

        self.tabProductTypes = QWidget()
        self.tabProductTypes.setObjectName(u"tabProductTypes")
        self.gridLayout_4 = QGridLayout(self.tabProductTypes)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableProductTypes = QTableWidget(self.tabProductTypes)
        if (self.tableProductTypes.columnCount() < 2):
            self.tableProductTypes.setColumnCount(2)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableProductTypes.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableProductTypes.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        self.tableProductTypes.setObjectName(u"tableProductTypes")

        self.gridLayout_4.addWidget(self.tableProductTypes, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabProductTypes, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dbPath = QLineEdit(self.centralwidget)
        self.dbPath.setObjectName(u"dbPath")
        self.dbPath.setReadOnly(True)

        self.horizontalLayout.addWidget(self.dbPath)

        self.btnOpen = QPushButton(self.centralwidget)
        self.btnOpen.setObjectName(u"btnOpen")
        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnDel = QPushButton(self.centralwidget)
        self.btnDel.setObjectName(u"btnDel")
        icon1 = QIcon()
        icon1.addFile(u":/img/img/open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnOpen.setIcon(icon1)
        self.horizontalLayout.addWidget(self.btnOpen)


        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.btnAdd)
        self.verticalLayout.addWidget(self.btnDel)
        self.btnConnect = QPushButton(self.centralwidget)
        self.btnConnect.setObjectName(u"btnConnect")
        icon2 = QIcon()
        icon2.addFile(u":/img/img/connect.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnConnect.setIcon(icon2)

        self.verticalLayout.addWidget(self.btnConnect)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 759, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442\u043e\u0432\u043e\u0435 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a \u0411\u0414", None))
        ___qtablewidgetitem = self.tableDailySales.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tableDailySales.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Товар", None))
        ___qtablewidgetitem2 = self.tableDailySales.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Сотрудник", None))
        ___qtablewidgetitem3 = self.tableDailySales.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Количество", None))
        ___qtablewidgetitem4 = self.tableDailySales.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Дата", None))
        ___qtablewidgetitem5 = self.tableDailySales.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Сумма", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDailySales), QCoreApplication.translate("MainWindow", u"Суточные продажи", None))
        ___qtablewidgetitem6 = self.tableProducts.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem7 = self.tableProducts.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Тип товара", None))
        ___qtablewidgetitem8 = self.tableProducts.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Цена", None))
        ___qtablewidgetitem9 = self.tableProducts.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Количество", None))
        ___qtablewidgetitem10 = self.tableProducts.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Дата изготовления", None))
        ___qtablewidgetitem11 = self.tableProducts.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Срок годности", None))
        ___qtablewidgetitem12 = self.tableProducts.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Поставщик", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProducts), QCoreApplication.translate("MainWindow", u"Товары", None))
        ___qtablewidgetitem13 = self.tableProviders.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow",
                                                                 u"ID",
                                                                 None))
        ___qtablewidgetitem14 = self.tableProviders.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow",
                                                                 u"Поставщик",
                                                                 None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProviders), QCoreApplication.translate("MainWindow",
                                                                                                       u"Поставщики",
                                                                                                       None))
        ___qtablewidgetitem15 = self.tableSalesRes.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow",
                                                                 u"ID",
                                                                 None))
        ___qtablewidgetitem16 = self.tableSalesRes.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow",
                                                                 u"Год",
                                                                 None))
        ___qtablewidgetitem17 = self.tableSalesRes.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow",
                                                                 u"Квартал",
                                                                 None))
        ___qtablewidgetitem18 = self.tableSalesRes.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow",
                                                                 u"Выручка",
                                                                 None))
        ___qtablewidgetitem19 = self.tableSalesRes.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow",
                                                                 u"Чистая прибыль",
                                                                 None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSalesRes), QCoreApplication.translate("MainWindow",
                                                                                                        u"Результат продаж",
                                                                                                        None))
        ___qtablewidgetitem21 = self.tableProductTypes.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem22 = self.tableProductTypes.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Наименование типа", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProductTypes), QCoreApplication.translate("MainWindow", u"Типы товаров", None))
        ___qtablewidgetitem25 = self.tableImploees.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem26 = self.tableImploees.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Фамилия", None))
        ___qtablewidgetitem27 = self.tableImploees.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Имя", None))
        ___qtablewidgetitem28 = self.tableImploees.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Отчество", None))
        ___qtablewidgetitem29 = self.tableImploees.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Дата рождения", None))
        ___qtablewidgetitem30 = self.tableImploees.horizontalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Номер паспорта", None))
        ___qtablewidgetitem31 = self.tableImploees.horizontalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Телефон", None))
        ___qtablewidgetitem32 = self.tableImploees.horizontalHeaderItem(7)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Принят", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabImploee), QCoreApplication.translate("MainWindow",
                                                                                                           u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438",
                                                                                                           None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0411\u0414", None))
        self.btnOpen.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.btnConnect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow",
                                                           u"Добавить запись",
                                                           None))
        self.btnDel.setText(QCoreApplication.translate("MainWindow",
                                                       u"Удалить запись",
                                                       None))
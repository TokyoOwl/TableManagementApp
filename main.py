import sys
from wsgiref.validate import validator

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from database import *
from tables import *

from mainwindow import Ui_MainWindow

class DelWindow(QtWidgets.QMainWindow):

    def __init__(self, db, currTab, parent):
        super().__init__()

        self.currTab = currTab
        self.db = db
        self.parent = parent
        self.layout = QVBoxLayout()
        self.gridlayout = QGridLayout()
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        self.layout.addLayout(self.gridlayout)
        self.lbl = QLabel("ID записи для удаления")
        self.txt = QTextEdit()
        self.gridlayout.addWidget(self.lbl, 0, 0)
        self.gridlayout.addWidget(self.txt, 0, 1)
        self.delbtn = QPushButton("Удалить запись")
        self.layout.addWidget(self.delbtn)
        self.delbtn.clicked.connect(self.delFromTable)

    def delFromTable(self):
        match self.currTab.objectName():
            case "tabDailySales":
                ds = DaySales(id=int(self.txt.toPlainText()))
                self.db.delete_position(ds)
            case "tabImploees":
                ds = Imploee(id=int(self.txt.toPlainText()))
                self.db.delete_position(ds)
            case "tabProviders":
                ds = Provider(id=int(self.txt.toPlainText()))
                self.db.delete_position(ds)
            case "tabSalesRes":
                ds = ResultSaile(id=int(self.txt.toPlainText()))
                self.db.delete_position(ds)
            case "tabProductTypes":
                ds = TypeProduct(id=int(self.txt.toPlainText()))
                self.db.delete_position(ds)
            case "tabProducts":
                ds = Product(id=int(self.txt.toPlainText()))
                self.db.delete_position(ds)
        self.closeWindow()
    def closeWindow(self):
        self.parent.ui.tabWidget.setEnabled(True)
        self.parent.connect_db()
        self.close()
    def closeEvent(self, event):
        self.parent.ui.tabWidget.setEnabled(True)
        self.parent.connect_db()
        self.close()
        event.accept()
class BoxWindow(QtWidgets.QMainWindow):

    def __init__(self, db, currTab, parent):
        super().__init__()
        self.currTab = currTab
        self.db = db
        self.parent = parent
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        self.setGeometry(400,400,200,200)
        self.gridlayout = QGridLayout()
        self.layout.addLayout(self.gridlayout)

        self.addBtn = QPushButton("Добавить запись")
        self.layout.addWidget(self.addBtn)
        self.addBtn.clicked.connect(self.addToTable)
        self.txt = QTextEdit()
        self.txt1 = QTextEdit()
        self.txt2 = QTextEdit()
        self.txt3 = QTextEdit()
        self.txt4 = QTextEdit()
        self.txt5 = QTextEdit()
        self.txt6 = QTextEdit()
        match self.currTab.objectName():
            case "tabDailySales":
                for i in range(6):
                    match i:
                        case 0:
                            lbl = QLabel("Товар")
                            self.gridlayout.addWidget(lbl, 0, 0)
                            self.gridlayout.addWidget(self.txt, 0, 1)
                        case 1:
                            lbl = QLabel("Сотрудник")
                            self.gridlayout.addWidget(lbl, 1, 0)
                            self.gridlayout.addWidget(self.txt1, 1, 1)
                        case 2:
                            lbl = QLabel("Количество")
                            self.doubleSpinBoxDayliSalesCount = QDoubleSpinBox()
                            self.doubleSpinBoxDayliSalesCount.setRange(0, sys.float_info.max)
                            self.gridlayout.addWidget(lbl, 2, 0)
                            self.gridlayout.addWidget(self.doubleSpinBoxDayliSalesCount, 2, 1)
                        case 3:
                            lbl = QLabel("Дата")
                            self.dateTimeEditDayliSales = QDateTimeEdit()
                            self.dateTimeEditDayliSales.setCalendarPopup(True)
                            self.dateTimeEditDayliSales.setDisplayFormat("dd.MM.yyyy")
                            self.gridlayout.addWidget(lbl, 3, 0)
                            self.gridlayout.addWidget(self.dateTimeEditDayliSales, 3, 1)
                        case 4:
                            lbl = QLabel("Сумма")
                            self.doubleSpinBoxDayliSalesAmount = QDoubleSpinBox()
                            self.doubleSpinBoxDayliSalesAmount.setRange(0, sys.float_info.max)
                            self.gridlayout.addWidget(lbl, 4, 0)
                            self.gridlayout.addWidget(self.doubleSpinBoxDayliSalesAmount, 4, 1)
            case "tabImploees":
                for i in range(7):
                    match i:
                        case 0:
                            lbl = QLabel("Фамилия")
                            self.surnameWidget = QLineEdit()
                            self.surnameWidget.setPlaceholderText("Иванов")
                            validatorSurname = QRegularExpressionValidator(QRegularExpression("^[А-ЯЁ][а-яё]*$"))
                            self.surnameWidget.setValidator(validatorSurname)
                            self.gridlayout.addWidget(lbl, 0, 0)
                            self.gridlayout.addWidget(self.surnameWidget, 0, 1)
                        case 1:
                            lbl = QLabel("Имя")
                            self.nameWidget = QLineEdit()
                            self.nameWidget.setPlaceholderText("Иван")
                            validatorName = QRegularExpressionValidator(QRegularExpression("^[А-ЯЁ][а-яё]*$"))
                            self.nameWidget.setValidator(validatorName)
                            self.gridlayout.addWidget(lbl, 1, 0)
                            self.gridlayout.addWidget(self.nameWidget, 1, 1)
                        case 2:
                            lbl = QLabel("Отчество")
                            self.patronymicWidget = QLineEdit()
                            self.patronymicWidget.setPlaceholderText("Иванович")
                            validatorPatronymic = QRegularExpressionValidator(QRegularExpression("^[А-ЯЁ][а-яё]*$"))
                            self.nameWidget.setValidator(validatorPatronymic)
                            self.gridlayout.addWidget(lbl, 2, 0)
                            self.gridlayout.addWidget(self.patronymicWidget, 2, 1)
                        case 3:
                            lbl = QLabel("Дата рождения")
                            self.dateTimeEdit1 = QDateTimeEdit()
                            self.dateTimeEdit1.setCalendarPopup(True)
                            self.dateTimeEdit1.setDisplayFormat("dd.MM.yyyy")
                            self.gridlayout.addWidget(lbl, 3, 0)
                            self.gridlayout.addWidget(self.dateTimeEdit1, 3, 1)
                        case 4:
                            lbl = QLabel("Номер паспорта")
                            self.passwordWidget = QLineEdit()
                            self.passwordWidget.setPlaceholderText("2215131313")
                            validator = QRegularExpressionValidator(QRegularExpression("[0-9]{10}"))
                            self.passwordWidget.setValidator(validator)
                            self.gridlayout.addWidget(lbl, 4, 0)
                            self.gridlayout.addWidget(self.passwordWidget, 4, 1)
                        case 5:
                            lbl = QLabel("Телефон")
                            self.telephoneWidget = QLineEdit()
                            self.telephoneWidget.setPlaceholderText("+79051231313")
                            validator = QRegularExpressionValidator(QRegularExpression("(\\+[7]{1}[0-9]{10})|([8]{1}[0-9]{10})"))
                            self.telephoneWidget.setValidator(validator)
                            self.gridlayout.addWidget(lbl, 5, 0)
                            self.gridlayout.addWidget(self.telephoneWidget, 5, 1)
                        case 6:
                            lbl = QLabel("Принят")
                            self.dateTimeEdit = QDateTimeEdit()
                            self.dateTimeEdit.setCalendarPopup(True)
                            self.dateTimeEdit.setDisplayFormat("dd.MM.yyyy")
                            self.gridlayout.addWidget(lbl, 6, 0)
                            self.gridlayout.addWidget(self.dateTimeEdit, 6, 1)
            case "tabProviders":
                lbl = QLabel("Поставщик")
                self.gridlayout.addWidget(lbl, 0, 0)
                self.gridlayout.addWidget(self.txt, 0, 1)
            case "tabSalesRes":
                for i in range(4):
                    match i:
                        case 0:
                            lbl = QLabel("Год")
                            self.dateTimeEditt = QDateTimeEdit()
                            self.dateTimeEditt.setCalendarPopup(True)
                            self.dateTimeEditt.setDisplayFormat("dd.MM.yyyy")
                            self.gridlayout.addWidget(lbl, 0, 0)
                            self.gridlayout.addWidget(self.dateTimeEditt, 0, 1)
                        case 1:
                            lbl = QLabel("Квартал")
                            self.spinBox = QSpinBox()
                            self.spinBox.setRange(1,4)
                            self.gridlayout.addWidget(lbl, 1, 0)
                            self.gridlayout.addWidget(self.spinBox, 1, 1)
                        case 2:
                            lbl = QLabel("Выручка")
                            self.doubleSpinBoxViruchka = QDoubleSpinBox()
                            self.doubleSpinBoxViruchka.setRange(0, sys.float_info.max)
                            self.gridlayout.addWidget(lbl, 2, 0)
                            self.gridlayout.addWidget(self.doubleSpinBoxViruchka, 2, 1)
                        case 3:
                            lbl = QLabel("Чистая прибыль")
                            self.doubleSpinBoxPribyl = QDoubleSpinBox()
                            self.doubleSpinBoxPribyl.setRange(0, sys.float_info.max)
                            self.gridlayout.addWidget(lbl, 3, 0)
                            self.gridlayout.addWidget(self.doubleSpinBoxPribyl, 3, 1)
            case "tabProductTypes":
                lbl = QLabel("Наименование типа")
                self.gridlayout.addWidget(lbl, 0, 0)
                self.gridlayout.addWidget(self.txt, 0, 1)
            case "tabProducts":
                for i in range(6):
                    match i:
                        case 0:
                            lbl = QLabel("Тип товара")
                            self.patronymicWidget1.setPlaceholderText("Лыжи")
                            self.gridlayout.addWidget(lbl, 0, 0)
                            self.gridlayout.addWidget(self.txt, 0, 1)
                        case 1:
                            lbl = QLabel("Цена")
                            self.doubleSpinBoxPrice = QDoubleSpinBox()
                            self.doubleSpinBoxPrice.setRange(0, sys.float_info.max)
                            self.gridlayout.addWidget(lbl, 1, 0)
                            self.gridlayout.addWidget(self.doubleSpinBoxPrice, 1, 1)
                        case 2:
                            lbl = QLabel("Количество")
                            self.doubleSpinBoxCount1 = QDoubleSpinBox()
                            self.doubleSpinBoxCount1.setRange(0, sys.float_info.max)
                            self.gridlayout.addWidget(lbl, 2, 0)
                            self.gridlayout.addWidget(self.doubleSpinBoxCount1, 2, 1)
                        case 3:
                            lbl = QLabel("Дата изготовления")
                            self.dateTimeEditBorn = QDateTimeEdit()
                            self.dateTimeEditBorn.setCalendarPopup(True)
                            self.dateTimeEditBorn.setDisplayFormat("dd.MM.yyyy")
                            self.gridlayout.addWidget(lbl, 3, 0)
                            self.gridlayout.addWidget(self.dateTimeEditBorn, 3, 1)
                        case 4:
                            lbl = QLabel("Срок годности")
                            self.dateTimeEditSrok = QDateTimeEdit()
                            self.dateTimeEditSrok.setCalendarPopup(True)
                            self.dateTimeEditSrok.setDisplayFormat("dd.MM.yyyy")
                            self.gridlayout.addWidget(lbl, 4, 0)
                            self.gridlayout.addWidget(self.dateTimeEditSrok, 4, 1)
                        case 5:
                            lbl = QLabel("Поставщик")
                            self.gridlayout.addWidget(lbl, 5, 0)
                            self.gridlayout.addWidget(self.txt5, 5, 1)

    def addToTable(self):
        match self.currTab.objectName():
            case "tabDailySales":
                ds = DaySales(product=int(self.txt.toPlainText()), imploee=int(self.txt1.toPlainText()), quantity=int(self.txt2.toPlainText()),
                              data=self.txt3.toPlainText(), summ=float(self.txt4.toPlainText()))
                self.db.add_position(ds)
            case "tabImploees":
                imp = Imploee(lastName=self.txt.toPlainText(), name=self.txt1.toPlainText(), surName=self.txt2.toPlainText(), wasBorn=self.txt3.toPlainText(),
                              numberPassport=self.txt4.toPlainText(), telephone=self.txt5.toPlainText(), employment=self.txt6.toPlainText())
                self.db.add_position(imp)
            case "tabProviders":
                prv = Provider(name_provider=self.txt.toPlainText())
                self.db.add_position(prv)
            case "tabSalesRes":
                slrs = ResultSaile(year=int(self.txt.toPlainText()),quarter=int(self.txt1.toPlainText()),
                                   revenue=float(self.txt2.toPlainText()), profit=float(self.txt3.toPlainText()))
                self.db.add_position(slrs)
            case "tabProductTypes":
                prt = TypeProduct(typeName=self.txt.toPlainText())
                self.db.add_position(prt)
            case "tabProducts":
                prd = Product(typeProduct=int(self.txt.toPlainText()), price=float(self.txt1.toPlainText()),
                              quantitys=int(self.txt2.toPlainText()), dateOfManufacture=self.txt3.toPlainText(),
                              provider=int(self.txt4.toPlainText()))
                self.db.add_position(prd)
        self.closeWindow()
    def closeWindow(self):
        self.parent.ui.tabWidget.setEnabled(True)
        self.parent.connect_db()
        self.close()
    def closeEvent(self, event):
        self.parent.ui.tabWidget.setEnabled(True)
        self.parent.connect_db()
        self.close()
        event.accept()
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.dictImploeersId = {}
        self.dictProductsId = {}
        self.dictProviderId = {}
        self.dictProductsName = {}
        self.firstLoadingFlag = True
        self.isEditingFlag = False
        self.wnd: None = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.opened_windows = []
        self.db: DataBase | None = None
        self.ui.btnOpen.clicked.connect(self.open_db)
        self.ui.btnConnect.clicked.connect(self.connect_db)
        self.ui.btnAdd.clicked.connect(self.addZapis)
        self.ui.btnDel.clicked.connect(self.delZapis)
        self.currTab = self.ui.tabWidget.currentWidget()
        self.currTable = self.ui.tableImploees
        self.ui.tabWidget.currentChanged.connect(self.callTab)
        self.currTable.itemChanged.connect(self.updateDbItem)
        self.create_ui()

    def comboProductsIdActivated(self, indx, row):
        box: QtWidgets.QComboBox = self.ui.tableProducts.cellWidget(row, 1)
        key: int = 0
        for i in self.dictProductsId:
            if box.currentText() == self.dictProductsId.get(i):
                key = i
                break
        self.db.update_position(row+1, str(key), self.currTab.objectName(), 1)

    def comboProviderIdActivated(self, indx, row):
        box: QtWidgets.QComboBox = self.ui.tableProducts.cellWidget(row, 6)
        print(box)
        key: int = 0
        for i in self.dictProviderId:
            if box.currentText() == self.dictProviderId.get(i):
                key = i
                break
        self.db.update_position(row+1, str(key), self.currTab.objectName(), 6)

    def comboProductNameActivated(self, indx, row):
        box: QtWidgets.QComboBox = self.ui.tableDailySales.cellWidget(row, 1)
        key: int = 0
        for i in self.dictProductsName:
            if box.currentText() == self.dictProductsName.get(i):
                key = i
                break
        self.db.update_position(row + 1, str(key), self.currTab.objectName(), 1)

    def comboImploeeActivated(self, indx, row):
        box: QtWidgets.QComboBox = self.ui.tableDailySales.cellWidget(row, 2)
        key: int = 0
        for i in self.dictImploeersId:
            if box.currentText() == self.dictImploeersId.get(i):
                key = i
                break
        self.db.update_position(row + 1, str(key), self.currTab.objectName(), 2)

    def updateDbItem(self, item):
        if self.firstLoadingFlag == True:
            pass
        else:
            self.currTable.blockSignals(True)
            self.db.update_position(item.row()+1, item.text(), self.currTab.objectName(), item.column())
            self.connect_db()
            self.currTable.blockSignals(False)

    def callTab(self):
        # Отключаем сигнал от старой таблицы
        if hasattr(self, 'currTable') and self.currTable is not None:
            try:
                self.currTable.itemChanged.disconnect(self.updateDbItem)
            except RuntimeError:  # Если сигнал не был подключен
                pass
        # Обновляем текущую таблицу
        self.currTab = self.ui.tabWidget.currentWidget()
        self.setCurrTable()
        # Подключаем сигнал к новой таблице
        if self.currTable is not None:
            self.currTable.itemChanged.connect(self.updateDbItem)

    def setCurrTable(self):
        match self.currTab.objectName():
            case "tabDailySales":
                self.currTable = self.ui.tableDailySales
            case "tabImploees":
                self.currTable = self.ui.tableImploees
            case "tabProviders":
                self.currTable = self.ui.tableProviders
            case "tabSalesRes":
                self.currTable = self.ui.tableSalesRes
            case "tabProductTypes":
                self.currTable = self.ui.tableProductTypes
            case "tabProducts":
                self.currTable = self.ui.tableProducts




    def addZapis(self):
        self.wnd = BoxWindow(db=self.db, currTab=self.currTab, parent=self)
        self.wnd.show()
        self.ui.tabWidget.setEnabled(False)
        self.opened_windows.append(self.wnd)

    def delZapis(self):
        self.wnd = DelWindow(db=self.db, currTab=self.currTab, parent=self)
        self.wnd.show()
        self.ui.tabWidget.setEnabled(False)
        self.opened_windows.append(self.wnd)
    def closeEvent(self, event):
        # Close all opened windows when the main window is closed
        for window in self.opened_windows:
            window.close()
        event.accept()

    def create_ui(self):
        self.ui.tableSalesRes.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.tableImploees.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.tableProductTypes.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.tableProviders.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.tableProducts.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.tableDailySales.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    # Открытие диалогового окна и выбор файла
    def open_db(self):

        # Открывает диалоговое окно для выбора файла с базой данных
        file, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите файл с БД", ".", "SQLite(*.db *.sqlite)")
        # Если ничего не выбрали
        if file == '':
            return
        # В текстовое поле записываем полный путь к выбранному файлу
        self.ui.dbPath.setText(file)

    # Подключаемся к БД
    def connect_db(self):
        # Инициализируем класс для работы с БД
        self.db = DataBase(self.ui.dbPath.text())

        # Читаем из таблицы сотрудников
        res_list, error = self.db.read_positions()
        imploeers, providers, saleres, daysale, productype, product = res_list
        if error is not None:
            self.ui.tabWidget.setEnabled(False)
            self.show_error_message(self, error)
            return
        for i in imploeers:
            self.dictImploeersId[i.id] = f"{i.lastName} {i.name[0]}."
        for j in productype:
            self.dictProductsId[j.id] = f"{j.typeName}"
        for k in providers:
            self.dictProviderId[k.id] = f"{k.name_provider}"
        for h in product:
            self.dictProductsName[h.id] = f"{h.productName}"
        self.ui.tableImploees.setVisible(True)
        self.ui.tableDailySales.setVisible(True)
        self.ui.tableProviders.setVisible(True)
        self.ui.tableProducts.setVisible(True)
        self.ui.tableProductTypes.setVisible(True)
        self.ui.tableSalesRes.setVisible(True)
        self.ui.tabWidget.setEnabled(True)
        self.create_imploees_table(imploeers)
        self.create_daily_sales_table(daysale)
        self.create_providers_table(providers)
        self.create_products_table(product)
        self.create_product_types_table(productype)
        self.create_salesres_table(saleres)
        self.firstLoadingFlag = False




    @staticmethod
    def show_error_message(self, error: str | None):
        """Функция для вывода сообщения об ошибке при чтении из базы данных"""
        if error is None or error == '':
            return
        QtWidgets.QMessageBox.critical(self, "Ошибка подключения",
                                       f"Произошла ошибка при попытке считать данные из БД ... {error}")

    # Формируем таблицу по значениям для Должностей

    # Формируем таблицу по значениям для Должностей
    def create_imploees_table(self, employees: list[Imploee]):
        table: QtWidgets.QTableWidget = self.ui.tableImploees
        table.setEnabled(True)

        # Задаём количество строк и столбцов
        table.setRowCount(len(employees))
        table.setColumnCount(8)

        # Флаги для задания "поведения" отображения ячейки
        flags = QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable

        for index, employee in enumerate(employees):

            # Создаём ячейку для 1-го столбца
            tblIdItem = QtWidgets.QTableWidgetItem(str(employee.id))
            tblIdItem.setFlags(flags)

            # Создаём ячейку для 2-го столбца
            tblLastNameItem = QtWidgets.QTableWidgetItem(employee.lastName)
            tblLastNameItem.setFlags(flags)

            # Создаём ячейку для 3-го столбца
            tblFirstNameItem = QtWidgets.QTableWidgetItem(employee.name)
            tblFirstNameItem.setFlags(flags)

            # Создаём ячейку для 4-го столбца
            tblMiddleNameItem = QtWidgets.QTableWidgetItem(employee.surName)
            tblMiddleNameItem.setFlags(flags)

            # Создаём ячейку для 5-го столбца
            tblBirthdaytem = QtWidgets.QTableWidgetItem(employee.wasBorn)
            tblBirthdaytem.setFlags(flags)

            # Создаём ячейку для 6-го столбца
            tblPassportItem = QtWidgets.QTableWidgetItem(str(employee.numberPassport))
            tblPassportItem.setFlags(flags)

            # Создаём ячейку для 7-го столбца
            tblPhoneItem = QtWidgets.QTableWidgetItem(employee.telephone)
            tblPhoneItem.setFlags(flags)

            # Создаём ячейку для 8-го столбца
            tblEmplDateItem = QtWidgets.QTableWidgetItem(employee.employment)
            tblEmplDateItem.setFlags(flags)

            # Добавляем в таблицу
            table.setItem(index, 0, tblIdItem)
            table.setItem(index, 1, tblLastNameItem)
            table.setItem(index, 2, tblFirstNameItem)
            table.setItem(index, 3, tblMiddleNameItem)
            table.setItem(index, 4, tblBirthdaytem)
            table.setItem(index, 5, tblPassportItem)
            table.setItem(index, 6, tblPhoneItem)
            table.setItem(index, 7, tblEmplDateItem)

        pass
    def create_salesres_table(self, sales: list[ResultSaile]):
        table: QtWidgets.QTableWidget = self.ui.tableSalesRes
        table.setEnabled(True)

        # Задаём количество строк и столбцов
        table.setRowCount(len(sales))
        table.setColumnCount(5)

        # Флаги для задания "поведения" отображения ячейки
        flags = QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable

        for index, sale in enumerate(sales):

            # Создаём ячейку для 1-го столбца
            tblIdItem = QtWidgets.QTableWidgetItem(str(sale.id))
            tblIdItem.setFlags(flags)

            # Создаём ячейку для 2-го столбца
            tblYear = QtWidgets.QTableWidgetItem(str(sale.year))
            tblYear.setFlags(flags)

            # Создаём ячейку для 3-го столбца
            tblQuarter = QtWidgets.QTableWidgetItem(str(sale.quarter))
            tblQuarter.setFlags(flags)

            # Создаём ячейку для 4-го столбца
            tblRevenue = QtWidgets.QTableWidgetItem(str(sale.revenue))
            tblRevenue.setFlags(flags)

            # Создаём ячейку для 5-го столбца
            tblProfit = QtWidgets.QTableWidgetItem(str(sale.profit))
            tblProfit.setFlags(flags)

            # Добавляем в таблицу
            table.setItem(index, 0, tblIdItem)
            table.setItem(index, 1, tblYear)
            table.setItem(index, 2, tblQuarter)
            table.setItem(index, 3, tblRevenue)
            table.setItem(index, 4, tblProfit)



        pass
    def create_providers_table(self, providers: list[Provider]):
        table: QtWidgets.QTableWidget = self.ui.tableProviders
        table.setEnabled(True)

        # Задаём количество строк и столбцов
        table.setRowCount(len(providers))
        table.setColumnCount(2)

        # Флаги для задания "поведения" отображения ячейки
        flags = QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable

        for index, provider in enumerate(providers):

            # Создаём ячейку для 1-го столбца
            tblIdItem = QtWidgets.QTableWidgetItem(str(provider.id))
            tblIdItem.setFlags(flags)

            # Создаём ячейку для 2-го столбца
            tblProviderItem = QtWidgets.QTableWidgetItem(provider.name_provider)
            tblProviderItem.setFlags(flags)



            # Добавляем в таблицу
            table.setItem(index, 0, tblIdItem)
            table.setItem(index, 1, tblProviderItem)


        pass
    # Формируем таблицу по значениям для Типов продуктов
    def create_product_types_table(self, product_types: list[TypeProduct]):
        table: QtWidgets.QTableWidget = self.ui.tableProductTypes
        table.setEnabled(True)

        # Задаём количество строк и столбцов
        table.setRowCount(len(product_types))
        table.setColumnCount(2)

        flags = QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable

        for index, product_type in enumerate(product_types):

            # Создаём ячейку для 1-го столбца
            tblIdItem = QtWidgets.QTableWidgetItem(str(product_type.id))
            tblIdItem.setFlags(flags)

            # Создаём ячейку для 2-го столбца
            tblNameItem = QtWidgets.QTableWidgetItem(product_type.typeName)
            tblNameItem.setFlags(flags)

            # Добавляем в таблицу
            table.setItem(index, 0, tblIdItem)
            table.setItem(index, 1, tblNameItem)

        pass

    # Формируем таблицу по значениям для таблицы Товаров
    def create_products_table(self, products: list[Product]):
        table: QtWidgets.QTableWidget = self.ui.tableProducts
        table.setEnabled(True)

        # Задаём количество строк и столбцов
        table.setRowCount(len(products))
        table.setColumnCount(8)

        # Флаги для задания "поведения" отображения ячейки
        flags = QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable

        for index, product in enumerate(products):

            tblIdItem = QtWidgets.QTableWidgetItem(str(product.id))
            tblIdItem.setFlags(flags)

            tblTypeWidget = QtWidgets.QComboBox()

            for i in self.dictProductsId:
                tblTypeWidget.addItem(self.dictProductsId.get(i))

            tblTypeWidget.setCurrentIndex(product.typeProduct-1)
            tblTypeWidget.activated.connect(lambda indx, row = index: self.comboProductsIdActivated(indx, row))


            tblPrice = QtWidgets.QTableWidgetItem(str(product.price))
            tblPrice.setFlags(flags)

            tblCount = QtWidgets.QTableWidgetItem(str(product.quantitys))
            tblCount.setFlags(flags)

            tblProductionDate = QtWidgets.QTableWidgetItem(str(product.dateOfManufacture))
            tblProductionDate.setFlags(flags)

            tblExpireDate = QtWidgets.QTableWidgetItem(str(product.expirationDate))
            tblExpireDate.setFlags(flags)

            tblProviderWidget = QtWidgets.QComboBox()

            for i in self.dictProviderId:
                tblProviderWidget.addItem(self.dictProviderId.get(i))

            tblProviderWidget.setCurrentIndex(product.provider-1)
            tblProviderWidget.activated.connect(lambda indx, row = index: self.comboProviderIdActivated(indx, row))

            tblProductName =  QtWidgets.QTableWidgetItem(str(product.productName))
            tblProductName.setFlags(flags)

            table.setItem(index, 0, tblIdItem)
            table.setCellWidget(index, 1, tblTypeWidget)
            table.setItem(index, 2, tblPrice)
            table.setItem(index, 3, tblCount)
            table.setItem(index, 4, tblProductionDate)
            table.setItem(index, 5, tblExpireDate)
            table.setCellWidget(index, 6, tblProviderWidget)
            table.setItem(index, 7, tblProductName)
        pass

    # Формируем таблицу по значениям для дневных продаж
    def create_daily_sales_table(self, daily_sales: list[DaySales]):
        table: QtWidgets.QTableWidget = self.ui.tableDailySales
        table.setEnabled(True)

        # Задаём количество строк и столбцов
        table.setRowCount(len(daily_sales))
        table.setColumnCount(6)

        # Флаги для задания "поведения" отображения ячейки
        flags = QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable
        for index, daily_sale in enumerate(daily_sales):

            tblIdItem = QtWidgets.QTableWidgetItem(str(daily_sale.id))
            tblIdItem.setFlags(flags)

            tblProductIdBox = QtWidgets.QComboBox()
            for i in self.dictProductsName:
                tblProductIdBox.addItem(self.dictProductsName.get(i))
            tblProductIdBox.setCurrentIndex(daily_sale.product - 1)
            tblProductIdBox.activated.connect(lambda indx, row = index: self.comboProductNameActivated(indx, row))


            tblEmployeeIdBox = QtWidgets.QComboBox()
            for i in self.dictImploeersId:
                tblEmployeeIdBox.addItem(self.dictImploeersId.get(i))
            tblEmployeeIdBox.setCurrentIndex(daily_sale.imploee - 1)
            tblEmployeeIdBox.activated.connect(lambda indx, row = index: self.comboImploeeActivated(indx, row))

            tblCountItem = QtWidgets.QTableWidgetItem(str(daily_sale.quantity))
            tblCountItem.setFlags(flags)

            tblDateItem = QtWidgets.QTableWidgetItem(daily_sale.data)
            tblDateItem.setFlags(flags)

            tblTotalItem = QtWidgets.QTableWidgetItem(str(daily_sale.summ))
            tblTotalItem.setFlags(flags)
            table.setItem(index, 0, tblIdItem)
            table.setCellWidget(index, 1, tblProductIdBox)
            table.setCellWidget(index, 2, tblEmployeeIdBox)
            table.setItem(index, 3, tblCountItem)
            table.setItem(index, 4, tblDateItem)
            table.setItem(index, 5, tblTotalItem)
        pass

def app() -> int:
    application = QtWidgets.QApplication(sys.argv)
    #window = QUiLoader().load("mainwindow.ui", None)

    window = MainWindow()
    window.show()
    return application.exec()

if __name__ == '__main__':
    sys.exit(app())

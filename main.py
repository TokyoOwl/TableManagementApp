import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from orm import orm_service, orm_engine
from database import *
from tables import *

from mainwindow import Ui_MainWindow

class DelWindow(QtWidgets.QMainWindow):

    def __init__(self, db, currTab, parent: QtWidgets.QMainWindow, index: int):
        super().__init__()
        self.index = index
        self.currTab = currTab
        self.db = db
        self.parent = parent
        self.layout = QVBoxLayout()
        self.hlayout = QHBoxLayout()
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        self.layout.addLayout(self.hlayout)
        self.lbl = QLabel("Вы точно хотите удалить запись?")
        self.hlayout.addWidget(self.lbl)
        self.yesBtn = QPushButton("Да")
        self.noBtn = QPushButton("Нет")
        self.layout.addLayout(self.hlayout)
        self.hlayout.addWidget(self.yesBtn)
        self.hlayout.addWidget(self.noBtn)
        self.yesBtn.clicked.connect(self.delFromTable)
        self.noBtn.clicked.connect(self.closeWindow)

    def delFromTable(self):
        self.parent.db.delete_position(self.index, self.parent.currTab)
        self.closeWindow()
    def closeWindow(self):
        self.parent.ui.tabWidget.setEnabled(True)
        self.close()
    def closeEvent(self, event):
        self.parent.connect_db()
        self.parent.isEditingFlag = False
        event.accept()
class BoxWindow(QtWidgets.QMainWindow):
    """
    Пока что не работает добавление в таблицу Товары
    Причины выясню 26.04.25 после пар
    """
    def __init__(self, db, currTab, parent: QtWidgets.QMainWindow):
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
        match self.currTab.objectName():
            case "tabDailySales":
                for i in range(6):
                    match i:
                        case 0:
                            lbl = QLabel("Товар")
                            self.qComboBoxProduct = QComboBox()
                            for i in self.parent.dictProductsName:
                                self.qComboBoxProduct.addItem(self.parent.dictProductsName.get(i))
                            self.gridlayout.addWidget(lbl, 0, 0)
                            self.gridlayout.addWidget(self.qComboBoxProduct, 0, 1)
                        case 1:
                            lbl = QLabel("Сотрудник")
                            self.qComboBoxImploee = QComboBox()
                            for i in self.parent.dictImploeersId:
                                self.qComboBoxImploee.addItem(self.parent.dictImploeersId.get(i))
                            self.gridlayout.addWidget(lbl, 1, 0)
                            self.gridlayout.addWidget(self.qComboBoxImploee, 1, 1)
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
                            self.passwordWidget.setPlaceholderText("2215 131313")
                            validator = QRegularExpressionValidator(QRegularExpression("[0-9]{4} [0-9]{6}"))
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
                self.providerNameWidget = QLineEdit()
                self.providerNameWidget.setPlaceholderText("СпортТорг")
                validatorProviderName = QRegularExpressionValidator(QRegularExpression("\\D*"))
                self.providerNameWidget.setValidator(validatorProviderName)
                self.gridlayout.addWidget(lbl, 0, 0)
                self.gridlayout.addWidget(self.providerNameWidget, 0, 1)
            case "tabSalesRes":
                for i in range(4):
                    match i:
                        case 0:
                            lbl = QLabel("Год")
                            self.dateTimeEditt = QDateTimeEdit()
                            #self.dateTimeEditt.setCalendarPopup(True)
                            self.dateTimeEditt.setCurrentSection(QDateTimeEdit.Section.YearSection)
                            self.dateTimeEditt.setDisplayFormat("yyyy")
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
                self.productTypeWidget = QLineEdit()
                self.productTypeWidget.setPlaceholderText("Мячи")
                validatorProductType = QRegularExpressionValidator(QRegularExpression("\\D*"))
                self.productTypeWidget.setValidator(validatorProductType)
                self.gridlayout.addWidget(lbl, 0, 0)
                self.gridlayout.addWidget(self.productTypeWidget, 0, 1)
            case "tabProducts":
                for i in range(7):
                    match i:
                        case 0:
                            lbl = QLabel("Тип товара")
                            self.qComboTypeProduct = QComboBox()
                            for i in self.parent.dictProductsId:
                                self.qComboTypeProduct.addItem(self.parent.dictProductsId.get(i))
                            self.gridlayout.addWidget(lbl, 0, 0)
                            self.gridlayout.addWidget(self.qComboTypeProduct, 0, 1)
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
                            self.dateTimeEditSrok = QComboBox()
                            for i in range(1,5):
                                self.dateTimeEditSrok.addItem(f"{i*6}")
                            self.gridlayout.addWidget(lbl, 4, 0)
                            self.gridlayout.addWidget(self.dateTimeEditSrok, 4, 1)
                        case 5:
                            lbl = QLabel("Поставщик")
                            self.qComboProvider = QComboBox()
                            for i in self.parent.dictProviderId:
                                self.qComboProvider.addItem(self.parent.dictProviderId.get(i))
                            self.gridlayout.addWidget(lbl, 5, 0)
                            self.gridlayout.addWidget(self.qComboProvider, 5, 1)
                        case 6:
                            lbl = QLabel("Название товара")
                            self.productNameWidget = QLineEdit()
                            self.productNameWidget.setPlaceholderText("AdidasProMax League")
                            self.gridlayout.addWidget(lbl, 6, 0)
                            self.gridlayout.addWidget(self.productNameWidget, 6, 1)

    def addToTable(self):
        match self.currTab.objectName():
            case "tabDailySales":
                productName: list[int] = [i for i in self.parent.dictProductsName if self.parent.dictProductsName.get(i) == self.qComboBoxProduct.currentText()]
                imploeeId: list[int] = [i for i in self.parent.dictImploeersId if self.parent.dictImploeersId.get(i) == self.qComboBoxImploee.currentText()]
                if productName[0] is not None and imploeeId[0] is not None:
                    ds = DaySales(product=productName[0], imploee=imploeeId[0], quantity=int(self.doubleSpinBoxDayliSalesCount.value()),
                                  data=self.dateTimeEditDayliSales.text(), summ=self.doubleSpinBoxDayliSalesAmount.value())
                    self.db.add_position(ds)
                else:
                    print(f"Error: productName: {productName} or imploeeId: {imploeeId} cannot None")
            case "tabImploees":
                imp = Imploee(lastName=self.surnameWidget.text(), name=self.nameWidget.text(), surName=self.patronymicWidget.text(), wasBorn=self.dateTimeEdit1.text(),
                              numberPassport=self.passwordWidget.text(), telephone=self.telephoneWidget.text(), employment=self.dateTimeEdit.text())
                self.db.add_position(imp)
            case "tabProviders":
                prv = Provider(name_provider=self.providerNameWidget.text())
                self.db.add_position(prv)
            case "tabSalesRes":
                slrs = ResultSaile(year=int(self.dateTimeEditt.text()), quarter=self.spinBox.value(),
                                   revenue=self.doubleSpinBoxViruchka.value(), profit=self.doubleSpinBoxPribyl.value())
                self.db.add_position(slrs)
            case "tabProductTypes":
                prt = TypeProduct(typeName=self.productTypeWidget.text())
                self.db.add_position(prt)
            case "tabProducts":
                productId: list[int] = [i for i in self.parent.dictProductsId if
                                          self.parent.dictProductsId.get(i) == self.qComboTypeProduct.currentText()]
                providerId: list[int] = [i for i in self.parent.dictProviderId if
                                        self.parent.dictProviderId.get(i) == self.qComboProvider.currentText()]

                if productId[0] is not None and providerId[0] is not None:
                    prd = Product(typeProduct=productId[0], price=self.doubleSpinBoxPrice.value(), quantitys=int(self.doubleSpinBoxCount1.value()),
                                  dateOfManufacture=self.dateTimeEditBorn.text(), provider=providerId[0], productName=self.productNameWidget.text(), expirationDate=int(self.dateTimeEditSrok.currentText()))
                    self.db.add_position(prd)
                else:
                    print(f"Error: productId: {productId} or providerId: {providerId} cannot None")

        self.closeWindow()
    def closeWindow(self):
        self.parent.ui.tabWidget.setEnabled(True)
        self.close()
    def closeEvent(self, event):
        self.parent.connect_db()
        self.parent.isEditingFlag = False
        self.parent
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
        self.isUpdatingTables = False
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
        if self.isEditingFlag == True or self.isUpdatingTables == True:
            pass
        else:
            box: QtWidgets.QComboBox = self.ui.tableProducts.cellWidget(row, 0)
            key: int = 0
            for i in self.dictProductsId:
                if box.currentText() == self.dictProductsId.get(i):
                    key = i
                    break
            self.db.update_position(row+1, str(key), self.currTab.objectName(), 1)

    def comboProviderIdActivated(self, indx, row):
        if self.isEditingFlag == True or self.isUpdatingTables == True:
            pass
        else:
            box: QtWidgets.QComboBox = self.ui.tableProducts.cellWidget(row, 5)
            print(box)
            key: int = 0
            for i in self.dictProviderId:
                if box.currentText() == self.dictProviderId.get(i):
                    key = i
                    break
            self.db.update_position(row+1, str(key), self.currTab.objectName(), 6)

    def comboProductNameActivated(self, indx, row):
        if self.isEditingFlag == True or self.isUpdatingTables == True:
            pass
        else:
            box: QtWidgets.QComboBox = self.ui.tableDailySales.cellWidget(row, 0)
            key: int = 0
            for i in self.dictProductsName:
                if box.currentText() == self.dictProductsName.get(i):
                    key = i
                    break
            self.db.update_position(row + 1, str(key), self.currTab.objectName(), 1)

    def comboImploeeActivated(self, indx, row):
        if self.isEditingFlag == True or self.isUpdatingTables == True:
            pass
        else:
            box: QtWidgets.QComboBox = self.ui.tableDailySales.cellWidget(row, 1)
            key: int = 0
            for i in self.dictImploeersId:
                if box.currentText() == self.dictImploeersId.get(i):
                    key = i
                    break
            self.db.update_position(row + 1, str(key), self.currTab.objectName(), 2)

    def updateDbItem(self, item):
        if self.firstLoadingFlag == True or self.isEditingFlag == True or self.isUpdatingTables == True:
            pass
        else:
            self.currTable.blockSignals(True)
            self.db.update_position(item.row()+1, item.text(), self.currTab.objectName(), item.column()+1)
            #self.connect_db()
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

    def getTableRowId(self):
        index = self.currTable.currentRow() + 1
        print(index)
        return index

    def addZapis(self):
        self.isEditingFlag = True
        self.wnd = BoxWindow(db=self.db, currTab=self.currTab, parent=self)
        self.wnd.show()
        self.ui.tabWidget.setEnabled(False)
        self.opened_windows.append(self.wnd)

    def delZapis(self):
        self.isEditingFlag = True
        index = self.getTableRowId()
        if index != 0:
            self.wnd = DelWindow(db=self.db, currTab=self.currTab, parent=self, index=index)
            self.wnd.show()
            self.ui.tabWidget.setEnabled(False)
            self.opened_windows.append(self.wnd)
        else:
            err = QDialog()
            layout = QVBoxLayout()
            err.setLayout(layout)
            layout.addWidget(QLabel("Сначала выберите запись для удаления"))
            err.exec()
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
        self.isUpdatingTables = True
        # Инициализируем класс для работы с БД
        #self.db = DataBase(self.ui.dbPath.text())s
        dbParam = orm_engine.DatabaseConnectionParameters(orm_engine.DatabaseType.SQLite, Database=self.ui.dbPath.text())
        self.db = orm_service.Service(dbParam)
        # Читаем из таблицы сотрудников
        #res_list, error = self.db.read_positions()
        imploeers, providers, saleres, daysale, productype, product = self.db.Employees.read(), self.db.Provider.read(), self.db.ResultSales.read(), self.db.DailySales.read(), self.db.ProductTypes.read(), self.db.Products.read()
        #if error is not None:
        #    self.ui.tabWidget.setEnabled(False)
        #    self.show_error_message(self, error)
        #    return
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
        if self.firstLoadingFlag:
            self.firstLoadingFlag = False
        self.isUpdatingTables = False





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
        #table.setColumnCount(7)

        # Флаги для задания "поведения" отображения ячейки
        flags = QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable

        for index, employee in enumerate(employees):

            # Создаём ячейку для 1-го столбца
            #tblIdItem = QtWidgets.QTableWidgetItem(str(employee.id))
            #tblIdItem.setFlags(flags)

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
            #table.setItem(index, 0, tblIdItem)
            table.setItem(index, 0, tblLastNameItem)
            table.setItem(index, 1, tblFirstNameItem)
            table.setItem(index, 2, tblMiddleNameItem)
            table.setItem(index, 3, tblBirthdaytem)
            table.setItem(index, 4, tblPassportItem)
            table.setItem(index, 5, tblPhoneItem)
            table.setItem(index, 6, tblEmplDateItem)

        pass
    def create_salesres_table(self, sales: list[ResultSaile]):
        table: QtWidgets.QTableWidget = self.ui.tableSalesRes
        table.setEnabled(True)

        # Задаём количество строк и столбцов
        table.setRowCount(len(sales))
        table.setColumnCount(4)

        # Флаги для задания "поведения" отображения ячейки
        flags = QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable

        for index, sale in enumerate(sales):

            # Создаём ячейку для 1-го столбца
            #tblIdItem = QtWidgets.QTableWidgetItem(str(sale.id))
            #tblIdItem.setFlags(flags)

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
            #table.setItem(index, 0, tblIdItem)
            table.setItem(index, 0, tblYear)
            table.setItem(index, 1, tblQuarter)
            table.setItem(index, 2, tblRevenue)
            table.setItem(index, 3, tblProfit)



        pass
    def create_providers_table(self, providers: list[Provider]):
        table: QtWidgets.QTableWidget = self.ui.tableProviders
        table.setEnabled(True)

        # Задаём количество строк и столбцов
        table.setRowCount(len(providers))
        table.setColumnCount(1)

        # Флаги для задания "поведения" отображения ячейки
        flags = QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable

        for index, provider in enumerate(providers):

            # Создаём ячейку для 1-го столбца
            #tblIdItem = QtWidgets.QTableWidgetItem(str(provider.id))
            #tblIdItem.setFlags(flags)

            # Создаём ячейку для 2-го столбца
            tblProviderItem = QtWidgets.QTableWidgetItem(provider.name_provider)
            tblProviderItem.setFlags(flags)



            # Добавляем в таблицу
            #table.setItem(index, 0, tblIdItem)
            table.setItem(index, 0, tblProviderItem)


        pass
    # Формируем таблицу по значениям для Типов продуктов
    def create_product_types_table(self, product_types: list[TypeProduct]):
        table: QtWidgets.QTableWidget = self.ui.tableProductTypes
        table.setEnabled(True)

        # Задаём количество строк и столбцов
        table.setRowCount(len(product_types))
        table.setColumnCount(1)

        flags = QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable

        for index, product_type in enumerate(product_types):

            # Создаём ячейку для 1-го столбца
            #tblIdItem = QtWidgets.QTableWidgetItem(str(product_type.id))
            #tblIdItem.setFlags(flags)

            # Создаём ячейку для 2-го столбца
            tblNameItem = QtWidgets.QTableWidgetItem(product_type.typeName)
            tblNameItem.setFlags(flags)

            # Добавляем в таблицу
            #table.setItem(index, 0, tblIdItem)
            table.setItem(index, 0, tblNameItem)

        pass

    # Формируем таблицу по значениям для таблицы Товаров
    def create_products_table(self, products: list[Product]):
        table: QtWidgets.QTableWidget = self.ui.tableProducts
        table.setEnabled(True)

        # Задаём количество строк и столбцов
        table.setRowCount(len(products))
        table.setColumnCount(7)

        # Флаги для задания "поведения" отображения ячейки
        flags = QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable

        for index, product in enumerate(products):

            #tblIdItem = QtWidgets.QTableWidgetItem(str(product.id))
            #tblIdItem.setFlags(flags)

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

            #table.setItem(index, 0, tblIdItem)
            table.setCellWidget(index, 0, tblTypeWidget)
            table.setItem(index, 1, tblPrice)
            table.setItem(index, 2, tblCount)
            table.setItem(index, 3, tblProductionDate)
            table.setItem(index, 4, tblExpireDate)
            table.setCellWidget(index, 5, tblProviderWidget)
            table.setItem(index, 6, tblProductName)
        pass

    # Формируем таблицу по значениям для дневных продаж
    def create_daily_sales_table(self, daily_sales: list[DaySales]):
        table: QtWidgets.QTableWidget = self.ui.tableDailySales
        table.setEnabled(True)

        # Задаём количество строк и столбцов
        table.setRowCount(len(daily_sales))
        #table.setColumnCount(6)

        # Флаги для задания "поведения" отображения ячейки
        flags = QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable
        for index, daily_sale in enumerate(daily_sales):

            #tblIdItem = QtWidgets.QTableWidgetItem(str(daily_sale.id))
            #tblIdItem.setFlags(flags)

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
            #table.setItem(index, 0, tblIdItem)
            table.setCellWidget(index, 0, tblProductIdBox)
            table.setCellWidget(index, 1, tblEmployeeIdBox)
            table.setItem(index, 2, tblCountItem)
            table.setItem(index, 3, tblDateItem)
            table.setItem(index, 4, tblTotalItem)
        pass

def app() -> int:
    application = QtWidgets.QApplication(sys.argv)
    #window = QUiLoader().load("mainwindow.ui", None)

    window = MainWindow()
    window.show()
    return application.exec()

if __name__ == '__main__':
    sys.exit(app())

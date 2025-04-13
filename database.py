import sqlite3

from tables import *

from types import *

class DataBase:

    def __init__(self, db_path: str):
        # Абсолютный путь к БД
        self.db_path = db_path


        self.conn = sqlite3.connect(db_path)
        self.conn.close()
    def read_positions(self) -> (list, str|None):
        list_read = []
        try:
            # Подключаемся к БД
            self.conn = sqlite3.connect(self.db_path)
            # Формируем запрос и отправляем
            cursor = self.conn.cursor()
            # Здесь получаем list, состоящих из tuple значений в столбцах
            for i in range(6):
                match i:
                    case 0:
                        read = []
                        result = cursor.execute('''SELECT * FROM Сотрудники''').fetchall()
                        for r in result:
                            read.append(Imploee(*r))
                        list_read.append(read)
                    case 1:
                        read = []
                        result = cursor.execute('''SELECT * FROM Поставщики''').fetchall()
                        for r in result:
                            read.append(Provider(*r))
                        list_read.append(read)
                    case 2:
                        read = []
                        result = cursor.execute('''SELECT * FROM Результат_продаж''').fetchall()
                        for r in result:
                            read.append(ResultSaile(*r))
                        list_read.append(read)
                    case 3:
                        read = []
                        result = cursor.execute('''SELECT * FROM Суточные_продажи''').fetchall()
                        for r in result:
                            read.append(DaySales(*r))
                        list_read.append(read)
                    case 4:
                        read = []
                        result = cursor.execute('''SELECT * FROM Типы_товаров''').fetchall()
                        for r in result:
                            read.append(TypeProduct(*r))
                        list_read.append(read)
                    case 5:
                        read = []
                        result = cursor.execute('''SELECT * FROM Товары''').fetchall()
                        for r in result:
                            read.append(Product(*r))
                        list_read.append(read)
            # Преобразуем в список объектов класса Position
        except sqlite3.Error as e:
            return None,e
        finally:
            self.conn.close()
        for i in list_read:
            print("===========")
            for j in i:
                print(j)
        return list_read, None

    def add_position(self, classes: Imploee | Provider | ResultSaile | DaySales | TypeProduct | Product) -> (int, str | None):
        insert_id: int = 0
        options = SimpleNamespace()
        options.Imploee = Imploee
        options.DaySales = DaySales
        options.ResultSaile = ResultSaile
        options.Provider = Provider
        options.TypeProduct = TypeProduct
        options.Product = Product
        try:
            # Подключаемся к БД
            self.conn = sqlite3.connect(self.db_path)
            # Формируем запрос и отправляем
            cursor = self.conn.cursor()
            match type(classes):
                case options.DaySales:
                     r = cursor.execute('''INSERT INTO Суточные_продажи (Товар, Сотрудник, Количество, Дата, Сумма) VALUES (?, ?, ?, ?, ?)''',
                               (classes.product, classes.imploee, classes.quantity, classes.data, classes.summ))
                     insert_id = r.lastrowid
                case options.Imploee:
                    r = cursor.execute(
                        '''INSERT INTO Сотрудники (Фамилия, Имя, Отчество, Дата_рождения, Номер_паспорта, Телефон, Прием_на_работу) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                        (classes.lastName, classes.name, classes.surName, classes.wasBorn, classes.numberPassport, classes.telephone, classes.employment))
                    insert_id = r.lastrowid
                case options.Provider:
                    r = cursor.execute('''INSERT INTO Поставщики (Поставщик) VALUES (?)''',
                                       (classes.name_provider,))
                    insert_id = r.lastrowid
                case options.ResultSaile:
                    r = cursor.execute('''INSERT INTO Результат_продаж (Год, Квартал, Выручка, Чистая_прибыль) VALUES (?, ?, ?, ?)''',
                                       (classes.year, classes.quarter, classes.revenue, classes.profit))
                    insert_id = r.lastrowid
                case options.Product:
                    r = cursor.execute('''INSERT INTO Товары (Тип_товара, Цена, Количество, Дата_изготовления, Срок_годности, Поставщик) VALUES (?, ?, ?, ?, ?, ?)''',
                                       (classes.typeProduct, classes.price, classes.quantitys, classes.dateOfManufacture, classes.expirationDate, classes.provider))
                    insert_id = r.lastrowid
                case options.TypeProduct:
                    r = cursor.execute('''INSERT INTO Типы_товаров (Наименование_типа) VALUES (?)''',
                                       (classes.typeName,))
                    insert_id = r.lastrowid
            # Фиксируем изменение в транзакции
            self.conn.commit()
        except sqlite3.Error as e:
            return -1, f"{e}"
        finally:
            self.conn.close()
            return insert_id, None

        # Обновляет запись в таблицу.
        # Возвращает ошибку (если есть).
    def update_position(self, id: int, data: str, selectedtab: str, col: int) -> str | None:
        options = SimpleNamespace()
        options.Imploee = Imploee
        options.DaySales = DaySales
        options.ResultSaile = ResultSaile
        options.Provider = Provider
        options.TypeProduct = TypeProduct
        options.Product = Product
        try:
            # Подключаемся к БД
            self.conn = sqlite3.connect(self.db_path)
            # Формируем запрос и отправляем
            cursor = self.conn.cursor()
            match selectedtab:
                case "tabImploees":
                    match col:
                        case 1:
                            cursor.execute('''UPDATE Сотрудники SET Фамилия = ? WHERE ID = ?''', (data, id))
                        case 2:
                            cursor.execute('''UPDATE Сотрудники SET Имя = ? WHERE ID = ?''', (data, id))
                        case 3:
                            cursor.execute('''UPDATE Сотрудники SET Отчество = ? WHERE ID = ?''', (data, id))
                        case 4:
                            cursor.execute('''UPDATE Сотрудники SET Дата_рождения = ? WHERE ID = ?''', (data, id))
                        case 5:
                            cursor.execute('''UPDATE Сотрудники SET Номер_паспорта = ? WHERE ID = ?''', (data, id))
                        case 6:
                            cursor.execute('''UPDATE Сотрудники SET Телефон = ? WHERE ID = ?''', (data, id))
                        case 7:
                            cursor.execute('''UPDATE Сотрудники SET Прием_на_работу = ? WHERE ID = ?''', (data, id))
                case "tabProductTypes":
                    cursor.execute('''UPDATE Типы_товаров SET Наименование_типа = ? WHERE ID = ?''', (data, id))
                case "tabProviders":
                    cursor.execute('''UPDATE Поставщики SET Поставщик = ? WHERE ID = ?''', (data, id))
                case "tabDailySales":
                    match col:
                        case 1:
                            cursor.execute('''UPDATE Суточные_продажи SET Товар = ? WHERE ID = ?''', (int(data), id))
                        case 2:
                            cursor.execute('''UPDATE Суточные_продажи SET Сотрудник = ? WHERE ID = ?''', (int(data), id))
                        case 3:
                            cursor.execute('''UPDATE Суточные_продажи SET Количество = ? WHERE ID = ?''', (int(data), id))
                        case 4:
                            cursor.execute('''UPDATE Суточные_продажи SET Дата = ? WHERE ID = ?''', (data, id))
                        case 5:
                            cursor.execute('''UPDATE Суточные_продажи SET Сумма = ? WHERE ID = ?''', (float(data), id))
                case "tabSalesRes":
                    match col:
                        case 1:
                            cursor.execute('''UPDATE Результат_продаж SET Год = ? WHERE ID = ?''', (int(data), id))
                        case 2:
                            cursor.execute('''UPDATE Результат_продаж SET Квартал = ? WHERE ID = ?''', (int(data), id))
                        case 3:
                            cursor.execute('''UPDATE Результат_продаж SET Выручка = ? WHERE ID = ?''', (float(data), id))
                        case 4:
                            cursor.execute('''UPDATE Результат_продаж SET Чистая_прибыль = ? WHERE ID = ?''', (float(data), id))
                case "tabProduct":
                    match col:
                        case 1:
                            cursor.execute('''UPDATE Тип_товара SET Год = ? WHERE ID = ?''', (int(data), id))
                        case 2:
                            cursor.execute('''UPDATE Цена SET Год = ? WHERE ID = ?''', (float(data), id))
                        case 3:
                            cursor.execute('''UPDATE Количество SET Год = ? WHERE ID = ?''', (int(data), id))
                        case 4:
                            cursor.execute('''UPDATE Дата_изготовления SET Год = ? WHERE ID = ?''', (data, id))
                        case 5:
                            cursor.execute('''UPDATE Срок_годности SET Год = ? WHERE ID = ?''', (int(data), id))
                        case 6:
                            cursor.execute('''UPDATE Поставщик SET Год = ? WHERE ID = ?''', (int(data), id))
            # Фиксируем изменение в транзакции
            self.conn.commit()
        except sqlite3.Error as e:
            return f"{e}"
        finally:
            self.conn.close()

        return None

        # Удаляет запись в таблицу.
        # Возвращает ошибку (если есть).
    def delete_position(self, classes: Imploee | Provider | ResultSaile | DaySales | TypeProduct | Product) -> str | None:
        options = SimpleNamespace()
        options.Imploee = Imploee
        options.DaySales = DaySales
        options.ResultSaile = ResultSaile
        options.Provider = Provider
        options.TypeProduct = TypeProduct
        options.Product = Product
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            match type(classes):
                case options.Imploee:
                    cursor.execute('''DELETE FROM Сотрудники WHERE ID = ?''', (classes.id,))
                case options.DaySales:
                    cursor.execute('''DELETE FROM Суточные_продажи WHERE ID = ?''', (classes.id,))
                case options.ResultSaile:
                    cursor.execute('''DELETE FROM Результат_продаж WHERE ID = ?''', (classes.id,))
                case options.Provider:
                    cursor.execute('''DELETE FROM Поставщики WHERE ID = ?''', (classes.id,))
                case options.TypeProduct:
                    cursor.execute('''DELETE FROM Типы_товаров WHERE ID = ?''', (classes.id,))
                case options.Product:
                    cursor.execute('''DELETE FROM Товары WHERE ID = ?''', (classes.id,))
            self.conn.commit()
        except sqlite3.Error as e:
            return f"{e}"
        finally:
            self.conn.close()

        return None
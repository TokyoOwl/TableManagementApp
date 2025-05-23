from typing import Any
from sqlalchemy import Engine, result_tuple
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, subqueryload
from orm.orm_engine import DatabaseConnectionParameters, create
from orm.orm_models import *


class Base:
    def __init__(self, engine: Engine):
        self._engine = engine
        self.List = []

    def read(self):
        pass

    def add(self, data):
        pass

    def update(self, data):
        pass

    def delete(self, data: Any | None):
        pass


class Products(Base):
    def add(self, product: Product):
        """Добавление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.add(product)
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при добавлении продукта: {e}")

    def read(self):
        """Чтение данных из БД"""
        try:
            with Session(self._engine) as session:
                self.List = session.query(Product).options(subqueryload(Product.type_product), subqueryload(Product.provider), subqueryload(Product.day_sales)).all()
                return self.List
        except SQLAlchemyError as e:
            print(f"Ошибка при чтении продуктов: {e}")
            return []

    def update(self, product: Product):
        """Обновление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.query(Product).filter(Product.id == product.id).update({
                        Product.type_Product_ID: product.type_Product_ID,
                        Product.price: product.price,
                        Product.quantity: product.quantity,
                        Product.dateOfManufacture: product.dateOfManufacture,
                        Product.expirationDate: product.expirationDate,
                        Product.providerID: product.providerID,
                        Product.productName: product.productName,
                    })
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при обновлении продукта: {e}")

    def delete(self, product: Product):
        """Удаление данных из БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    if not isinstance(product, Product):
                        session.query(Product).delete()
                    else:
                        session.query(Product).filter(Product.id == product.id).delete()
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при удалении продукта: {e}")


class ProductTypes(Base):
    def add(self, product_type: TypeProduct):
        """Добавление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.add(product_type)
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при добавлении типа продукта: {e}")

    def read(self):
        """Чтение данных из БД"""
        try:
            with Session(self._engine) as session:
                self.List = session.query(TypeProduct).options(subqueryload(TypeProduct.products)).all()
                return self.List
        except SQLAlchemyError as e:
            print(f"Ошибка при чтении типов продуктов: {e}")
            return []

    def update(self, product_type: TypeProduct):
        """Обновление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.query(TypeProduct).filter(TypeProduct.id == product_type.id).update({
                        TypeProduct.typeName: product_type.typeName
                    })
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при обновлении типа продукта: {e}")

    def delete(self, product_type: TypeProduct):
        """Удаление данных из БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    if not isinstance(product_type, TypeProduct):
                        session.query(TypeProduct).delete()
                    else:
                        session.query(TypeProduct).filter(TypeProduct.id == product_type.id).delete()
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при удалении типа продукта: {e}")


class DailySales(Base):
    def add(self, daily_sale: DaySales):
        """Добавление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.add(daily_sale)
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при добавлении ежедневной продажи: {e}")

    def read(self):
        """Чтение данных из БД"""
        try:
            with Session(self._engine) as session:
                self.List = session.query(DaySales).options(subqueryload(DaySales.employee), subqueryload(DaySales.product)).all()
                return self.List
        except SQLAlchemyError as e:
            print(f"Ошибка при чтении ежедневных продаж: {e}")
            return []

    def update(self, daily_sale: DaySales):
        """Обновление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.query(DaySales).filter(DaySales.id == daily_sale.id).update({
                        DaySales.productID: daily_sale.productID,
                        DaySales.employee_ID: daily_sale.employee_ID,
                        DaySales.quantity: daily_sale.quantity,
                        DaySales.data: daily_sale.data,
                        DaySales.summ: daily_sale.summ
                    })
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при обновлении ежедневной продажи: {e}")

    def delete(self, daily_sale: DaySales):
        """Удаление данных из БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    if not isinstance(daily_sale, DaySales):
                        session.query(DaySales).delete()
                    else:
                        session.query(DaySales).filter(DaySales.id == daily_sale.id).delete()
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при удалении ежедневной продажи: {e}")


class Employees(Base):
    def add(self, employee: Employee):
        """Добавление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.add(employee)
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при добавлении сотрудника: {e}")

    def read(self):
        """Чтение данных из БД"""
        try:
            with Session(self._engine) as session:
                self.List = session.query(Employee).all()
                return self.List
        except SQLAlchemyError as e:
            print(f"Ошибка при чтении сотрудников: {e}")
            return []

    def update(self, employee: Employee):
        """Обновление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.query(Employee).filter(Employee.id == employee.id).update({
                        Employee.lastName: employee.lastName,
                        Employee.name: employee.name,
                        Employee.surName: employee.surName,
                        Employee.wasBorn: employee.wasBorn,
                        Employee.numberPassport: employee.numberPassport,
                        Employee.telephone: employee.telephone,
                        Employee.employment: employee.employment
                    })
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при обновлении сотрудника: {e}")

    def delete(self, employee: Employee):
        """Удаление данных из БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    if not isinstance(employee, Employee):
                        session.query(Employee).delete()
                    else:
                        session.query(Employee).filter(Employee.id == employee.id).delete()
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при удалении сотрудника: {e}")


class Providers(Base):
    def add(self, provider: Provider):
        """Добавление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.add(provider)
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при добавлении поставщика: {e}")

    def read(self):
        """Чтение данных из БД"""
        try:
            with Session(self._engine) as session:
                self.List = session.query(Provider).options(subqueryload(Provider.products)).all()
                return self.List
        except SQLAlchemyError as e:
            print(f"Ошибка при чтении поставщика: {e}")
            return []

    def update(self, provider: Provider):
        """Обновление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.query(Provider).filter(Provider.id == provider.id).update({
                        Provider.name: provider.name
                    })
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при обновлении поставщика: {e}")

    def delete(self, provider: Provider):
        """Удаление данных из БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    if not isinstance(provider, Provider):
                        session.query(Provider).delete()
                    else:
                        session.query(Provider).filter(Provider.id == provider.id).delete()
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при удалении поставщика: {e}")


class ResultSales(Base):
    def add(self, result_sale: ResultSale):
        """Добавление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.add(result_sale)
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при добавлении результата продаж: {e}")

    def read(self):
        """Чтение данных из БД"""
        try:
            with Session(self._engine) as session:
                self.List = session.query(ResultSale).all()
                return self.List
        except SQLAlchemyError as e:
            print(f"Ошибка при чтении результата продаж: {e}")
            return []

    def update(self, result_sale: ResultSale):
        """Обновление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.query(ResultSale).filter(ResultSale.id == result_sale.id).update({
                        ResultSale.year: result_sale.year,
                        ResultSale.quarter: result_sale.quarter,
                        ResultSale.revenue: result_sale.revenue,
                        ResultSale.profit: result_sale.profit
                    })
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при обновлении результата продаж: {e}")

    def delete(self, result_sale: ResultSale):
        """Удаление данных из БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    if not isinstance(result_sale, ResultSale):
                        session.query(ResultSale).delete()
                    else:
                        session.query(ResultSale).filter(ResultSale.id == result_sale.id).delete()
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при удалении результата продаж: {e}")


class Service:
    def __init__(self, params: DatabaseConnectionParameters):
        self.params = params
        self._engine = create(params)
        self.Products = Products(self._engine)
        self.ProductTypes = ProductTypes(self._engine)
        self.DailySales = DailySales(self._engine)
        self.Employees = Employees(self._engine)
        self.ResultSales = ResultSales(self._engine)
        self.Providers = Providers(self._engine)

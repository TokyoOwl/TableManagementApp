from typing import Any
from sqlalchemy import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, subqueryload
from orm.orm_engine import DatabaseConnectionParameters, create
from orm.orm_models import Product, ProductType, DailySale, Employee, Position


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
                self.List = session.query(Product).options(subqueryload(Product.product_type)).all()
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
                        Product.name: product.name,
                        Product.product_type_id: product.product_type_id,
                        Product.price: product.price,
                        Product.count: product.count,
                        Product.production_date: product.production_date,
                        Product.expiration_date: product.expiration_date
                    })
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при обновлении продукта: {e}")

    def delete(self, product: Product):
        """Удаление данных из БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    if product is not Product:
                        session.query(Product).delete()
                    else:
                        session.query(Product).filter(Product.id == product.id).delete()
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при удалении продукта: {e}")


class ProductTypes(Base):
    def add(self, product_type: ProductType):
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
                self.List = session.query(ProductType).all()
                return self.List
        except SQLAlchemyError as e:
            print(f"Ошибка при чтении типов продуктов: {e}")
            return []

    def update(self, product_type: ProductType):
        """Обновление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.query(ProductType).filter(ProductType.id == product_type.id).update({
                        ProductType.name: product_type.name
                    })
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при обновлении типа продукта: {e}")

    def delete(self, product_type: ProductType):
        """Удаление данных из БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    if product_type is not ProductType:
                        session.query(ProductType).delete()
                    else:
                        session.query(ProductType).filter(ProductType.id == product_type.id).delete()
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при удалении типа продукта: {e}")


class DailySales(Base):
    def add(self, daily_sale: DailySale):
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
                self.List = session.query(DailySale).options(subqueryload(DailySale.employee), subqueryload(DailySale.product)).all()
                return self.List
        except SQLAlchemyError as e:
            print(f"Ошибка при чтении ежедневных продаж: {e}")
            return []

    def update(self, daily_sale: DailySale):
        """Обновление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.query(DailySale).filter(DailySale.id == daily_sale.id).update({
                        DailySale.product_id: daily_sale.product_id,
                        DailySale.employee_id: daily_sale.employee_id,
                        DailySale.count: daily_sale.count,
                        DailySale.date: daily_sale.date,
                        DailySale.total: daily_sale.total
                    })
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при обновлении ежедневной продажи: {e}")

    def delete(self, daily_sale: DailySale):
        """Удаление данных из БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    if daily_sale is not DailySale:
                        session.query(DailySale).delete()
                    else:
                        session.query(DailySale).filter(DailySale.id == daily_sale.id).delete()
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
                self.List = session.query(Employee).options(subqueryload(Employee.position)).all()
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
                        Employee.last_name: employee.last_name,
                        Employee.first_name: employee.first_name,
                        Employee.middle_name: employee.middle_name,
                        Employee.birthday: employee.birthday,
                        Employee.position_id: employee.position_id,
                        Employee.phone: employee.phone,
                        Employee.employment_date: employee.employment_date
                    })
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при обновлении сотрудника: {e}")

    def delete(self, employee: Employee):
        """Удаление данных из БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    if employee is not Employee:
                        session.query(Employee).delete()
                    else:
                        session.query(Employee).filter(Employee.id == employee.id).delete()
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при удалении сотрудника: {e}")


class Positions(Base):
    def add(self, position: Position):
        """Добавление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.add(position)
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при добавлении должности: {e}")

    def read(self):
        """Чтение данных из БД"""
        try:
            with Session(self._engine) as session:
                self.List = session.query(Position).all()
                return self.List
        except SQLAlchemyError as e:
            print(f"Ошибка при чтении должностей: {e}")
            return []

    def update(self, position: Position):
        """Обновление данных в БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    session.query(Position).filter(Position.id == position.id).update({
                        Position.name: position.name
                    })
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при обновлении должности: {e}")

    def delete(self, position: Position):
        """Удаление данных из БД"""
        try:
            with Session(self._engine) as session:
                with session.begin():
                    if position is not Position:
                        session.query(Position).delete()
                    else:
                        session.query(Position).filter(Position.id == position.id).delete()
                    session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при удалении должности: {e}")


class Service:
    def __init__(self, params: DatabaseConnectionParameters):
        self.params = params
        self._engine = create(params)

        self.Products = Products(self._engine)
        self.ProductTypes = ProductTypes(self._engine)
        self.DailySales = DailySales(self._engine)
        self.Employees = Employees(self._engine)
        self.Positions = Positions(self._engine)

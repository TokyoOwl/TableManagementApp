import unittest

from sqlalchemy.orm import Session

import orm.orm_engine
from orm.orm_engine import DatabaseConnectionParameters, DatabaseType
from orm.orm_models import *
from orm.orm_service import Service


class ORMTest(unittest.TestCase):
    def test(self):
        dbParam = DatabaseConnectionParameters(DatabaseType.SQLite, Database="../Shop.db")
        engine = orm.orm_engine.create(dbParam)
        with Session(bind=engine) as session:
            positions = session.query(Position).all()
            employees = session.query(Employee).all()
            products = session.query(Product).all()
            productTypes = session.query(ProductType).all()
            dailySales = session.query(DailySale).all()
            pass

class TestService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Создаем тестовую базу данных в памяти
        cls.db_params = DatabaseConnectionParameters(DatabaseType.SQLite, Database=":memory:")
        cls.service = Service(cls.db_params)

    def setUp(self):
        # Очищаем базу перед каждым тестом
        self.service.DailySales.delete(None)
        self.service.Products.delete(None)
        self.service.ProductTypes.delete(None)
        self.service.Employees.delete(None)
        self.service.Positions.delete(None)


    def test_add_and_read_product_type(self):
        product_type = ProductType(name="Test Type")
        self.service.ProductTypes.add(product_type)
        result = self.service.ProductTypes.read()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Test Type")

    def test_update_product_type(self):
        product_type = ProductType(name="Old Name")
        self.service.ProductTypes.add(product_type)
        product_type = self.service.ProductTypes.read()[0]
        product_type.name = "New Name"
        self.service.ProductTypes.update(product_type)
        result = self.service.ProductTypes.read()
        self.assertEqual(result[0].name, "New Name")

    def test_delete_product_type(self):
        product_type = ProductType(name="To Delete")
        self.service.ProductTypes.add(product_type)
        product_type = self.service.ProductTypes.read()[0]
        self.service.ProductTypes.delete(product_type)
        result = self.service.ProductTypes.read()
        self.assertEqual(len(result), 0)

    def test_add_and_read_product(self):
        product_type = ProductType(name="Type")
        self.service.ProductTypes.add(product_type)
        product_type = self.service.ProductTypes.read()[0]
        product = Product(name="Test Product",
                          product_type_id=product_type.id,
                          price=100,
                          count=10,
                          production_date="2023-01-01",
                          expiration_date="2024-01-01")
        self.service.Products.add(product)
        result = self.service.Products.read()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Test Product")
        self.assertEqual(result[0].product_type.name, "Type")

    def test_add_and_read_employee(self):
        position = Position(name="Manager")
        self.service.Positions.add(position)
        position = self.service.Positions.read()[0]
        employee = Employee(
            last_name="Doe",
            first_name="John",
            middle_name="M",
            birthday="1990-01-01",
            position_id=position.id,
            phone="1234567890",
            employment_date="2020-01-01"
        )
        self.service.Employees.add(employee)
        result = self.service.Employees.read()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].last_name, "Doe")

    def test_add_and_read_daily_sale(self):
        position = Position(name="Tester")
        self.service.Positions.add(position)
        position = self.service.Positions.read()[0]

        product_type = ProductType(name="Type")
        self.service.ProductTypes.add(product_type)
        product_type = self.service.ProductTypes.read()[0]
        product = Product(name="Product",
                          product_type_id=product_type.id,
                          price=100, count=10,
                          production_date="2023-01-01", expiration_date="2024-01-01")
        self.service.Products.add(product)
        product = self.service.Products.read()[0]
        employee = Employee(
            last_name="Doe",
            first_name="John",
            middle_name="M",
            birthday="1990-01-01",
            position_id=position.id,
            phone="1234567890",
            employment_date="2020-01-01"
        )
        self.service.Employees.add(employee)
        employee = self.service.Employees.read()[0]
        daily_sale = DailySale(
            product_id=product.id,
            employee_id=employee.id,
            count=2,
            date="2023-01-01",
            total=200
        )
        self.service.DailySales.add(daily_sale)
        result = self.service.DailySales.read()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].total, 200)


if __name__ == "__main__":
    unittest.main()

import unittest

from sqlalchemy.orm import Session

import orm.orm_engine
from orm.orm_engine import DatabaseConnectionParameters, DatabaseType
from orm.orm_models import *
from orm.orm_service import Service


class ORMTest(unittest.TestCase):
    def test(self):
        dbParam = DatabaseConnectionParameters(DatabaseType.SQLite, Database=":memory:")
        engine = orm.orm_engine.create(dbParam)
        with Session(bind=engine) as session:
            provider = session.query(Provider).all()
            employees = session.query(Employee).all()
            products = session.query(Product).all()
            productTypes = session.query(TypeProduct).all()
            dailySales = session.query(DaySales).all()
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
        self.service.Provider.delete(None)
        self.service.ResultSales.delete(None)


    def test_add_and_read_product_type(self):
        product_type = TypeProduct(typeName="Test Type")
        self.service.ProductTypes.add(product_type)
        result = self.service.ProductTypes.read()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].typeName, "Test Type")

    def test_update_product_type(self):
        product_type = TypeProduct(typeName="Old Name")
        self.service.ProductTypes.add(product_type)
        product_type = self.service.ProductTypes.read()[0]
        product_type.typeName = "New Name"
        self.service.ProductTypes.update(product_type)
        result = self.service.ProductTypes.read()
        self.assertEqual(result[0].typeName, "New Name")

    def test_delete_product_type(self):
        product_type = TypeProduct(typeName="To Delete")
        self.service.ProductTypes.add(product_type)
        product_type = self.service.ProductTypes.read()[0]
        self.service.ProductTypes.delete(product_type)
        result = self.service.ProductTypes.read()
        self.assertEqual(len(result), 0)

    def test_add_and_read_product(self):
        product_type = TypeProduct(typeName="Type")
        providers = Provider(name="RRRRRRRRR")
        self.service.ProductTypes.add(product_type)
        self.service.Provider.add(providers)
        product_type = self.service.ProductTypes.read()[0]
        providers = self.service.Provider.read()[0]
        product = Product(type_Product_ID=product_type.id,
                          price=100,
                          quantity=10,
                          dateOfManufacture="2023-01-01",
                          expirationDate="2024-01-01",
                          providerID=providers.id,
                          productName="PN",)
        self.service.Products.add(product)
        result = self.service.Products.read()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].productName, "PN")
        self.assertEqual(result[0].type_product.typeName, "Type")
        self.assertEqual(result[0].provider.name, "RRRRRRRRR")

    def test_add_and_read_employee(self):
        employee = Employee(
            last_name="Doe",
            first_name="John",
            middle_name="M",
            was_born="1990-01-01",
            number_passport="2222 101010",
            phone="1234567890",
            employment="2020-01-01"
        )
        self.service.Employees.add(employee)
        result = self.service.Employees.read()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].last_name, "Doe")

    def test_add_and_read_daily_sale(self):
        product_type = TypeProduct(typeName="Type")
        providers = Provider(name="RRRRRRRRR")
        self.service.ProductTypes.add(product_type)
        self.service.Provider.add(providers)
        product_type = self.service.ProductTypes.read()[0]
        providers = self.service.Provider.read()[0]
        product = Product(type_Product_ID=product_type.id,
                          price=100,
                          quantity=10,
                          dateOfManufacture="2023-01-01",
                          expirationDate="2024-01-01",
                          providerID=providers.id,
                          productName="PN", )
        self.service.Products.add(product)
        product = self.service.Products.read()[0]
        employee = Employee(
            last_name="Doe",
            first_name="John",
            middle_name="M",
            was_born="1990-01-01",
            number_passport="2222 101010",
            phone="1234567890",
            employment="2020-01-01"
        )
        self.service.Employees.add(employee)
        employee = self.service.Employees.read()[0]
        daily_sale = DaySales(
            productID=product.id,
            employee_ID=employee.id,
            quantity=2,
            data="2023-01-01",
            summ=200
        )
        self.service.DailySales.add(daily_sale)
        result = self.service.DailySales.read()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].summ, 200)


if __name__ == "__main__":
    unittest.main()

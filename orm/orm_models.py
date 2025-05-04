from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, relationship, mapped_column

# Базовый класс. Это родительский класс для каждого класса таблицы-модели
Base = declarative_base()

class Provider(Base):
    __tablename__ = 'Provider'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name="ID")
    name: Mapped[String] = mapped_column(String, name="Name", unique=True)

class ResultSale(Base):
    __tablename__ = 'ResultSale'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name="ID")
    year: Mapped[int] = mapped_column(Integer, name="Year")
    quarter: Mapped[int] = mapped_column(Integer, name = "Quarter")
    revenue: Mapped[float] = mapped_column(Float, name = "Revenue")
    profit: Mapped[float] = mapped_column(Float, name = "Profit")


class Employee(Base):
    __tablename__ = 'Employee'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name="ID")
    last_name: Mapped[String] = mapped_column(String, name = "Lastname")
    first_name: Mapped[String] = mapped_column(String, name="Name")
    middle_name: Mapped[String] = mapped_column(String, name = "Surname")
    was_born: Mapped[int] = mapped_column(Integer, name = "WasBorn")
    number_passport: Mapped[String] = mapped_column(String, name = "NumberPassport", unique=True)
    phone: Mapped[String] = mapped_column(String, name = "NumberTelephone", unique=True)
    employment: Mapped[String] = mapped_column(String, name = "Employment")

    @property
    def last_name_and_initials(self) -> str:
        """Для вывода фамилии и инициалов. Вида Иванов И.И."""
        return f"{self.last_name} {str(self.first_name)[0]}. {str(self.middle_name)[0]}."

    def __str__(self):
        """Функция для "красивого" отображения при отладке и не только"""
        return f"[{self.id}] {self.last_name} {self.first_name} {self.middle_name} | {self.birthday} | {self.position.name} | {self.employment_date} | {self.phone}"


class DaySales(Base):
    __tablename__ = 'DaySales'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name="ID")
    productID: Mapped[int] = mapped_column(Integer, ForeignKey("Product.ID"), name = "Product")
    product: Mapped["Product"] = relationship("Product")
    employee_ID: Mapped[int] = mapped_column(Integer, ForeignKey("Employee.ID"), name = "Imploee")
    employee: Mapped["Employee"] = relationship("Employee")
    quantity: Mapped[int] = mapped_column(Integer, name = "Quantity")
    data: Mapped[int] = mapped_column(Integer, name = "Data")
    summ: Mapped[float]= mapped_column(Float, name = "Summ")

def __str__(self):
    return f"[{self.id}] {self.date} | {self.employee.last_name_and_initials} | {self.product.product_name} | {self.quantity} | {self.total:.2f}"

class TypeProduct(Base):
    __tablename__ = 'TypeProduct'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name = "ID")
    typeName: Mapped[String] = mapped_column(String, name = "TypeProduct")

class Product(Base):
    __tablename__ = 'Product'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name = "ID")
    type_Product_ID: Mapped[int] = mapped_column(Integer, ForeignKey(TypeProduct.ID), name = "TypeProduct")
    type_product: Mapped["TypeProduct"] = relationship("TypeProduct")
    price: Mapped[float] = mapped_column(Float, name = "Price")
    quantity: Mapped[int] = mapped_column(Integer, name = "Quantitys:")
    dateOfManufacture: Mapped[String] = mapped_column(String, name="DateOfManufacture:")
    expirationDate: Mapped[int] = mapped_column(Integer, name = "ExpirationDate:")
    provider: Mapped[int] = mapped_column(Integer, ForeignKey("Provider.ID"), name = "Provider")
    productName: Mapped[String] = mapped_column(String, name="ProductName")










    def __str__(self):
        """Функция для "красивого" отображения при отладке и не только"""
        return f"[{self.id}] {self.date} | {self.employee.last_name_and_initials} | {self.product.name} | {self.count} | {self.total:.2f}"

from enum import IntEnum
from typing import Optional

import sqlalchemy
from dataclasses import dataclass

from orm.orm_models import Base

class DatabaseType(IntEnum):
    """Тип базы данных"""
    Postgresql = 0
    MySQL = 1
    Oracle = 2
    SQLite = 3

@dataclass
class DatabaseConnectionParameters:
    Type: DatabaseType
    Database: str
    Host: Optional[str] = None
    Port: Optional[int] = None
    User: Optional[str] = None
    Password: Optional[str] = None

def create(db_param: DatabaseConnectionParameters) -> sqlalchemy.Engine | None:
    """Создание "движка" для работы с БД через ORM"""

    engine: sqlalchemy.Engine | None = None
    # В зависимости от типа базы данных, формируем строку подключения
    if db_param.Type == DatabaseType.SQLite:
        engine = sqlalchemy.create_engine(f"sqlite:///{db_param.Database}")
    elif db_param.Type == DatabaseType.Postgresql:
        engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{db_param.User}:{db_param.Password}@{db_param.Host}:{db_param.Port}/{db_param.Database}")
    elif db_param.Type == DatabaseType.MySQL:
        engine = sqlalchemy.create_engine(f"mysql+mysqlconnector://{db_param.User}:{db_param.Password}@{db_param.Host}:{db_param.Port}/{db_param.Database}")
    elif db_param.Type == DatabaseType.Oracle:
        engine = sqlalchemy.create_engine(f"oracle+oracledb://{db_param.User}:{db_param.Password}@{db_param.Host}:{db_param.Port}/?service_name={db_param.Database}")

    if engine is None:
        return None

    engine.connect()
    # На основании модели создаём все таблицы.
    Base.metadata.create_all(engine)
    return engine




___________mod
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
    year: Mapped[int] = mapped_column(Integer, name="Year", unique=True)
    quarter: Mapped[int] = mapped_column(Integer, name = "Quarter")
    revenue: Mapped[float] = mapped_column(Float, name = "Revenue")
    profit: Mapped[float] = mapped_column(Float, name = "Profit")


class Imploee(Base):
    __tablename__ = 'Imploee'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name="ID")
    lastName: Mapped[str] = mapped_column(String, name = "Lastname")
    name: Mapped[str] = mapped_column(String, name="Name")
    surName: Mapped[str] = mapped_column(String, name = "Surname")
    wasBorn: Mapped[int] = mapped_column(Integer, name = "WasBorn")
    numberPassport: Mapped[str] = mapped_column(String, name = "NumberPassport", unique=True)
    telephone: Mapped[str] = mapped_column(String, name = "NumberTelephone", unique=True)
    employment: Mapped[]

class DaySales(Base):
    __tablename__ = 'DaySales'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name="ID")
    productID: Mapped[int] = mapped_column(Integer, ForeignKey("Product.ID"), name = "Product")
    position: Mapped[product] = relationship(product)
    imploeeID: Mapped[int] = mapped_column(Integer, ForeignKey("Imploee.ID"), name = "Imploee")
    position: Mapped[imployee] = relationship("imployee")
    quantity: Mapped[int] = mapped_column(Integer, name = "Quantity")
    data: Mapped[int] = mapped_column(Integer, name = "Data")
    summ: Mapped[float]= mapped_column(Float, name = "Summ")

class TypeProduct(Base):
    __tablename__ = 'TypeProduct'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name = "ID")
    typeName: Mapped[str] = mapped_column(String, name = "TypeProduct")

class Product(Base):
    __tablename__ = 'Product'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name = "ID")
    typeProduct: Mapped[int] = mapped_column(Integer, ForeignKey(TypeProduct.ID), name = "TypeProduct")
    position: Mapped[typeProd] = relationship(typeProd)
    price: Mapped[float] = mapped_column(Float, name = "Price")
    quantitys: Mapped[int] = mapped_column(Integer, name = "Quantitys:")
    dateOfManufacture: Mapped[String] = mapped_column(String, name="DateOfManufacture:")
    expirationDate: Mapped[int] = mapped_column(Integer, name = "ExpirationDate:")
    provider: Mapped[int] = mapped_column(Integer, ForeignKey("Provider.ID"), name = "Provider")
    productName: Mapped[str] = mapped_column(String, name="ProductName")





class DqySales(Base):
    __tablename__ = 'DqySales'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name="ID")
    last_name: Mapped[String] = mapped_column(String, name="LastName")
    first_name: Mapped[String] = mapped_column(String, name="FirstName")
    middle_name: Mapped[String] = mapped_column(String, name="MiddleName", nullable=True)
    birthday: Mapped[String] = mapped_column(String, name="Birthday")
    position_id: Mapped[int] = mapped_column(Integer, ForeignKey("Positions.ID"), name="PositionId")
    position: Mapped[Position] = relationship(Position)
    phone: Mapped[String] = mapped_column(String, name="Phone")
    employment_date: Mapped[String] = mapped_column(String, name="EmploymentDate")

    @property
    def last_name_and_initials(self) -> str:
        """Для вывода фамилии и инициалов. Вида Иванов И.И."""
        return f"{self.last_name} {str(self.first_name)[0]}. {str(self.middle_name)[0]}."

    def __str__(self):
        """Функция для "красивого" отображения при отладке и не только"""
        return f"[{self.id}] {self.last_name} {self.first_name} {self.middle_name} | {self.birthday} | {self.position.name} | {self.employment_date} | {self.phone}"


class DailySale(Base):
    __tablename__ = 'DailySales'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name="ID")
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("Products.ID"), name="ProductId")
    product: Mapped[Product] = relationship(Product)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey("Employees.ID"), name="EmployeeId")
    employee: Mapped[Employee] = relationship(Employee)
    count: Mapped[int] = mapped_column(Integer, name="Count")
    date: Mapped[String] = mapped_column(String, name="Date")
    total: Mapped[float] = mapped_column(Float, name="Total")

    def __str__(self):
        """Функция для "красивого" отображения при отладке и не только"""
        return f"[{self.id}] {self.date} | {self.employee.last_name_and_initials} | {self.product.name} | {self.count} | {self.total:.2f}"



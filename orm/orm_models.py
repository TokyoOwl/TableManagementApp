from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, relationship, mapped_column

# Базовый класс. Это родительский класс для каждого класса таблицы-модели
Base = declarative_base()

class Provider(Base):
    __tablename__ = 'Поставщики'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name="ID")
    name_provider: Mapped[str] = mapped_column(String, name="Поставщик", unique=True)
    products: Mapped["Product"] = relationship("Product", back_populates= "provider")

class ResultSale(Base):
    __tablename__ = 'Результат_продаж'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name="ID")
    year: Mapped[int] = mapped_column(Integer, name="Год")
    quarter: Mapped[int] = mapped_column(Integer, name = "Квартал")
    revenue: Mapped[float] = mapped_column(Float, name = "Выручка")
    profit: Mapped[float] = mapped_column(Float, name = "Чистая_прибыль")


class Employee(Base):
    __tablename__ = 'Сотрудники'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name="ID")
    lastName: Mapped[str] = mapped_column(String, name = "Фамилия")
    name: Mapped[str] = mapped_column(String, name="Имя")
    surName: Mapped[str] = mapped_column(String, name = "Отчество")
    wasBorn: Mapped[str] = mapped_column(String, name = "Дата_рождения")
    numberPassport: Mapped[str] = mapped_column(String, name = "Номер_паспорта")
    telephone: Mapped[str] = mapped_column(String, name = "Телефон", unique=True)
    employment: Mapped[str] = mapped_column(String, name = "Прием_на_работу")
    day_sales: Mapped["DaySales"] = relationship("DaySales", back_populates= "employee")

    @property
    def last_name_and_initials(self) -> str:
        """Для вывода фамилии и инициалов. Вида Иванов И.И."""
        return f"{self.last_name} {str(self.first_name)[0]}. {str(self.middle_name)[0]}."

    def __str__(self):
        """Функция для "красивого" отображения при отладке и не только"""
        return f"[{self.id}] {self.last_name} {self.first_name} {self.middle_name} | {self.birthday} | {self.position.name} | {self.employment_date} | {self.phone}"


class DaySales(Base):
    __tablename__ = 'Суточные_продажи'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name="ID")
    productID: Mapped[int] = mapped_column(Integer, ForeignKey("Товары.ID"), name = "Товар")
    product: Mapped["Product"] = relationship("Product", back_populates= "day_sales")
    employee_ID = mapped_column(Integer, ForeignKey("Сотрудники.ID"), name = "Сотрудник")
    employee: Mapped["Employee"] = relationship("Employee", back_populates= "day_sales")
    quantity: Mapped[int] = mapped_column(Integer, name = "Количество")
    data: Mapped[str] = mapped_column(String, name = "Дата")
    summ: Mapped[float]= mapped_column(Float, name = "Сумма")


    def __str__(self):
        return f"[{self.id}] {self.date} | {self.employee.last_name_and_initials} | {self.product.product_name} | {self.quantity} | {self.total:.2f}"

class TypeProduct(Base):
    __tablename__ = 'Типы_товаров'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name = "ID")
    typeName: Mapped[str] = mapped_column(String, name = "Наименование_типа")
    products: Mapped["Product"] = relationship("Product", back_populates="type_product")

class Product(Base):
    __tablename__ = 'Товары'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, name = "ID")
    type_Product_ID: Mapped[int] = mapped_column(Integer, ForeignKey("Типы_товаров.ID"), name = "Тип_товара")
    type_product: Mapped["TypeProduct"] = relationship("TypeProduct", back_populates= "products")
    price: Mapped[float] = mapped_column(Float, name = "Цена")
    quantity: Mapped[int] = mapped_column(Integer, name = "Количество")
    dateOfManufacture: Mapped[str] = mapped_column(String, name="Дата_изготовления")
    expirationDate: Mapped[int] = mapped_column(Integer, name = "Срок_годности")
    providerID: Mapped[int] = mapped_column(Integer, ForeignKey("Поставщики.ID"), name = "Поставщик")
    provider: Mapped["Provider"] = relationship("Provider", back_populates="products")
    productName: Mapped[str] = mapped_column(String, name="Название товара")
    day_sales: Mapped["DaySales"] = relationship("DaySales", back_populates= "product")

    def __str__(self):
        """Функция для "красивого" отображения при отладке и не только"""
        return f"[{self.id}] {self.date} | {self.employee.last_name_and_initials} | {self.product.name} | {self.count} | {self.total:.2f}"

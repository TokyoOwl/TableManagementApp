from dataclasses import dataclass

@dataclass
class Provider:
    id: int = -1
    name_provider: str = ""

@dataclass
class ResultSaile:
    id: int = -1
    year: int = ""
    quarter: int = -1
    revenue: float = 0
    profit: float = 0

@dataclass
class Imploee:
    id: int = -1
    lastName: str = ""
    name: str = ""
    surName: str = ""
    wasBorn: str = ""
    numberPassport: str = ""
    telephone: str = ""
    employment: str = ""

@dataclass
class DaySales:
    id: int = -1
    product: int = 0
    imploee: int = 0
    quantity: int = 0
    data: str = ""
    summ: float = 0

@dataclass
class TypeProduct:
    id: int = -1
    typeName: str = ""

@dataclass
class Product:
    id: int = -1
    typeProduct: int = -1
    price: float = 0
    quantitys: int = 0
    dateOfManufacture: str = ""
    expirationDate: int = 0
    provider: int = 0



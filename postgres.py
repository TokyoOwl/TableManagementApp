from psycopg2 import *
from sqlalchemy import *
class PostgresDatabase:
    """
    Класс для написания логики работы с базой данных в PostgreSQL
    С помощью библиотек psycopg2 и sqlalchemy нужно реализовать все функции из файла database.py
    Все функции снизу нужно реализовать используя библиотеки psycopg2 и sqlalchemy, pass в процессе нужно удалить
    и заменить на соответствующий return (кроме функции __init__)
    Все новые библиотеки добавил в requirements.txt, не забудь их установить
    """
    def __init__(self):
        """
        Функция для инициализации подключения к базе данных
        """
        pass
    def read_positions(self):
        """
        Функция для чтения всех записей из базы
        """
        pass
    def add_position(self):
        """
        Функция для добавления записей в базы
        """
        pass
    def update_position(self):
        """
        Функция для редактирования записей из базы
        """
        pass
    def delete_position(self):
        """
        Функция для удаления записей из базы
        """
        pass
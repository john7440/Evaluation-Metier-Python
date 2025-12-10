# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""
from typing import List
import pymysql

from goncourt.daos.author_dao import AuthorDao
from goncourt.daos.selection_dao import SelectionDao
from goncourt.daos.vote_dao import VoteDao
from goncourt.daos.book_dao import BookDao
from goncourt.daos.publisher_dao import PublisherDao
from goncourt.models.book import Book

def search_by_title(self, title: str) -> List[Book]:
    """Rechercher des livres par titre """
    try:
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM book WHERE b_title LIKE %s"
            cursor.execute(sql, (f"%{title}%",))
            rows = cursor.fetchall()
            return [Book(**row) for row in rows]
    except pymysql.MySQLError as e:
        print(f"Erreur search_by_title: {e}")
        return []

def get_books_by_author(self, author_id: int) -> List[Book]:
    """Récupérer tous les livres d'un auteur"""
    try:
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM book WHERE Id_Author = %s"
            cursor.execute(sql, (author_id,))
            rows = cursor.fetchall()
            return [Book(**row) for row in rows]
    except pymysql.MySQLError as e:
        print(f"Erreur get_books_by_author: {e}")
        return []

def get_books_by_publisher(self, publisher_id: int) -> List[Book]:
    """Récupérer tous les livres d'un éditeur"""
    try:
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM book WHERE Id_Publisher = %s"
            cursor.execute(sql, (publisher_id,))
            rows = cursor.fetchall()
            return [Book(**row) for row in rows]
    except pymysql.MySQLError as e:
        print(f"Erreur get_books_by_publisher: {e}")
        return []

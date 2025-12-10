# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""
from typing import List, Optional
import pymysql  # type: ignore 

from goncourt.daos.author_dao import AuthorDao
from goncourt.daos.selection_dao import SelectionDao
from goncourt.daos.vote_dao import VoteDao
from goncourt.daos.book_dao import BookDao
from goncourt.daos.publisher_dao import PublisherDao
from goncourt.models.book import Book

# gestion des livres
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

def count_books(self) -> int:
    """Compter le nombre total de livres"""
    try:
        with self.connection.cursor() as cursor:
            sql = "SELECT COUNT(*) as total FROM book"
            cursor.execute(sql)
            row = cursor.fetchone()
            return row['total'] if row else 0
    except pymysql.MySQLError as e:
        print(f"Erreur count_books: {e}")
        return 0

## gestion des votes
def get_winner(self) -> Optional[dict]:
    """Récupérer le livre gagnant (celui avec le plus de votes)"""
    try:
        with self.connection.cursor() as cursor:
            sql = """
                SELECT b.Id_Book, b.b_title, a.a_first_name, a.a_last_name, 
                       COUNT(v.Id_Vote) AS votes
                FROM vote v
                INNER JOIN book b ON v.Id_Book = b.Id_Book
                INNER JOIN author a ON b.Id_Author = a.Id_Author
                GROUP BY b.Id_Book, b.b_title, a.a_first_name, a.a_last_name
                ORDER BY votes DESC
                LIMIT 1
            """
            cursor.execute(sql)
            return cursor.fetchone()
    except pymysql.MySQLError as e:
        print(f"Erreur get_winner: {e}")
        return None


def get_votes_by_selection(self, selection_id: int) -> str:
    """Récupérer les votes pour une sélection spécifique"""
    try:
        with self.connection.cursor() as cursor:
            sql = """
                SELECT b.b_title, COUNT(v.Id_Vote) AS votes
                FROM vote v
                INNER JOIN book b ON v.Id_Book = b.Id_Book
                INNER JOIN possess p ON b.Id_Book = p.Id_Book
                WHERE p.Id_Selection = %s
                GROUP BY b.Id_Book, b.b_title
                ORDER BY votes DESC
            """
            cursor.execute(sql, (selection_id,))
            rows = cursor.fetchall()

            if not rows:
                return f"Aucun vote pour la sélection {selection_id}"

            text = [f"=== Votes pour la sélection {selection_id} ==="]
            for r in rows:
                text.append(f"{r['b_title']} : {r['votes']} vote(s)")
            return "\n".join(text)
    except pymysql.MySQLError as e:
        print(f"Erreur get_votes_by_selection: {e}")
        return "Erreur lors de la récupération des votes"


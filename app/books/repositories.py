from abc import ABC, abstractmethod
from typing import List, Optional

from app.books.models import Book
from app.books.utils import load_books
from app.books.utils import save_books


class BaseBooksAbstractRepository(ABC):
    """
    Абстрактный базовый класс для репозитория книг.
    Определяет интерфейс для работы с книгами.
    """

    books = None

    @abstractmethod
    def add_book(self, title: str, author: str, year: int, status: str) -> Book:
        """
        Добавляет книгу в репозиторий.
        """
        pass

    @abstractmethod
    def remove_book(self, book_uuid: str) -> Optional[Book]:
        """
        Удаляет книгу из репозитория по UUID.
        """
        pass

    @abstractmethod
    def search_books(self, query: str) -> List[Book]:
        """
        Ищет книги в репозитории по запросу.
        """
        pass

    @abstractmethod
    def change_status(self, book_uuid: str, status: str) -> Optional[Book]:
        """
        Изменяет статус книги по UUID.
        """
        pass


class BooksRepository(BaseBooksAbstractRepository):
    """
    Реализация репозитория для управления книгами.
    Сохраняет данные о книгах в памяти и синхронизирует их с хранилищем.
    """

    books = load_books()

    @classmethod
    def add_book(cls, title: str, author: str, year: int, status: str) -> Book:
        """
        Добавляет книгу в репозиторий и сохраняет изменения.
        """
        book = Book(title=title, author=author, year=year, status=status)
        cls.books.append(book)
        save_books(cls.books)
        return book

    @classmethod
    def remove_book(cls, book_uuid: str) -> Optional[Book]:
        """
        Удаляет книгу из репозитория по UUID. Возвращает удаленную книгу, если она найдена.
        """
        book = next((book for book in cls.books if str(book.uuid) == book_uuid), None)
        print(book)
        if book:
            cls.books.remove(book)
            save_books(cls.books)
            return book
        return None

    @classmethod
    def search_books(cls, query: str) -> List[Book]:
        """
        Ищет книги по запросу в UUID, названию, автору или году издания.
        """
        result = []
        for book in cls.books:
            if (
                    query.lower() in book.uuid
                    or query.lower() in book.title.lower()
                    or query.lower() in book.author.lower()
                    or query in str(book.year)
            ):
                result.append(book)
        return result

    @classmethod
    def change_status(cls, book_uuid: str, new_status: str) -> Optional[Book]:
        """
        Изменяет статус книги по UUID. Возвращает обновленную книгу, если она найдена.
        """
        book = next((book for book in cls.books if str(book.uuid) == book_uuid), None)
        if book:
            book.status = new_status
            save_books(cls.books)
            return book
        return None

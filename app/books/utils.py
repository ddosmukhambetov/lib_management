import json
from typing import List

from app.books.models import Book
from app.core.config import settings


def load_books(file_path: str = settings.books.path_to_save_books) -> List[Book]:
    """
    Загружает список книг из файла JSON.

    :param file_path: Путь к файлу с книгами. По умолчанию используется путь из настроек.
    :return: Список объектов Book.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            books_data = json.load(file)
            return [Book.from_dict(data) for data in books_data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_books(books: List[Book], file_path: str = settings.books.path_to_save_books) -> None:
    """
    Сохраняет список книг в файл JSON.

    :param books: Список объектов Book для сохранения.
    :param file_path: Путь к файлу для сохранения. По умолчанию используется путь из настроек.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump([book.as_dict() for book in books], file, indent=4, ensure_ascii=False)

import uuid
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Book:
    """
    Модель книги с информацией о названии, авторе, году издания, статусе и уникальном идентификаторе.
    """
    title: str
    author: str
    year: int
    status: str
    uuid: str = field(default_factory=lambda: uuid.uuid4().hex)

    def as_dict(self) -> Dict:
        """
        Преобразует объект книги в словарь.

        :return: Словарь с атрибутами книги.
        """
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status,
            'uuid': self.uuid,
        }

    @classmethod
    def from_dict(cls, data) -> 'Book':
        """
        Создает объект книги из словаря.

        :param data: Словарь с данными о книге.
        :return: Экземпляр класса Book.
        """
        return cls(
            title=data['title'],
            author=data['author'],
            year=data['year'],
            status=data['status'],
            uuid=data['uuid'],
        )

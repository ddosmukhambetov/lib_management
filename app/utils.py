import json
from typing import List, TypeVar, Type

T = TypeVar('T')


def load_data(file_path: str, cls: Type[T]) -> List[T]:
    """
    Загружает список объектов из файла JSON.

    :param file_path: Путь к файлу с данными.
    :param cls: Класс, из которого нужно создать объекты.
    :return: Список объектов типа cls.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [cls.from_dict(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(data: List[T], file_path: str) -> None:
    """
    Сохраняет список объектов в файл JSON.

    :param data: Список объектов для сохранения.
    :param file_path: Путь к файлу для сохранения.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump([item.as_dict() for item in data], file, indent=4, ensure_ascii=False)

import pathlib

base_dir = pathlib.Path(__file__).resolve().parent.parent.parent


class BooksConfig:
    """
    Конфигурация для работы с книгами.
    Содержит пути для хранения данных и гарантирует наличие каталога для данных.
    """
    data_dir = base_dir / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)

    @property
    def path_to_save_books(self) -> pathlib.Path:
        """
        Возвращает путь к файлу для сохранения данных о книгах.
        """
        return self.data_dir / 'books.json'


class Settings:
    """
    Основной класс настроек приложения.
    """
    books: BooksConfig = BooksConfig()


settings = Settings()

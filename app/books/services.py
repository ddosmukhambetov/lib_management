from datetime import datetime

from app.books.repositories import BaseBooksAbstractRepository


class BooksService:
    """
    Сервис для управления книгами, который предоставляет методы взаимодействия с репозиторием книг.
    """

    def __init__(self, repository: BaseBooksAbstractRepository) -> None:
        self.repository = repository

    def display_all_books(self) -> None:
        """
        Отображает все книги из репозитория.
        """
        if not self.repository.books:
            print('В библиотеке нет книг!')
            return

        for i, book in enumerate(self.repository.books, start=1):
            print(
                f'{i}. '
                f'UUID: {book.uuid} | '
                f'Название: {book.title} | '
                f'Автор: {book.author} | '
                f'Год: {book.year} | '
                f'Статус: {book.status}'
            )

    def add_book_interactive(self):
        """
        Интерактивное добавление книги в репозиторий через ввод пользователя.
        """
        while True:
            title = input('Введите название книги: ').strip()
            if not title:
                print('Название книги не может быть пустым!')
                continue

            author = input('Введите автора книги: ').strip()
            if not author:
                print('Автор книги не может быть пустым!')
                continue

            year = input('Введите год издания книги: ')
            if not year.isdigit():
                print('Год издания книги должен быть числом!')
                continue
            elif int(year) > datetime.now().year:
                print('Год издания книги не может быть больше текущего года!')
                continue

            status = input('Введите статус книги (в наличии/нет в наличии или 1/0): ').lower()
            if status == '1' or status == 'в наличии':
                status = 'в наличии'
            elif status == '0' or status == 'нет в наличии':
                status = 'нет в наличии'
            else:
                print('Неверный статус книги! Введите в наличии или нет в наличии или 1/0.')
                continue

            book = self.repository.add_book(title, author, int(year), status)
            print(f'Книга {book.title} добавлена в библиотеку.')
            break

    def remove_book_interactive(self) -> None:
        """
        Интерактивное удаление книги из репозитория по UUID.
        """
        book_uuid = input('Введите UUID книги для удаления: ')
        removed_book = self.repository.remove_book(book_uuid)
        if removed_book:
            print(f'Книга {removed_book.title} удалена.')
        else:
            print(f'Книга с UUID {book_uuid} не найдена!')

    def search_books_interactive(self) -> None:
        """
        Интерактивный поиск книг в репозитории по UUID, названию, автору или году.
        """
        query = input('Введите текст для поиска (по UUID, названию, автору или году): ')
        results = self.repository.search_books(query)
        if results:
            print('Найденные книги:')
            for i, book in enumerate(results, start=1):
                print(
                    f'{i}. '
                    f'UUID: {book.uuid} | '
                    f'Название: {book.title} | '
                    f'Автор: {book.author} | '
                    f'Год: {book.year} | '
                    f'Статус: {book.status}'
                )
        else:
            print('Книги по запросу не найдены!')

    def change_status_interactive(self) -> None:
        """
        Интерактивное изменение статуса книги по UUID.
        """
        book_uuid = input('Введите UUID книги для изменения статуса: ')
        new_status = input('Введите новый статус (в наличии/нет в наличии или 1/0): ').strip().lower()

        if new_status == '1' or new_status == 'в наличии':
            new_status = 'в наличии'
        elif new_status == '0' or new_status == 'нет в наличии':
            new_status = 'нет в наличии'
        else:
            print('Неверный статус! Введите в наличии или нет в наличии или 1/0.')
            return

        updated_book = self.repository.change_status(book_uuid, new_status)
        if updated_book:
            print(f'Статус книги {updated_book.title} изменен на {new_status}.')
        else:
            print(f'Книга с ID {book_uuid} не найдена!')

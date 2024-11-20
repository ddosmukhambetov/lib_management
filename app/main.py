import sys

from app.books.repositories import BooksRepository
from app.books.services import BooksService


def main() -> None:
    """
    Запускает консольное приложение для управления книгами.
    Предоставляет меню для добавления, удаления, поиска, просмотра и изменения статуса книг.
    Завершение программы осуществляется по выбору пункта "Выход".
    """
    repository = BooksRepository()
    service = BooksService(repository)

    while True:
        print('\nМеню:')
        print('1. Добавить книгу')
        print('2. Удалить книгу')
        print('3. Поиск книг')
        print('4. Список всех книг')
        print('5. Изменить статус книги')
        print('6. Выход')

        choice = input('Выберите действие (1-6): ')

        if choice == '1':
            service.add_book_interactive()
        elif choice == '2':
            service.remove_book_interactive()
        elif choice == '3':
            service.search_books_interactive()
        elif choice == '4':
            service.display_all_books()
        elif choice == '5':
            service.change_status_interactive()
        elif choice == '6':
            print('Выход из программы.')
            sys.exit(0)
        else:
            print('Неверный выбор. Попробуйте снова!')


if __name__ == '__main__':
    main()

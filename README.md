# Библиотечная система

Проект представляет собой простую библиотечную систему для управления книгами. Она позволяет добавлять, удалять,
изменять статус и искать книги. Реализованы основные функции управления книгами с использованием JSON-файлов для
хранения данных.

## Описание

Система управления библиотекой включает в себя следующие функции:

- Добавление книг.
- Удаление книг.
- Поиск книг по UUID, названию, автору или году.
- Изменение статуса книг (например, "в наличии" или "нет в наличии").
- Сохранение данных о книгах в JSON-файл.

## Установка

- Клонируйте репозиторий: ```git clone https://github.com/ddosmukhambetov/lib_management.git```
- Перейдите в директорию проекта: ```cd lib_management```

## Запуск

- Сторонние библиотеки не были использованы, так что можно запускать сразу, без создания виртуального окружения
- Чтобы запустить систему, выполните следующий командой: ```python -m app.main```
- При запуске приложение предложит интерактивное меню для управления книгами.

## Использование

Когда приложение запущено, вы увидите следующее меню:

    1. Добавить книгу
    2. Удалить книгу
    3. Поиск книг
    4. Список всех книг
    5. Изменить статус книги
    6. Выход

Выберите действие, введя соответствующий номер:

    1. Добавить книгу — добавление книги в библиотеку (вам нужно будет ввести название, автора, год издания и статус).
    2. Удалить книгу — удаление книги по UUID.
    3. Поиск книг — поиск книг по UUID, названию, автору или году.
    4. Список всех книг — вывод всех книг в библиотеке.
    5. Изменить статус книги — изменение статуса книги (например, "в наличии" или "нет в наличии").
    6. Выход — выход из программы.

#### Во всех функциях написаны комментарии, чтобы легче понять, что делает программа.
# qa_python

В проекте содержатся:
- файл main.py, где хранится класс, который нужно протестировать, и его методы
- файл tests.py, в котором содержится тестовый класс и его методы
- файл conftest.py, в котором содержится фикстура, которая создаёт объект класса BooksCollector

Чтобы запустить тесты, нужно:
- нажать на зелёную стрелочку рядом с классом TestBooksCollector 

Список тестов:
- test_init_success проверяет, правильно ли создаётся экземпляр класса BooksCollector
- test_add_new_book_book_added проверяет, добавилась ли книга
- test_set_book_genre_genre_is_set проверяет, получилось ли задать жанр книге
- test_get_book_genre_shows_genre проверяет, можно ли по названию книги получить её жанр
- test_get_books_with_specific_genre_shows_books проверяет, можно ли получить книги конкретного жанра по его названию
- test_get_books_genre_is_dict проверяет,является ли словарь книг и жанров словарём
- test_get_books_for_children_returns_safe_books проверяет, возвращает ли метод книги не относящиесяк жанрам "Детективы" и "Ужасы"
- test_add_book_in_favorites_is_added проверяет успешное добавление книги в избранное по названию
- test_delete_book_from_favorites_is_deleted проверяет успешное удаление книги из избранного
- test_get_list_of_favorites_books_returns_favorites проверяет, что метод возвращает избранное

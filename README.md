1.test_add_new_book_add_two_different_books
Добавляем 2 различные книги и смотрим, что длина полученного словаря 2

2.test_add_new_book_add_identical_books
Добавляем 2 одинаковые книги и смотрим, что длина полученного словаря не равно 2. Добавилась только одна книга

3.test_add_new_book_more_fourty_symbols_max
Проверяем, что книги с пустым названием и с названием больше 40 символов не добавляются в словарь

4.test_set_book_genre_setting_book_genre
Проверяем, что созданной книге в словаре добавляется жанр

5.test_get_book_genre_return_existing_name
Проверяем, что жанр книги соответствует имени созданной книги

6.test_get_books_with_specific_genre_return_list
Проверяем, что books_with_specific_genre имеет формат list(список)

7.test_get_books_genre_return_dict
Проверяем, что books_genre имеет формат dict(словарь)

8.test_get_books_for_children_return_books_kids
Проверяем, что из 2х доблавленных книг, метод возвращает только книгу с жанром для детей

9.test_add_book_in_favorites_add_one_book
Проверям, что в списке избранных появилась новая добавленная книга

10.test_delete_book_from_favorites_empty_list
Проверяем, что удаленной книги нет в избранных и список пустой

11.test_get_list_of_favorites_books_empty_list
Проверяем, что список избранных пустой, если ни каких действий с ним не производилось

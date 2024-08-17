import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_different_books(self, collector):
        collector.add_new_book('Метро')
        collector.add_new_book('Остров')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_identical_books(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')

        assert len(collector.get_books_genre()) != 2

    @pytest.mark.parametrize('name', ['', 'Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции'])
    def test_add_new_book_more_fourty_symbols_max(self, collector, name):
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('name,genre', [
        ['Сказка о царе Салтане', 'Мультфильмы'],
        ['Властелин колец', 'Фантастика']
    ])
    def test_set_book_genre_setting_book_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre[name] == genre

    def test_get_book_genre_return_existing_name(self, collector):
        collector.add_new_book('Метро')
        collector.set_book_genre('Метро', 'Фантастика')

        assert collector.get_book_genre('Метро') == 'Фантастика'

    def test_get_books_with_specific_genre_return_list(self, collector):
        collector.add_new_book('Дядя Стёпа')
        collector.set_book_genre('Дядя Стёпа', 'Мультфильмы')

        assert type(collector.get_books_with_specific_genre('Мультфильмы')) == list

    def test_get_books_genre_return_dict(self, collector):
        collector.add_new_book('Дядя Стёпа')
        collector.set_book_genre('Дядя Стёпа', 'Мультфильмы')

        assert type(collector.get_books_genre()) == dict

    def test_get_books_for_children_return_books_kids(self, collector):
        collector.add_new_book('Дядя Стёпа')
        collector.set_book_genre('Дядя Стёпа', 'Мультфильмы')
        collector.add_new_book('Зеркало')
        collector.set_book_genre('Зеркало', 'Ужасы')
        assert collector.get_books_for_children() == ['Дядя Стёпа']

    def test_add_book_in_favorites_add_one_book(self, collector):
        book_add = 'Война и мир'
        collector.add_new_book(book_add)
        collector.add_book_in_favorites(book_add)

        assert collector.get_list_of_favorites_books() == [book_add]

    def test_delete_book_from_favorites_empty_list(self, collector):
        book_del = 'Отцы и дети'
        collector.add_new_book(book_del)
        collector.add_book_in_favorites(book_del)
        collector.delete_book_from_favorites(book_del)

        assert book_del not in collector.favorites and collector.favorites == []

    def test_get_list_of_favorites_books_empty_list(self, collector):
        assert collector.get_list_of_favorites_books() == []

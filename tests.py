from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # проверить, что при добавлении книге присвоен рейтинг 1 по дефолту
    def test_add_new_book_rating_default_one_positive_result(self):
        collector = BooksCollector()

        collector.add_new_book('Властелин колец')

        act_result = collector.books_rating['Властелин колец']
        exp_result = 1

        assert act_result == exp_result

    # проверить, что рейтинг 5 (позитивное значение диапазона 1 до 10) передается в список books_rating
    def test_set_book_rating_five_positive_result(self):
        collector = BooksCollector()

        collector.add_new_book('Великий Гэтсби')
        collector.set_book_rating('Великий Гэтсби', 5)

        act_result = collector.books_rating['Великий Гэтсби']
        exp_result = 5

        assert act_result == exp_result

    # проверить получение рейтинга книги по имени
    def test_get_book_rating_by_name_positive_result(self):
        collector = BooksCollector()

        collector.add_new_book('Голодные игры')
        collector.set_book_rating('Голодные игры', 5)

        act_result = collector.get_book_rating('Голодные игры')
        exp_result = 5

        assert act_result == exp_result

    # проверить получение списка книг с указанным рейтингом = 1 (граничное значение диапазона рейтинга от 1 до 10)
    def test_get_books_with_specific_rating_one_positive_result(self):
        collector = BooksCollector()

        collector.add_new_book('О дивный новый мир')
        collector.set_book_rating('О дивный новый мир', 1)

        collector.add_new_book('Маленький принц')
        collector.set_book_rating('Маленький принц', 9)

        collector.add_new_book('Виноваты звёзды')
        collector.set_book_rating('Виноваты звёзды', 1)

        act_result = collector.get_books_with_specific_rating(1)
        exp_result = ['О дивный новый мир', 'Виноваты звёзды']

        assert act_result == exp_result

    # проверить получение 2-х книг из словаря books_rating
    def test_get_books_rating_two_books_positive_result(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_rating('Гарри Поттер и философский камень', 9)

        collector.add_new_book('Гарри Поттер и Тайная комната')
        collector.set_book_rating('Гарри Поттер и Тайная комната', 7)

        act_result = collector.get_books_rating()
        exp_result = {'Гарри Поттер и философский камень': 9, 'Гарри Поттер и Тайная комната': 7}

        assert act_result == exp_result

        # проверить добавление книги в избранное
    def test_add_book_in_favorites_one_book_positive_result(self):
        collector = BooksCollector()

        collector.add_new_book('Идиот')
        collector.set_book_rating('Идиот', 10)
        collector.add_book_in_favorites('Идиот')

        act_result = collector.favorites
        exp_result = ['Идиот']

        assert act_result == exp_result

    # проверить удаление книги из избранного
    def test_delete_book_from_favorites_one_book_positive_result(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.set_book_rating('1984', 10)
        collector.add_book_in_favorites('1984')

        collector.add_new_book('Убить пересмешника')
        collector.set_book_rating('Убить пересмешника', 8)
        collector.add_book_in_favorites('Убить пересмешника')

        collector.delete_book_from_favorites('1984')

        act_result = collector.favorites
        exp_result = ['Убить пересмешника']

        assert act_result == exp_result

    # проверить получение списка избранных книг
    def test_get_list_of_favorites_books_two_book_positive_result(self):
        collector = BooksCollector()

        collector.add_new_book('451° по Фаренгейту')
        collector.set_book_rating('451° по Фаренгейту', 9)
        collector.add_book_in_favorites('451° по Фаренгейту')

        collector.add_new_book('Скотный двор')
        collector.set_book_rating('Скотный двор', 10)
        collector.add_book_in_favorites('Скотный двор')

        act_result = collector.get_list_of_favorites_books()
        exp_result = ['451° по Фаренгейту', 'Скотный двор']
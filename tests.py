class TestBooksCollector:

    def test_init_success(self, collector):
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_book_added(self,collector):
        collector.add_new_book("Магистр дьявольского культа")
        assert "Магистр дьявольского культа" in collector.books_genre

    def test_set_book_genre_genre_is_set(self, collector):
        collector.add_new_book("Магистр дьявольского культа")
        collector.set_book_genre("Магистр дьявольского культа", "Фантастика")
        assert collector.books_genre["Магистр дьявольского культа"] == "Фантастика"

    def test_get_book_genre_shows_genre(self, collector):
        collector.add_new_book("Магистр дьявольского культа")
        collector.set_book_genre("Магистр дьявольского культа", "Фантастика")
        assert collector.get_book_genre("Магистр дьявольского культа") == "Фантастика"

    def test_get_books_with_specific_genre_shows_books(self, collector):
        collector.add_new_book("Магистр дьявольского культа")
        collector.set_book_genre("Магистр дьявольского культа", "Фантастика")
        collector.add_new_book("Благие знамения")
        collector.set_book_genre("Благие знамения", "Комедии")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Магистр дьявольского культа"]

    def test_get_books_genre_returns_book_and_genre(self, collector):
        collector.add_new_book("Магистр дьявольского культа")
        collector.set_book_genre("Магистр дьявольского культа", "Фантастика")
        assert collector.get_books_genre() == {"Магистр дьявольского культа": "Фантастика"}

    def test_get_books_for_children_returns_safe_books(self,collector):
        collector.add_new_book("Магистр дьявольского культа")
        collector.set_book_genre("Магистр дьявольского культа", "Фантастика")
        collector.add_new_book("Токийский зодиак")
        collector.set_book_genre("Токийский зодиак", "Детективы")
        collector.add_new_book("Мизери")
        collector.set_book_genre("Мизери", "Ужасы")
        assert "Мизери", "Токийский зодиак" not in collector.get_books_for_children()

    def test_add_book_in_favorites_is_added(self, collector):
        collector.add_new_book("Магистр дьявольского культа")
        collector.add_book_in_favorites("Магистр дьявольского культа")
        assert "Магистр дьявольского культа" in collector.favorites

    def test_delete_book_from_favorites_is_deleted(self, collector):
        collector.add_new_book("Магистр дьявольского культа")
        collector.add_book_in_favorites("Магистр дьявольского культа")
        collector.delete_book_from_favorites("Магистр дьявольского культа")
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_returns_favorites(self, collector):
        collector.add_new_book("Магистр дьявольского культа")
        collector.add_book_in_favorites("Магистр дьявольского культа")
        assert "Магистр дьявольского культа" in collector.get_list_of_favorites_books()
from dao.model.movie import Movie


class MovieDAO:
    """
    Класс ДАО для сущности Movie.

    В поля класса добавляем сессию подключения.
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """
        Метод для получения списка всех фильмов.
        """
        return self.session.query(Movie).all()

    def get_one(self, mid):
        """
        Метод для получения фильма по его id.
        """
        return self.session.query(Movie).get(mid)

    def get_by_did(self, did):
        """
        Метод получения списка фильмов по id режиссера.
        """
        return self.session.query(Movie).filter(Movie.director_id == int(did)).all()

    def get_by_gid(self, gid):
        """
        Метод получения списка фильмов по id жанра.
        """
        return self.session.query(Movie).filter(Movie.genre_id == int(gid)).all()

    def get_by_year(self, year):
        """
        Метод получения списка фильмов по году выпуска.
        """
        return self.session.query(Movie).filter(Movie.year == int(year)).all()

    def create(self, data):
        """
        Метод для создания и добавления нового фильма в список.
        """
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        """
        Метод добавления обновленного фильма.
        """
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        """
        Метод для удаления фильма по его id.
        """
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()

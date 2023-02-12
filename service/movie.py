from dao.movie import MovieDAO


class MovieService:
    """
    Класс сервис для сущности Movie.

    В поля класса добавляем объект ДАО.
    """
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        """
        Метод получения списка всех фильмов через обращение к ДАО.
        """
        return self.dao.get_all()

    def get_one(self, mid):
        """
        Метод получения фильма по его id через обращение к ДАО.
        """
        return self.dao.get_one(mid)

    def create(self, data):
        """
        Метод создания фильма через обращение к ДАО.
        """
        return self.dao.create(data)

    def update(self, data):
        """
        Метод для полного обновления данных фильма.

        На основе полученных данных получаем фильм по его id через обращение к ДАО.
        Обновляем запись и добавляем в список через обращение к ДАО.
        """
        mid = data.get('id')

        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        self.dao.update(movie)

    def update_partial(self, data):
        """
        Метод частичного обновления данных фильма.

        На основе полученных данных получаем фильм по его id через обращение к ДАО.
        Обновляем запись в соответствии с полученными данными и добавляем в список через обращение к ДАО.
        """
        mid = data.get('id')

        movie = self.get_one(mid)

        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        if 'director_id' in data:
            movie.director_id = data.get('director_id')

        self.dao.update(movie)

    def delete(self, mid):
        """
        Метод удаления фильма по его id через обращение к ДАО.
        """
        self.dao.delete(mid)

    def get_by_did(self, did):
        """
        Метод получения фильма по id режиссера через обращение к ДАО.
        """
        return self.dao.get_by_did(did)

    def get_by_gid(self, gid):
        """
        Метод получения фильма по id жанра через обращение к ДАО.
        """
        return self.dao.get_by_gid(gid)

    def get_by_year(self, year):
        """
        Метод получения фильма по году выпуска через обращение к ДАО.
        """
        return self.dao.get_by_year(year)

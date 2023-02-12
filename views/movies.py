from flask import request  # Импортируем необходимые пакеты, модули и т.д.
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema  # Импортируем схему для сериализации/десериализации.
from implemented import movie_service  # Импортируем сервис.

movie_ns = Namespace('movies')  # Создаем неймспейс.

movie_schema = MovieSchema()  # Объявляем переменные для обращения к схемам сериализации/десериализации.
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')  # Представление по маршруту /movies/
class MoviesView(Resource):
    """
    Класс представления для сущностей movies.
    """
    def get(self):
        """
        Метод get.

        Возвращает данные на основе запроса.
        По маршруту /movies/ возвращает список всех фильмов.
        Если в запросе указан 'director_id', возвращает список фильмов с указанным режиссером.
        Если в запросе указан 'genre_id', возвращает список фильмов с указанным жанром.
        Если в запросе указан 'year', возвращает список фильмов выпущенных в указанном году.
        Данные получает через обращение к сервису.
        """
        did = request.args.get('director_id')
        gid = request.args.get('genre_id')
        year = request.args.get('year')

        if did is None and gid is None and year is None:
            result = movie_service.get_all()
            if result:
                return movies_schema.dump(result), 200
            else:
                return "Данные не найдены", 404

        elif did and gid is None and year is None:
            result = movie_service.get_by_did(did)
            if result:
                return movies_schema.dump(result), 200
            else:
                return "Данные не найдены", 404

        elif gid and did is None and year is None:
            result = movie_service.get_by_gid(gid)
            if result:
                return movies_schema.dump(result), 200
            else:
                return "Данные не найдены", 404

        elif year and gid is None and did is None:
            result = movie_service.get_by_year(year)
            if result:
                return movies_schema.dump(result), 200
            else:
                return "Данные не найдены", 404

    def post(self):
        """
        Метод post.

        На основе полученных данных создаем фильм и добавляем его в список через обращение к сервису.
        """
        try:
            data = request.json
            movie_service.create(data)
            return '', 201
        except Exception as e:
            return str(e), 404


@movie_ns.route('/<int:mid>')  # Представление по маршруту /movies/mid
class MovieView(Resource):
    """
    Класс представление для сущности movie.
    """
    def get(self, mid):
        """
        Метод get.

        Через обращение к сервису получает и возвращает фильм по его id.
        """
        result = movie_service.get_one(mid)
        if result:
            return movie_schema.dump(result), 200
        else:
            return "Данные не найдены", 404

    def put(self, mid):
        """
        Метод put.

        Получает данные и передает их сервису для обновления данных о фильме.
        """
        try:
            data = request.json
            data['id'] = mid
            movie_service.update(data)
            return '', 204
        except Exception as e:
            return str(e), 404

    def delete(self, mid):
        """
        Метод delete.

        Обращается к сервису для удаления фильма по его id.
        """
        try:
            movie_service.delete(mid)
            return '', 204
        except Exception as e:
            return str(e), 404

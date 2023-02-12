from flask_restx import Resource, Namespace  # Импортируем необходимые пакеты, модули и т.д.

from dao.model.genre import GenreSchema  # Импортируем схему для сериализации/десериализации.
from implemented import genre_service  # Импортируем сервис.

genre_ns = Namespace('genres')  # Создаем неймспейс.

genre_schema = GenreSchema()  # Объявляем переменные для обращения к схемам сериализации/десериализации.
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')  # Представление по маршруту /genres/
class GenresView(Resource):
    """
    Класс представления для сущностей genres.
    """
    def get(self):
        """
        Метод get.

        Через обращение к сервису получает и возвращает список всех жанров.
        """
        result = genre_service.get_all()
        if result:
            return genres_schema.dump(result), 200
        else:
            return "Данные не найдены", 404


@genre_ns.route('/<int:gid>')  # Представление по маршруту /genres/gid
class GenreView(Resource):
    """
    Класс представления для сущности genre.
    """
    def get(self, gid):
        """
        Метод get.

        Через обращение к сервису получает и возвращает жанр по его id.
        """
        result = genre_service.get_one(gid)
        if result:
            return genre_schema.dump(result), 200
        else:
            return "Данные не найдены", 404

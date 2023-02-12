from flask_restx import Namespace, Resource  # Импортируем необходимые пакеты, модули и т.д.

from dao.model.director import DirectorSchema  # Импортируем схему для сериализации/десериализации.
from implemented import director_service  # Импортируем сервис.

director_ns = Namespace('directors')  # Создаем неймспейс.

director_schema = DirectorSchema()  # Объявляем переменные для обращения к схемам сериализации/десериализации.
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')  # Представление по маршруту /directors/
class DirectorsView(Resource):
    """
    Класс представления для сущностей directors.
    """
    def get(self):
        """
        Метод get.

        Через обращение к сервису получает и возвращает список всех режиссеров.
        """
        result = director_service.get_all()
        if result:
            return directors_schema.dump(result), 200
        else:
            return "Данные не найдены", 404


@director_ns.route('/<int:did>')  # Представление по маршруту /directors/did
class DirectorView(Resource):
    """
    Класс представления для сущности director.
    """
    def get(self, did):
        """
        Метод get.

        Через обращение к сервису получает и возвращает режиссера по его id.
        """
        result = director_service.get_one(did)
        if result:
            return director_schema.dump(result), 200
        else:
            return "Данные не найдены", 404

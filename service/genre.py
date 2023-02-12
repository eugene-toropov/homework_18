from dao.genre import GenreDAO


class GenreService:
    """
    Класс сервис для сущности Genre.

    В поля класса добавляем объект ДАО.
    """
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        """
        Метод для получения списка всех жанров через обращение к ДАО.
        """
        return self.dao.get_all()

    def get_one(self, gid):
        """
        Метод получения жанра по его id через обращение к ДАО.
        """
        return self.dao.get_one(gid)

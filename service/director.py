from dao.director import DirectorDAO


class DirectorService:
    """
    Класс сервис для сущности Director.

    В поля класса добавляем объект ДАО.
    """
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        """
        Метод для получения списка всех режиссеров через обращение к ДАО.
        """
        return self.dao.get_all()

    def get_one(self, did):
        """
        Метод получения режиссера по его id через обращение к ДАО.
        """
        return self.dao.get_one(did)

from dao.model.director import Director


class DirectorDAO:
    """
    ДАО класс для сущности Director.

    В поля класса добавляем сессию подключения.
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """
        Метод вызова списка всех режиссеров.
        """
        return self.session.query(Director).all()

    def get_one(self, did):
        """
        Метод вызова режиссера по его id.
        """
        return self.session.query(Director).get(did)

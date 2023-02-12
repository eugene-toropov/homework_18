from dao.model.genre import Genre


class GenreDAO:
    """
    ДАО класс для сущности Genre.

    В поля класса добавляем сессию подключения.
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """
        Метод вызова списка всех жанров.
        """
        return self.session.query(Genre).all()

    def get_one(self, gid):
        """
        Метод вызова жанра по его id.
        """
        return self.session.query(Genre).get(gid)

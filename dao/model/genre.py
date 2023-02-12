from setup_db import db
from marshmallow import Schema, fields


class Genre(db.Model):
    """
    Класс/модель ДБ 'Genre'.
    Прописываем поля класса: id, name.
    """
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """
        Схема сериализации/десериализации для класса 'Genre'.
        На основе полей класса 'Genre' создаем схему с указанием типа данных.
        """
    id = fields.Int()
    name = fields.Str()

from setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
    """
    Класс/модель ДБ 'Director'.
    Прописываем поля класса: id, name.
    """
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    """
        Схема сериализации/десериализации для класса 'Director'.
        На основе полей класса 'Director' создаем схему с указанием типа данных.
        """
    id = fields.Int()
    name = fields.Str()

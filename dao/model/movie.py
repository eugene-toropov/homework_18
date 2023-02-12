from setup_db import db
from marshmallow import Schema, fields


class Movie(db.Model):
    """
    Класс/модель ДБ 'Movie'.
    Прописываем поля класса: id, title, description, trailer, year, rating, genre_id, director_id.
    """
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.String(200))
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    """
    Схема сериализации/десериализации для класса 'Movie'.
    На основе полей класса 'Movie' создаем схему с указанием типа данных.
    """
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Str()
    genre_id = fields.Int()
    director_id = fields.Int()

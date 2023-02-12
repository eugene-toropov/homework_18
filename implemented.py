from dao.director import DirectorDAO  # Импортируем необходимые библиотеки, модули, пакеты, константы и т.д.
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup_db import db

movie_dao = MovieDAO(db.session)  # Создаем переменную для работы с MovieDAO
movie_service = MovieService(dao=movie_dao)  # Создаем переменную для работы с MovieService

genre_dao = GenreDAO(db.session)  # Создаем переменную для работы с GenreDAO
genre_service = GenreService(dao=genre_dao)  # Создаем переменную для работы с GenreService

director_dao = DirectorDAO(db.session)  # Создаем переменную для работы с DirectorDAO
director_service = DirectorService(dao=director_dao)  # Создаем переменную для работы с DirectorService

from unittest.mock import MagicMock
import pytest
from app.dao.models.movie import Movie
from app.dao.movie import MovieDAO
from app.service.movie import MovieService

@pytest.fixture()
def movie_dao():
   movie_dao = MovieDAO(None)

   Tom = Movie(id=1, title="one", description="text", trailer="wow", year=1991, rating=1.2 )
   Kat = Movie(id=2, title="three", description="text", trailer="wow", year=2005, rating=9.0 )
   Steve = Movie(id=3, title="four", description="text", trailer="wow", year=2021, rating=11.0)

   movie_dao.get_all = MagicMock(return_value=[Tom, Kat, Steve])
   movie_dao.get_one = MagicMock(return_value=Tom)
   movie_dao.create = MagicMock(return_value=Movie(id=3))
   movie_dao.delete = MagicMock()
   movie_dao.update = MagicMock()

   return movie_dao


class TestMovieService:
   @pytest.fixture(autouse=True)
   def movie_service(self,movie_dao):
      self.movie_service = MovieService(dao=movie_dao)

   def test_movie_get_one(self):
      movie = self.movie_service.get_one(1)

      assert movie is not None
      assert movie.id is not None

   def test_movie_get_all(self):
      movies = self.movie_service.get_all()

      assert len(movies) > 0 

   def test_movie_create(self):
      movie_req = {

         "id":1,
         "title":"OMG",
         "description":"text",
         "trailer":"free",
         "year":2000,
         "rating":1.0,
         "genre_id":1,
         "director_id":1

      }

      movie = self.movie_service.create(movie_req)
      assert movie.id is not None

   def test_movie_delete(self):
      self.movie_service.delete(1)

   def test_movie_update(self):
      movie_req = {

         "id":1,
         "title":"OMG",
         "description":"text",
         "trailer":"Woooow",
         "year":1999,
         "rating":1.0,
         "genre_id":4,
         "director_id":3

      }

      self.movie_service.update(movie_req)

      
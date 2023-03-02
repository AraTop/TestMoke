from unittest.mock import MagicMock
import pytest
from app.dao.models.genre import Genre
from app.dao.genre import GenreDAO
from app.service.genre import GenreService

@pytest.fixture()
def genre_dao():
   genre_dao = GenreDAO(None)

   Tom = Genre(id=1, name="Tom")
   Kat = Genre(id=1, name="Kat")
   Steve = Genre(id=1, name="Steve")

   genre_dao.get_all = MagicMock(return_value=[Tom, Kat, Steve])
   genre_dao.get_one = MagicMock(return_value=Tom)
   genre_dao.create = MagicMock(return_value=Genre(id=3))
   genre_dao.delete = MagicMock()
   genre_dao.update = MagicMock()

   return genre_dao


class TestGenreService:
   @pytest.fixture(autouse=True)
   def genre_service(self,genre_dao):
      self.genre_service = GenreService(dao=genre_dao)

   def test_genre_get_one(self):
      genre = self.genre_service.get_one(1)

      assert genre is not None
      assert genre.id is not None

   def test_genre_get_all(self):
      genre = self.genre_service.get_all()

      assert len(genre) > 0 

   def test_genre_create(self):
      genre_req = {
         "name": "ara"
      }

      genre = self.genre_service.create(genre_req)
      assert genre.id is not None

   def test_genre_delete(self):
      self.genre_service.delete(1)

   def test_genre_update(self):
      genre_req = {

         "id":1,
         "name":"Vanya"

      }

      self.genre_service.update(genre_req)

      
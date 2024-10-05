import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import tmdb_client
import requests
from app.main import app
from unittest.mock import Mock

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()


def some_function_to_mock():
   raise Exception("Original was called")

def test_mocking():
   result = some_function_to_mock()

def test_mocking(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = 2
   monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
   result = some_function_to_mock()
   assert result == 2


def test_get_poster_url_uses_default_size():
   # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   
   # Porównanie wyników
   assert expected_default_size in poster_url
   #assert poster_url == "https://image.tmdb.org/t/p/w342/some-poster-path"

def get_movies_list(list_type):
   return call_tmdb_api(f"movie/{list_type}")

def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None

def test_get_movies_list(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .son()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list



# zadanie Stwórz testy jednostkowe dla Twojej biblioteki filmów. Przetestuj funkcje takie jak get_single_movie, get_movie_images, get_single_movie_cast.

# Test funkcji get_single_movie
def test_get_single_movie(monkeypatch):
   # Przygotowanie danych
   mock_movie_data = {"title": "Test Movie"}

   # Mock dla funkcji requests.get
   mock_requests_get = Mock()
   mock_response = Mock()
   mock_response.json.return_value = mock_movie_data
   mock_requests_get.return_value = mock_response

   monkeypatch.setattr("tmdb_client.requests.get", mock_requests_get)

   # Wywoływanie funkcji
   movie_id = 123
   result = tmdb_client.get_single_movie(movie_id)

   assert result == mock_movie_data

   mock_requests_get.assert_called_once_with(f"https://api.themoviedb.org/3/movie/{movie_id}",
        headers={"Authorization": f"Bearer {tmdb_client.api_token}"}
   )

# Test funkcji get_movie_images
def test_get_movie_images(monkeypatch):
   # Przygotowanie danych
   mock_image_data = {"backdrops": [{"file_patch": "/path_to_image.jpg"}]}

   # Mock dla funkcji requests.get
   mock_requests_get = Mock()
   mock_response = Mock()
   mock_response.json.return_value = mock_image_data
   mock_requests_get.return_value = mock_response

   monkeypatch.setattr("tmdb_client.requests.get", mock_requests_get)

   # Wywołanie funkcji
   movie_id = 123
   result = tmdb_client.get_movie_images(movie_id)

   # Sprawdzenie, czy funkcja zwraca oczekiwane dane
   assert result == mock_image_data
   mock_requests_get.assert_called_once_with(
      f"https://api.themoviedb.org/3/movie/{movie_id}/images",
      headers={"Authorization": f"Bearer {tmdb_client.api_token}"}
   )

# Test funkcji get_single_movie_cast
def test_get_single_movie_cast(monkeypatch):
   # Przygotowanie danych
   mock_cast_data = [{"name": "Actor1"}, {"name": "Actor 2"}, {"name": "Actor 3"}]

   # Mock dla funkcji requests.get
   mock_requests_get = Mock()
   mock_response = Mock()
   mock_response.json.return_value = {"cast": mock_cast_data}
   mock_requests_get.return_value = mock_response

   monkeypatch.setattr("tmdb_client.requests.get", mock_requests_get)

   # Wywołanie funkcji
   movie_id = 123
   result = tmdb_client.get_single_movie_cast(movie_id)

   # Sprawdzenie, czy funkcja zwraca oczekiwane dane
   assert result == mock_cast_data
   mock_requests_get.assert_called_once_with(
      f"https://api.themoviedb.org/3/movie/{movie_id}/credits",
      headers={"Authorization": f"Bearer {tmdb_client.api_token}"}
   )


# Define the parameterized test
@pytest.mark.parametrize("selected_list, expected_movies", [
   ('popular', [{'id': 1, 'title': 'Movie 1'}, {'id': 2, 'title': 'Movie 2'}]),
   ('top_rated', [{'id': 3, 'title': 'Top Rated Movie 1'}, {'id': 4, 'title': 'Top Rated Movie 2'}]),
   ('upcoming', [{'id': 5, 'title': 'Upcoming Movie 1'}, {'id': 6, 'title': 'Upcoming Movie 2'}]),
])
def test_homepage(monkeypatch, selected_list, expected_movies):
   # Mock the API response based on the selected_list
   api_mock = Mock(return_value=expected_movies)
   monkeypatch.setattr("tmdb_client.get_movies", api_mock)

   with app.test_client() as client:
      # Make the request to the homepage with the selected_list as a query parameter
      response = client.get(f"/?list_type={selected_list}")
        
      assert response.status_code == 200
      api_mock.assert_called_once_with(how_many=8, list_type=selected_list)

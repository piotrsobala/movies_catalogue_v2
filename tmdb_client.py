import requests

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNjczOTVlODExMmUyYzA1OGU0MTA2OGE2NTBkOGM3MCIsIm5iZiI6MTcyNjc1NjIxOS4zMzY2NzIsInN1YiI6IjY2ZTFlY2E2YTZmNTRmYWM4ZmNmYWI3YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.HvRmdpXxtPNDgXYeyQGweSFsC4Vb8-EmZASQUoXbgdY"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNjczOTVlODExMmUyYzA1OGU0MTA2OGE2NTBkOGM3MCIsIm5iZiI6MTcyNjc1NjIxOS4zMzY2NzIsInN1YiI6IjY2ZTFlY2E2YTZmNTRmYWM4ZmNmYWI3YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.HvRmdpXxtPNDgXYeyQGweSFsC4Vb8-EmZASQUoXbgdY"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()



#movies = get_popular_movies()

#if movies:
#    for movie in movies['results']:
#        print(f"Title: {movie['title']}, Release Date: {movie['release_date']}")



def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNjczOTVlODExMmUyYzA1OGU0MTA2OGE2NTBkOGM3MCIsIm5iZiI6MTcyNjc1NjIxOS4zMzY2NzIsInN1YiI6IjY2ZTFlY2E2YTZmNTRmYWM4ZmNmYWI3YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.HvRmdpXxtPNDgXYeyQGweSFsC4Vb8-EmZASQUoXbgdY"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movie_details(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNjczOTVlODExMmUyYzA1OGU0MTA2OGE2NTBkOGM3MCIsIm5iZiI6MTcyNjc1NjIxOS4zMzY2NzIsInN1YiI6IjY2ZTFlY2E2YTZmNTRmYWM4ZmNmYWI3YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.HvRmdpXxtPNDgXYeyQGweSFsC4Vb8-EmZASQUoXbgdY"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

#def get_movies(list_type="popular"):
#    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
#    headers = get_headers()
#    response = requests.get(endpoint, headers=headers)
#    return response.json()

def get_movies(how_many=8, list_type="top_rated"):
    """
    Fetch movies from TMDB API.
    
    :param how_many: Limit the number of movies to fetch.
    :param list_type: Type of movie list (e.g., popular, top_rated).
    """
    movies = get_movies_list(list_type=list_type)
    return movies['results'][:how_many]


def call_tmdb_api(endpoint):
    """Makes a request to the TMDB API and returns the response JSON."""
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()  # Raises an HTTPError if the response was an error
    return response.json()
from flask import Flask, render_template, request, redirect, url_for
import tmdb_client
import random

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Dostępne typy list filmów
VALID_LIST_TYPES = ['popular', 'now_playing', 'top_rated', 'upcoming']

# Lista dostępnych typów filmów
movie_list_types = [
    ("now_playing", "Now Playing"),
    ("upcoming", "Upcoming"),
    ("popular", "Popular"),
    ("top_rated", "Top Rated"),
    ("test", "Test type")
    ]

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
#    movies = tmdb_client.get_popular_movies()["results"][:8]

    if selected_list not in VALID_LIST_TYPES:
        return redirect(url_for('homepage', list_type='popular'))



    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, list_types=movie_list_types)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

#@app.route("/movie/<movie_id>")
#def movie_details(movie_id):
#    return render_template("movie_details.html")


#TEST
@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    movie = tmdb_client.get_movie_details(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)[:16]
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])    
    return render_template("movie_details.html", movie=movie, cast=cast, selected_backdrop=selected_backdrop)

if __name__ == "__main__":
    app.run(debug=True)
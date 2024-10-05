# Movies catalogue

Aplikacja pobierająca bazę filmów z API tmdb 

## Funkcje:
- Pobieranie list filmów
- Pobieranie danych dotyczących filmów: nazwa, opis, budżet, rodzaj, plakat, obsada

## Instalacja

1. Pobierz repozytorium z github:
   ```bash
   git clone git@github.com:piotrsobala/movies_catalogue.git
   cd movies_catalogue
   
2. Stwórz wirtualne środowisko 
   python -m venv "sciezka-do-katalogu/movies_env/"

3. Aktywacja środowiska wirtualnego
   source "sciezka-do-katalogu…/movies_env/bin/activate"
   
4. Zainstaluj biblioteki i framework z requirements.txt
   pip install -r requirements.txt

5. Start aplikacji
   flask run

6. Otwórz stronę w przeglądarce
   http://127.0.0.1:5000/
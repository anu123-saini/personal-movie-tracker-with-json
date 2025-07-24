#personal movie tracker with json , (json is container of file, how to keep your data or file like csv)
# json is like a container or wrapper that contain any data type like [], {} ,string ,array
import os
import json
FILENAME = "movies.json"
def load_movies():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME , "r",encoding = "utf-8") as f :
        return json.load(f)
def save_movies(movies):
    with open(FILENAME , "w",encoding = "utf-8") as f :
        json.dump(movies,f,indent=2)
def add_movies(movies):
    title = input("Enter the movie name: ").strip().lower()
    if any(movie["title"].lower() == title for movie in movies):
        print("Movie is already exist")
        return
    genre = input("Enter Genre :").strip().lower()
    try:
        rating = float(input("Enter the rating(1-10) :"))
    except ValueError:
        print("Enter the correct value !")
        return
    movies.append({"title" : title , "genre" : genre, "rating" : rating})
    save_movies(movies)
    print("Movie added")

def view_movies(movies):
    if not movies:
        print("No movie found")
        print("-" * 40)
    for movie in movies:
        print(f"{movie['title']} -- {movie['genre']} -- {movie['rating']}")

def search_movies(movies):
    term = input("Enter the title or genre :").strip().lower()
    results = [movie for movie in movies
        if term in movie['title'].lower()or term in movie
        ['genre'].lower() ]
    
    if not results:
        print("NO Matching result !")
        return
    print(f"Found {len(results)} result(s)")
    for movie in results:
        print(f"{movie['title']} -- {movie['genre']} -- {movie['rating']}")

def run_movie_db():
    movies = load_movies()
    while True:
        print("\nMymoviedb")
        print(" 1. Add movie")
        print(" 2. View All movie")
        print(" 3. Search movie")
        print(" 4. Exit")

        choice = input("choce an option (1-4) : ").strip()
        match choice :
            case "1" :
                add_movies(movies)
            case "2" :
                view_movies(movies)
            case "3" :
                search_movies(movies)
            case "4" :
                break
            case _ :
                print("INvalid !!")

if __name__ == "__main__":
    run_movie_db()





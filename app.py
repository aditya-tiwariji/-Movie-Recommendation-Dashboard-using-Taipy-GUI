from taipy.gui import Gui
import pandas as pd

# Movie dataset
data = {
    "Movie": [
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Avengers Endgame",
        "Titanic",
        "Joker",
        "Frozen",
        "Toy Story",
        "Spider Man",
        "Doctor Strange"
    ],
    "Genre": [
        "Sci-Fi",
        "Sci-Fi",
        "Action",
        "Action",
        "Romance",
        "Drama",
        "Animation",
        "Animation",
        "Action",
        "Sci-Fi"
    ],
    "Rating": [8.8, 8.6, 9.0, 8.4, 7.9, 8.5, 7.5, 8.3, 8.1, 7.9]
}

df = pd.DataFrame(data)

# variables
genres = list(df["Genre"].unique())
selected_genre = genres[0]
search_movie = ""

filtered_movies = df

# filter by genre
def filter_genre(state):
    state.filtered_movies = df[df["Genre"] == state.selected_genre]

# search movie
def search(state):
    state.filtered_movies = df[df["Movie"].str.contains(state.search_movie, case=False)]

# top rated movies
top_movies = df.sort_values(by="Rating", ascending=False).head(5)

page = """

# 🎬 Netflix Style Movie Recommendation Dashboard

## 🔎 Search Movie
<|{search_movie}|input|on_change=search|label=Type movie name|>

## 🎭 Select Genre
<|{selected_genre}|selector|lov={genres}|on_change=filter_genre|>

---

## 🎥 Recommended Movies
<|{filtered_movies}|table|>

---

## ⭐ Top Rated Movies
<|{top_movies}|table|>

---

## 📊 Rating Visualization
<|{filtered_movies}|chart|x=Movie|y=Rating|>

"""

Gui(page).run()
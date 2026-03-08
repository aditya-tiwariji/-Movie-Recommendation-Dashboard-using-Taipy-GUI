🎬 Netflix Style Movie Recommendation Dashboard

A Movie Recommendation Dashboard built using Taipy GUI and Python.
This project demonstrates how interactive dashboards can be used to explore and analyze movie data.

The system allows users to search movies, filter by genre, view top rated movies, and visualize ratings through charts.

📌 Problem Statement

With the increasing number of movies available on streaming platforms, users often find it difficult to decide which movie to watch.

Traditional browsing methods can be time-consuming and inefficient. Users need a simple system that can:

Filter movies by genre

Search movies quickly

Identify top-rated movies

Visualize ratings for better understanding

This project aims to solve this problem by creating an interactive movie recommendation dashboard using Taipy GUI.

💡 Solution

We developed a Movie Recommendation Dashboard that helps users explore movies easily.

The dashboard provides:

🔎 Movie Search – Search movies by name

🎭 Genre Filtering – Filter movies by genre

⭐ Top Rated Movies – Display highest rated movies

📊 Rating Visualization – Visual chart of movie ratings

🎥 Recommended Movies Table – List of filtered movies

The system uses Python and Pandas for data processing and Taipy GUI for building the interactive interface.

🛠 Technologies Used

Python

Taipy GUI

Pandas

Data Visualization (Taipy Charts)

📂 Project Structure
movie-recommendation-dashboard
│
├── app.py
├── README.md
└── screenshots
    ├── dashboard.png
    ├── recommended_movies.png
    ├── top_rated_movies.png
    └── rating_chart.png
⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/aditya-tiwariji/movie-recommendation-dashboard.git
2️⃣ Navigate to the project folder
cd movie-recommendation-dashboard
3️⃣ Install dependencies
pip install taipy pandas
▶️ Run the Application

Run the following command:

python app.py

Then open the browser:

http://127.0.0.1:5000
📊 Features
🔎 Search Movie

Users can type a movie name to filter the movie list.

🎭 Genre Selection

Movies can be filtered based on genre such as:

Sci-Fi

Action

Romance

Drama

Animation

⭐ Top Rated Movies

The system displays the top 5 movies with the highest ratings.

📊 Rating Visualization

A chart shows the relationship between movie titles and their ratings.

📸 Screenshots
Dashboard Interface

Recommended Movies

Top Rated Movies

Rating Visualization

🚀 Future Improvements

The project can be enhanced by:

Using a larger dataset (IMDB / TMDB)

Adding machine learning recommendation algorithms

Displaying movie posters

Integrating movie APIs

Deploying the dashboard online

📚 References

Taipy Documentation
https://docs.taipy.io/en/latest/

Taipy GitHub
https://github.com/Avaiga/taipy

👨‍💻 Author

Aditya Kumar Tiwari
B.Tech Computer Science
NIT Agartala

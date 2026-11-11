
# IMDb Movie Analytics & Recommendation System

A Python-based web scraping and movie recommendation project that collects IMDb Top 250 movie titles and ratings, processes the data and recommends movies based on user-defined rating thresholds.

## Project Overview

The application retrieves movie information from IMDb, extracts titles and ratings, stores the results in a CSV file and allows users to filter movies based on their minimum preferred rating.

## Features

- Scrapes IMDb Top 250 movie listings.
- Extracts movie titles and ratings.
- Stores scraped information in CSV format.
- Cleans and processes rating data using Pandas.
- Accepts a user-defined minimum rating.
- Sorts recommended movies by rating.
- Displays the top 10 matching movies.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Requests | HTTP requests |
| BeautifulSoup | HTML parsing |
| Pandas | Data processing |
| CSV | Data storage |

## Project Workflow

1. Send an HTTP request to IMDb.
2. Parse the returned HTML using BeautifulSoup.
3. Extract movie titles and ratings.
4. Store the collected data in `imdb_movies.csv`.
5. Clean the rating column.
6. Accept a minimum rating from the user.
7. Filter and rank matching movies.
8. Display the top 10 recommendations.

## Project Structure

```text
imdb-movie-analytics/
├── README.md
├── movie_recommender.py
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/JayP-1/imdb-movie-analytics.git
cd imdb-movie-analytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python movie_recommender.py
```

Enter your minimum preferred IMDb rating when prompted.

## Future Improvements

- Add genre-based filtering.
- Introduce a graphical user interface.
- Add movie release year and additional metadata.
- Implement more advanced recommendation techniques.
- Improve scraping reliability and error handling.

## Project Information

**Domain:** Python Development, Web Scraping and Data Analytics.

Developed as an academic programming project at Manipal Institute of Technology.

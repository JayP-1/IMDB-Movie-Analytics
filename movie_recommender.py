import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.imdb.com/chart/top"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

movies = []

rows = soup.select("li.ipc-metadata-list-summary-item")

for row in rows:
    title = row.find("h3").text.strip()
    rating_tag = row.find("span", class_="ipc-rating-star")

    if rating_tag:
        rating = rating_tag.text.strip()
        movies.append([title, rating])

# Save CSV
df = pd.DataFrame(movies, columns=["Title", "Rating"])
df.to_csv("imdb_movies.csv", index=False)

print("✅ Movie data scraped and saved to imdb_movies.csv")

# Load CSV
df = pd.read_csv("imdb_movies.csv")

# Clean rating column
df["Rating"] = df["Rating"].str.extract(r'(\d\.\d)').astype(float)

print("\nMovie Recommendation System 🎬")
min_rating = float(input("Enter minimum IMDb rating (eg: 8.5): "))

recommended = df[df["Rating"] >= min_rating].sort_values(by="Rating", ascending=False)

if recommended.empty:
    print("\n❌ No movies found. Try a lower rating like 8.5")
else:
    print("\nTop Recommended Movies:\n")
    print(recommended.head(10).to_string(index=False))

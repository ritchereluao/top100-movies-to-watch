import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")[::-1]

movie_titles = [each_movie.getText() for each_movie in all_movies]

with open("movies.txt", mode="w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")

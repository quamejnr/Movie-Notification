import os
from dotenv import load_dotenv
import requests
from abc import ABC, abstractmethod

# Initialize dotenv
load_dotenv()



class MovieApi(ABC):

    @abstractmethod
    def get_movie_info(self, movie_title):
        pass


class YTSApi(MovieApi):

    # API endpoint
    url = os.environ.get('YTS_API')

    def get_movies(self) -> list:

        response = requests.get(self.url)

        # Convert JSON to python dictionary and store API response in a variable: data
        data = response.json()
        movies = data['data']['movies']
        return movies

    def get_movie_info(self, movie_being_observed) -> dict:
        movies_on_site = self.get_movies()
        for movie_on_site in movies_on_site:
            if movie_being_observed.lower() in movie_on_site['title'].lower():
                return movie_on_site

    def get_movie_url(self, movie_being_observed) -> str:
        movie_info = self.get_movie_info(movie_being_observed)
        if movie_info:
            movie_url = movie_info['url']
            return movie_url





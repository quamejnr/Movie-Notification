import requests
import json
from abc import ABC, abstractmethod


class MovieApi(ABC):

    @abstractmethod
    def get_movies(self):
        pass

    @abstractmethod
    def get_movie_url(self, movie_title):
        pass

    @abstractmethod
    def get_movie_info(self, movie_title):
        pass


class YTSApi(MovieApi):

    url = 'https://yts.mx/api/v2/list_movies.json?sort_by=date_added&order_by=desc&limit=50'

    def get_movies(self):

        response = requests.get(self.url)

        # Convert JSON to python dictionary and store API response in a variable: data
        data = response.json()
        movies = data['data']['movies']
        return movies

    def get_movie_info(self, movie_title):
        movies = self.get_movies()
        for movie in movies:
            if movie_title.lower() in movie['title'].lower():
                return movie

    def get_movie_url(self, movie_title):
        movie_info = self.get_movie_info(movie_title)
        if movie_info:
            return movie_info['url']





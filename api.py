import requests
from abc import ABC, abstractmethod


class MovieApi(ABC):

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

    def get_movie_info(self, movie_being_observed):
        movies_on_site = self.get_movies()
        for movie_on_site in movies_on_site:
            if movie_being_observed.lower() in movie_on_site['title'].lower():
                return movie_on_site

    def get_movie_url(self, movie_being_observed):
        movie_info = self.get_movie_info(movie_being_observed)
        if movie_info:
            return movie_info['url']





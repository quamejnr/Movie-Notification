from event import notify
from api import MovieApi


TV_SHOWs = {
    'Cursed': ['cursed.s01e01', 'cursed.s01e02', 'cursed.s01e03', 'cursed.s01e04'],
    'The Resident': ['the.resident.s01e01', 'the.resident.s01e02', 'the.resident.s01e03', 'the.resident.s01e04']
}


def check_for_new_episode(series, episode):
    episodes = TV_SHOWs.setdefault(series, [])
    if episode in episodes:
        return
    notify('new_episode', episode)
    TV_SHOWs[series].append(episode)


def check_for_new_movie(movies_being_observed: list, movie_api: MovieApi) -> None:
    for movie in movies_being_observed:
        movie_info = movie_api.get_movie_info(movie)
        if movie_info:
            notify('new_movie', movie_info)

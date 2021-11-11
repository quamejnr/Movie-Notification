from event import notify
from api import YTSApi

yts = YTSApi()

TV_SHOWs = {
    'Cursed': ['cursed.s01e01', 'cursed.s01e02', 'cursed.s01e03', 'cursed.s01e04'],
    'The Resident': ['the.resident.s01e01', 'the.resident.s01e02', 'the.resident.s01e03', 'the.resident.s01e04']
}


MOVIES = ['Old Guard', 'Free Guy', 'Avengers', 'Marvel Eternals']


def check_for_new_episode(series, episode):
    episodes = TV_SHOWs.setdefault(series, [])
    if episode in episodes:
        return
    notify('new_episode', episode)
    TV_SHOWs[series].append(episode)


def check_for_new_movie(movies: list):
    movie_urls = [yts.get_movie_url(movie) for movie in movies if yts.get_movie_url(movie) is not None]
    if movie_urls:
        notify()
    return movie_urls

arr = ['Shang-Chi', 'eternals']

print(check_for_new_movie(arr))
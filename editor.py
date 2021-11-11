from event import notify


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


def check_for_new_movie(movies: list, movie_site):
    for movie in movies:
        movie_info = movie_site.get_movie_info(movie)
        if movie_info:
            notify('new_movie', movie_info)

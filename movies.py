MOVIES_BEING_OBSERVED = []


def register(movies):
    """
    Register movies to be observed
    :param movies: list or string
    :return: None
    """
    if type(movies) is list:
        MOVIES_BEING_OBSERVED.extend(movies)
    else:
        MOVIES_BEING_OBSERVED.append(movies)

from listener import EmailListener, PhoneListener
from desktop_listener import DesktopListener
from editor import check_for_new_episode, check_for_new_movie
from api import YTSApi
from movies import register, MOVIES_BEING_OBSERVED


def main():
    # Initialize event listeners
    # EmailListener()
    # PhoneListener()
    DesktopListener()

    # Initialize Movie Site
    yts = YTSApi()

    # register movies
    register(['eternals', 'venom carnage'])

    # check for new episode
    # check_for_new_episode('See', 'see.s01e01')

    # check for new movie
    check_for_new_movie(MOVIES_BEING_OBSERVED, movie_site=yts)


if __name__ == "__main__":
    main()






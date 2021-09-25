from event import subscribe
from abc import ABC, abstractmethod


class Listener(ABC):

    def __init__(self):
        self.setup_event_handlers()

    @abstractmethod
    def setup_event_handlers(self):
        pass


class PhoneListener(Listener):

    def handle_new_episode(self, episode_name):
        print(f'(Phone Notification) New episode alert: {episode_name} has been released')

    def handle_new_movie(self, movie):
        print(f'(Phone Notification) New movie alert: {movie} has been released')

    def setup_event_handlers(self):
        subscribe('new_episode', self.handle_new_episode)
        subscribe('new_movie', self.handle_new_movie)


class EmailListener(Listener):

    def handle_new_episode(self, episode_name):
        print(f'(Email Notification) New episode alert: {episode_name} has been released')

    def handle_new_movie(self, movie):
        print(f'(Email Notification) New movie alert: {movie} has been released')

    def setup_event_handlers(self):
        subscribe('new_episode', self.handle_new_episode)
        subscribe('new_movie', self.handle_new_movie)

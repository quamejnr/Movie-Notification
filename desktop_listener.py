from listener import Listener
from event import subscribe
from win10toast_click import ToastNotifier
import webbrowser

# Initialize edge web browser
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

# Initialize notifier
toaster = ToastNotifier()


class DesktopListener(Listener):

    @staticmethod
    def open_url(movie_url):
        try:
            webbrowser.get('edge').open(movie_url)
        except Exception as e:
            print(e)

    def handle_new_episode(self, episode_name):
        pass

    def handle_new_movie(self, movie):
        movie_url = movie['url']
        movie_title = movie['title']
        toaster.show_toast("Movie Notification", f"HD version of {movie_title} is available for download",
                           duration=5, callback_on_click=lambda: self.open_url(movie_url))

    def setup_event_handler(self):
        subscribe('new_episode', self.handle_new_episode)
        subscribe('new_movie', self.handle_new_movie)


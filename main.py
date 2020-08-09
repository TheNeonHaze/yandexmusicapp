from yandex_music.client import Client
import config
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.ERROR)


class Downloader:
    def __init__(self, login, password):
        self.client = Client.from_credentials(login, password)

    def tracks_parse(self):
        likes_tracks = [track.id for track in self.client.users_likes_tracks()]
        my_tracks = self.client.tracks(likes_tracks)
        tracks = []

        for track in my_tracks:
            title = track.title
            artist = track.artists[0]['name']
            fullname = title + " " + artist
            tracks.append(fullname)

        return tracks

    def download_track(self, track_id, album_id):
        track = self.client.tracks([f'{track_id}:{album_id}'])
        track = track[0]
        track.download('test.mp3')


bot = Downloader(config.login, config.password)
bot.download_track(2280249, 965663)

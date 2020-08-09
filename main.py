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
        likes_tracks = [f"{track.id}:{track.album_id}" for track in
                        self.client.users_likes_tracks().tracks]
        tracks = []
        for track in self.client.tracks(likes_tracks):
            full_name = track.title
            try:
                full_name += " - " + track.artists[0]['name']
            except IndexError:
                full_name += " - Какашка"
            tracks.append(full_name)
        return tracks

    def download_track(self, track_id, album_id):
        track = self.client.tracks([f'{track_id}:{album_id}'])
        track = track[0]
        track.download(track.title)


bot = Downloader(config.login, config.password)
print(bot.tracks_parse())

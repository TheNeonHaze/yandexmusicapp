from yandex_music.client import Client
import config

#client = Client.from_credentials('example@yandex.com', 'password')

class downloader:
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

bot = downloader(config.login, config.password)
bot.tracks_parse()

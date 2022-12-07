from pytube import YouTube, Playlist


def playlistURL(playlistlink):
    playlistURL = Playlist(playlistlink)
    for url in playlistURL:
        print(url)

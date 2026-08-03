# Refs:
#
# - https://musicdl.readthedocs.io/en/latest/Quickstart.html#download-playlist-items
# - https://click.palletsprojects.com/en/stable/options/  
# - https://pip.pypa.io/en/stable/cli/pip_install/
# - https://docs.astral.sh/uv/pip/packages/#installing-a-package

from musicdl.modules.sources import NeteaseMusicClient

ncm = NeteaseMusicClient()

playlist_url = "https://music.163.com/#/playlist?id=17844035924"

album_urls = (
    "https://music.163.com/#/album?id=78989061",
    "https://music.163.com/#/album?id=93166950",
)

if __name__ == '__main__':
    parsed_song_infos = []
    
    # for album_url in album_urls:
    #     song_info = ncm.parseAlbum(album_url)
    #     parsed_song_infos.append(song_info)
        
    song_info = ncm.parseAlbum(album_urls[0])
    downloaded_song_info = ncm.download(song_info)
    #ncm.parseplaylist(playlist_url)


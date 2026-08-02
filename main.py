from musicdl.modules.sources import NeteaseMusicClient

ncm = NeteaseMusicClient()
album_url = "https://music.163.com/#/album?id=78989061"

if __name__ == '__main__':
    ncm.parseAlbum(album_url)


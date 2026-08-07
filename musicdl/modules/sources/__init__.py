"""initialize"""

# [Ferne] Add selectable music qualities support
from .qq import QQMusicClient, MUSIC_QUALITIES as QQMUSIC_QUALITIES
from .kuwo import KuwoMusicClient, MUSIC_QUALITIES as KUWOMUSIC_QUALITIES
from .migu import MiguMusicClient, MUSIC_QUALITIES as MIGUMUSIC_QUALITIES
from .kugou import KugouMusicClient, MUSIC_QUALITIES as KUGOUMUSIC_QUALITIES
from .deezer import DeezerMusicClient, MUSIC_QUALITIES as DEEZERMUSIC_QUALITIES
from .netease import NeteaseMusicClient, MUSIC_QUALITIES as NETEASEMUSIC_QUALITIES
from .fivesing import FiveSingMusicClient, MUSIC_QUALITIES as FIVESINGMUSIC_QUALITIES
from .qianqian import QianqianMusicClient, MUSIC_QUALITIES as QIANQIANMUSIC_QUALITIES
from .jiosaavn import JioSaavnMusicClient, MUSIC_QUALITIES as JIOSAAVNMUSIC_QUALITIES

from .fma import FMAMusicClient
from .joox import JooxMusicClient
from .moov import MOOVMusicClient
from .base import BaseMusicClient
from .suno import SunoMusicClient
from .tidal import TIDALMusicClient
from .apple import AppleMusicClient
from .qobuz import QobuzMusicClient
from .bodian import BodianMusicClient
from .spotify import SpotifyMusicClient
from .youtube import YouTubeMusicClient
from .jamendo import JamendoMusicClient
from .bilibili import BilibiliMusicClient
from .soundcloud import (
    SoundCloudMusicClient,
    MUSIC_QUALITIES as SOUNDCLOUDMUSIC_QUALITIES,
)
from .streetvoice import (
    StreetVoiceMusicClient,
    MUSIC_QUALITIES as STREETVOICEMUSIC_QUALITIES,
)
from .opengameart import (
    OpenGameArtMusicClient,
    MUSIC_QUALITIES as OPENGAMEARTMUSIC_QUALITIES,
)
from ..utils import BaseModuleBuilder
from ..audiobooks import (
    XimalayaMusicClient,
    LizhiMusicClient,
    QingtingMusicClient,
    LRTSMusicClient,
    ITunesMusicClient,
)
from ..common import (
    GDStudioMusicClient,
    TuneHubMusicClient,
    MP3JuiceMusicClient,
    MyFreeMP3MusicClient,
    JBSouMusicClient,
    XiaoBaiMusicClient,
)
from ..thirdpartysites import (
    MituMusicClient,
    BuguyyMusicClient,
    YinyuedaoMusicClient,
    FiveSongMusicClient,
    FangpiMusicClient,
    TwoT58MusicClient,
    ZhuolinMusicClient,
    HTQYYMusicClient,
    FLMP3MusicClient,
    GequbaoMusicClient,
    KKWSMusicClient,
    GequhaiMusicClient,
    LivePOOMusicClient,
    LiziYYMusicClient,
    MGMP3MusicClient,
    ITingWaMusicClient,
    SgogoMusicClient,
    XiagebaMusicClient,
)


"""MusicClientBuilder"""


class MusicClientBuilder(BaseModuleBuilder):
    REGISTERED_MODULES = {
        # Platforms in Greater China
        "QQMusicClient": QQMusicClient,
        "KugouMusicClient": KugouMusicClient,
        "StreetVoiceMusicClient": StreetVoiceMusicClient,
        "SodaMusicClient": SodaMusicClient,
        "FiveSingMusicClient": FiveSingMusicClient,
        "NeteaseMusicClient": NeteaseMusicClient,
        "QianqianMusicClient": QianqianMusicClient,
        "MiguMusicClient": MiguMusicClient,
        "KuwoMusicClient": KuwoMusicClient,
        "BilibiliMusicClient": BilibiliMusicClient,
        "BodianMusicClient": BodianMusicClient,
        "MOOVMusicClient": MOOVMusicClient,
        # Global Streaming / Indie
        "YouTubeMusicClient": YouTubeMusicClient,
        "JooxMusicClient": JooxMusicClient,
        "AppleMusicClient": AppleMusicClient,
        "JamendoMusicClient": JamendoMusicClient,
        "SoundCloudMusicClient": SoundCloudMusicClient,
        "DeezerMusicClient": DeezerMusicClient,
        "QobuzMusicClient": QobuzMusicClient,
        "SpotifyMusicClient": SpotifyMusicClient,
        "TIDALMusicClient": TIDALMusicClient,
        "FMAMusicClient": FMAMusicClient,
        "JioSaavnMusicClient": JioSaavnMusicClient,
        "OpenGameArtMusicClient": OpenGameArtMusicClient,
        "SunoMusicClient": SunoMusicClient,
        # Audio / Radio
        "XimalayaMusicClient": XimalayaMusicClient,
        "LizhiMusicClient": LizhiMusicClient,
        "QingtingMusicClient": QingtingMusicClient,
        "LRTSMusicClient": LRTSMusicClient,
        "ITunesMusicClient": ITunesMusicClient,
        # Aggregators / Multi-Source Gateways
        "MP3JuiceMusicClient": MP3JuiceMusicClient,
        "TuneHubMusicClient": TuneHubMusicClient,
        "GDStudioMusicClient": GDStudioMusicClient,
        "MyFreeMP3MusicClient": MyFreeMP3MusicClient,
        "JBSouMusicClient": JBSouMusicClient,
        "XiaoBaiMusicClient": XiaoBaiMusicClient,
        # Unofficial Download Sites / Scrapers
        "MituMusicClient": MituMusicClient,
        "BuguyyMusicClient": BuguyyMusicClient,
        "GequbaoMusicClient": GequbaoMusicClient,
        "YinyuedaoMusicClient": YinyuedaoMusicClient,
        "FLMP3MusicClient": FLMP3MusicClient,
        "FangpiMusicClient": FangpiMusicClient,
        "FiveSongMusicClient": FiveSongMusicClient,
        "KKWSMusicClient": KKWSMusicClient,
        "GequhaiMusicClient": GequhaiMusicClient,
        "LivePOOMusicClient": LivePOOMusicClient,
        "HTQYYMusicClient": HTQYYMusicClient,
        "TwoT58MusicClient": TwoT58MusicClient,
        "ZhuolinMusicClient": ZhuolinMusicClient,
        "LiziYYMusicClient": LiziYYMusicClient,
        "MGMP3MusicClient": MGMP3MusicClient,
        "ITingWaMusicClient": ITingWaMusicClient,
        "SgogoMusicClient": SgogoMusicClient,
        "XiagebaMusicClient": XiagebaMusicClient,
    }


"""BuildMusicClient"""
BuildMusicClient = MusicClientBuilder().build

# [Ferne] Add selectable music qualities support
AVALIABLE_MUSIC_QUALITIES = {
    "QQMusicClient": QQMUSIC_QUALITIES,
    "KuwoMusicClient": KUWOMUSIC_QUALITIES,
    "MiguMusicClient": MIGUMUSIC_QUALITIES,
    "KugouMusicClient": KUGOUMUSIC_QUALITIES,
    "DeezerMusicClient": DEEZERMUSIC_QUALITIES,
    "NeteaseMusicClient": NETEASEMUSIC_QUALITIES,
    "FiveSingMusicClient": FIVESINGMUSIC_QUALITIES,
    "QianqianMusicClient": QIANQIANMUSIC_QUALITIES,
    "JioSaavnMusicClient": JIOSAAVNMUSIC_QUALITIES,
    "SoundCloudMusicClient": SOUNDCLOUDMUSIC_QUALITIES,
    "StreetVoiceMusicClient": STREETVOICEMUSIC_QUALITIES,
    "OpenGameArtMusicClient": OPENGAMEARTMUSIC_QUALITIES,
}


from torrent_scrapper.wrappers.BaseWrapper import BaseWrapper
from torrent_scrapper.wrappers.TorrentthoundWrapper import TorrentthoundWrapper
from torrent_scrapper.wrappers.KickasstorrentsWrapper import KickasstorrentsWrapper
from torrent_scrapper.wrappers.VertorWrapper import VertorWrapper

from torrent_scrapper.TorrentEntry import TorrentEntry

class TorrentzWrapper(BaseWrapper):
    
    def __init__(self, *args, **kargs):
        self.__wrappers = [ ("www.torrenthound.com", TorrentthoundWrapper),
                            #("www.kickasstorrents.com", KickasstorrentsWrapper),
                            ("www.vertor.com", VertorWrapper)
            ]
        self.__kargs = kargs
        super().__init__(*args, **kargs)
        
    def download_torrent(self, torrentEntry):
        soup = self.browser.get_soup(torrentEntry.url)
        
        for entry in soup.find("div", {"class": "download"}).find_all("dl"):
            for w in self.__wrappers:
                if w[0] in entry.find("a")["href"]:
                    newTorrentEntry = TorrentEntry(
                        page="torrenthound",
                        name=torrentEntry.name,
                        url=entry.find("a")["href"],
                        fileName=torrentEntry.fileName
                    )
                    w[1](**self.__kargs).download_torrent(newTorrentEntry)
                    return True
        
        return False
        
        
    def get_links(self, keyword):
        soup = self.browser.get_soup("http://torrentz.eu/search", dict(f=keyword))
        
        for entry in soup.find("div", {"class": "results"}).find_all("dl"):
            try:
                te = TorrentEntry(
                    page="torrentz",
                    name=entry.find("dt").get_text(),
                    url="http://torrentz.eu{0}".format(entry.find("a")["href"]),
                    fileName="{0}.torrent".format(entry.find("dt").get_text()),
                    leechers=entry.find("span", {"class": "d"}).get_text(),
                    peers=entry.find("span", {"class": "u"}).get_text()
                )
            except:
                # TODO: manage some errors
                pass
            
            self.add_torrent(keyword, te)
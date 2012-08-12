from wrappers.BaseWrapper import BaseWrapper
from TorrentEntry import TorrentEntry

class TorrentthoundWrapper(BaseWrapper):
    
    def download_torrent(self, torrentEntry):
        html = self.browser.get_soup(torrentEntry.url)
        
        urlToDownload = "http://www.torrenthound.com{0}".format(html.find("div", {"id": "torrent"}).find("a")["href"])
        
        torrent = self.browser.get_file(urlToDownload)

        self.save_torrent(torrentEntry.fileName, torrent)
        
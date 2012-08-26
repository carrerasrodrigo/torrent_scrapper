from torrent_scrapper.wrappers.BaseWrapper import BaseWrapper
from torrent_scrapper.TorrentEntry import TorrentEntry

class VertorWrapper(BaseWrapper):
    
    def download_torrent(self, torrentEntry):
        html = self.browser.get_soup(torrentEntry.url)
        import pdb; pdb.set_trace()
        urlToDownload = html.find("ul", {"class": "down_but"}).find_all("li")[1].find_all("a")[1]["href"]
                
        torrent = self.browser.get_file(urlToDownload)

        self.save_torrent(torrentEntry.fileName, torrent)
        
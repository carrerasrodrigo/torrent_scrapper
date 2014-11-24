from torrent_scrapper.wrappers.BaseWrapper import BaseWrapper


class TorrentthoundWrapper(BaseWrapper):

    def download_torrent(self, torrent_entry):
        html = self.browser.get_soup(torrent_entry.url)

        url = "http://www.torrenthound.com{0}".format(
            html.find("div", {"id": "torrent"}).find("a")["href"])
        torrent = self.browser.get(url)
        self.save_torrent(torrent_entry.file_name, torrent)

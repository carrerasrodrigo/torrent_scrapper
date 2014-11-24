from torrent_scrapper.wrappers.BaseWrapper import BaseWrapper


class VertorWrapper(BaseWrapper):
    def download_torrent(self, torrent_entry):
        html = self.browser.get_soup(torrent_entry.url)

        url = html.find("ul",
            {"class": "down_but"}).find_all("li")[1].find_all("a")[1]["href"]
        torrent = self.browser.get('http://vertor.eu' + url)
        self.save_torrent(torrent_entry.file_name, torrent)

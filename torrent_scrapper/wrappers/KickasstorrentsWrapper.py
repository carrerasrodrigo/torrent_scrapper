from torrent_scrapper.wrappers.BaseWrapper import BaseWrapper


class KickasstorrentsWrapper(BaseWrapper):

    def download_torrent(self, torrentEntry):
        html = self.browser.get_soup(torrentEntry.url)

        urlToDownload = html.find("div",
            {"class": "buttonsline"}).find_all("a")[1]["href"]
        urlToDownload = "http:{0}".format(urlToDownload)

        torrent = self.browser.get_file(urlToDownload)

        self.save_torrent(torrentEntry.fileName, torrent)


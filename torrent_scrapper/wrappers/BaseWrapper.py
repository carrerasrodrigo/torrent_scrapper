import hashlib
import os

from torrent_scrapper.Browser import Browser


class BaseWrapper(object):
    def __init__(self, *args, **kargs):
        self.browser = Browser()
        self.__torrents = {}
        self.__path_torrent = kargs.get("path", "")

    def get_name(self):
        raise NotImplementedError("Should have implemented this")

    def add_torrent(self, keyword, torrent_entry):
        m = hashlib.md5()
        m.update(keyword.encode("utf-8"))
        key = m.hexdigest()

        if not key in self.__torrents:
            self.__torrents[key] = []

        self.__torrents[key].append(torrent_entry)

    def get_torrents(self, keyword):
        m = hashlib.md5()
        m.update(keyword.encode("utf-8"))
        key = m.hexdigest()

        if key in self.__torrents:
            return self.__torrents[key]
        return []

    def get_links(self, keyword):
        raise NotImplementedError("Should have implemented this")

    def save_torrent(self, name, torrent):
        path_to_save = os.path.join(self.__path_torrent, name)
        with open(path_to_save, "wb") as f:
            f.write(torrent)

    def download_torrent(self, torrent_entry):
        raise NotImplementedError("Should have implemented this")

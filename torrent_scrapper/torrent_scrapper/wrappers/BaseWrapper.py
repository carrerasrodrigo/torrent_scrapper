import hashlib, os

from torrent_scrapper.Browser import Browser

class BaseWrapper(object):
    def __init__(self, *args, **kargs):
        self.browser = Browser()
        self.__torrents = {}
        self.__pathTorrent = kargs.get("path", "")
    
    def get_name(self):
        raise NotImplementedError("Should have implemented this")
    
    def add_torrent(self, keyword, torrentEntry):
        m = hashlib.md5()
        m.update(keyword.encode("utf-8"))
        key = m.hexdigest()
        
        if not key in self.__torrents:
            self.__torrents[key] = []
        
        self.__torrents[key].append(torrentEntry)
        
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
        pathToSave = os.path.join(self.__pathTorrent, name)
        with open(pathToSave, "wb") as f:
            f.write(torrent)
            
    def download_torrent(self, torrentEntry):
        raise NotImplementedError("Should have implemented this")

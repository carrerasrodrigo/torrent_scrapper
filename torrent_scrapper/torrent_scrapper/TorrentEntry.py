
class TorrentEntry(object):
    
    def __init__(self, **kargs):
        self.name = kargs.get("name", "")
        self.url = kargs.get("url", "")
        self.added = kargs.get("added", None)
        self.size = kargs.get("size", -1)
        self.peers = kargs.get("peers", -1)
        self.leechers = kargs.get("leechers", -1)
        self.fileName = kargs.get("fileName", -1)

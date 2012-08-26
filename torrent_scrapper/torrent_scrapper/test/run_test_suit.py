import unittest
import os

from torrent_scrapper.wrappers.VertorWrapper import VertorWrapper
from torrent_scrapper.wrappers.KickasstorrentsWrapper import KickasstorrentsWrapper
from torrent_scrapper.wrappers.TorrentthoundWrapper import TorrentthoundWrapper
from torrent_scrapper.TorrentEntry import TorrentEntry

class Wrappers(unittest.TestCase):
    filesToDelete = []
    
    def test_vertor_wrapper(self):
        """
            Test The vertor Wrapper
        """
        
        wrapper = VertorWrapper(path=os.path.abspath("."))
        
        te = TorrentEntry(
            page="vertor",
            name="Test Name",
            url="http://www.vertor.com/torrents/2195389/Hello-Stranger-DVDrip-Eng-Sub-Thai-Movie",
            fileName="TestTorrentVertor.torrent"
        )
        wrapper.download_torrent(te)
        
        pathToFile = os.path.join(os.path.abspath("."), te.fileName)
        
        self.assertTrue(os.path.exists(pathToFile))
        
        self.filesToDelete.append(pathToFile)
    
    def test_kickass_wrapper(self):
        """
            Test The KickAss Wrapper
        """
        
        wrapper = KickasstorrentsWrapper(path=os.path.abspath("."))
        
        te = TorrentEntry(
            page="kickass",
            name="Test Name",
            url="http://www.kickasstorrents.com/hello-stranger-dvdrip-eng-sub-thai-movie-t5262198.html",
            fileName="TestTorrentKickAss.torrent"
        )
        wrapper.download_torrent(te)
        
        pathToFile = os.path.join(os.path.abspath("."), te.fileName)

        self.assertTrue(os.path.exists(pathToFile))

        self.filesToDelete.append(pathToFile)
    
    def test_thound_wrapper(self):
        """
            Test TorrentthoundWrapper Wrapper
        """
        
        wrapper = TorrentthoundWrapper(path=os.path.abspath("."))
        
        te = TorrentEntry(
            page="kickass",
            name="Test Name",
            url="http://www.torrenthound.com/hash/cfde54175585d1b210a7b21688fd673a30ec00a1/torrent-info/Hello-Stranger-DVDrip-Eng-Sub-Thai-Movie-",
            fileName="TestTorrentThound.torrent"
        )
        wrapper.download_torrent(te)
        
        pathToFile = os.path.join(os.path.abspath("."), te.fileName)

        self.assertTrue(os.path.exists(pathToFile))

        self.filesToDelete.append(pathToFile)
    
    
    def tearDown(self):
        for f in self.filesToDelete:
            if os.path.exists(f):
                os.remove(f)
        

if __name__ == '__main__':
    unittest.main()
import sys, getopt

from torrent_scrapper.wrappers.TorrentzWrapper import TorrentzWrapper

class Downloader:
    def __init__(self):
        self.__wrappers = [TorrentzWrapper()]
    
    def __print_torrents(self, torrents):
        i = 0
        print ("Leechers:Peers\tid::Name")
        for t in torrents:
            print ("{0}:{1}\t\t{2} :: {3}".format(t.leechers, t.peers, i, t.name))
            i += 1
    
    def __get_torrent_to_download(self, maxNumber):
        val = -1
        while val not in range(maxNumber+1):
            val = input("Please enter the torrent that you want to download: ")
            try:
                val = int(val)
            except:
                pass
        
        return val
    
    def search(self, keyword):
        torrents = []
        
        for w in self.__wrappers:
            w.get_links(keyword)
            torrents.extend([(w, t) for t in w.get_torrents(keyword)])
            
        self.__print_torrents([t[1] for t in torrents])
        
        ti = self.__get_torrent_to_download(len(torrents))
        torrentToDownload = torrents[ti]
        
        print("--> Downloading ", torrentToDownload[1].name)
        torrentToDownload[0].download_torrent(torrentToDownload[1])
        
        print("--> End")
        
        
    
def main(*argv):
    opts, args = getopt.getopt(argv, "h:k:", ["help", "keyword="])        
    
    helpLine = """
        -h --help : Print the Help
        -k --keyword : Required. The keyword that we want to use to search in the differents engines
        -n --name : The name of the torrent
        -p --path : the path of the torrent
    """
    keyword = ""
    for opt in opts:
        if opt[0] in ["--help", "-h"]:
            print(helpLine)
            sys.exit()
        elif opt[0] in ["--keyword", "-k"]:
            keyword = opt[1]
            
    Downloader().search(keyword)
    
#if __file__ == "main.py":
#    main(sys.argv[1:])

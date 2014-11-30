import getopt
import os
import sys

import colorama
from torrent_scrapper.wrappers.TorrentzWrapper import TorrentzWrapper


colorama.init()


class Downloader:
    def __init__(self, *args, **kargs):
        self.__wrappers = [TorrentzWrapper(path=kargs.get("torrent_path"))]

    def __print_torrents(self, torrents):
        i = 0
        print("ID\tLeechers\tPeers\tName")
        for t in torrents:
            print("{green_color}{number}\t"
                "{leechers}\t\t{peers}\t{name}".format(
                    number=i, leechers=t.leechers, peers=t.peers,
                    name=t.name, green_color=colorama.Fore.GREEN))
            i += 1

    def __get_torrent_to_download(self, max_number):
        val = -1
        while val not in range(max_number+1):
            val = input(colorama.Fore.YELLOW +
                "Please enter the torrent that you want to download: ")
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
        torrent_to_download = torrents[ti]

        print("--> Downloading ", torrent_to_download[1].name)
        torrent_to_download[0].download_torrent(torrent_to_download[1])

        print("--> End")


def main(*argv):
    opts, args = getopt.getopt(argv, "h:k:p:", ["help", "keyword=", "path"])

    helpLine = """
        -h --help : Print the Help
        -k --keyword : Required. The keyword that we want to use to search in the differents engines
        -n --name : The name of the torrent
        -p --path : the path of the torrent
    """
    keyword = ""
    path = os.path.abspath(".")

    for opt in opts:
        if opt[0] in ["--help", "-h"]:
            print(helpLine)
            sys.exit()
        elif opt[0] in ["--keyword", "-k"]:
            keyword = opt[1]
        elif opt[0] in ["--path", "-p"]:
            path = opt[1]

    Downloader(torrent_path=path).search(keyword)

if __file__.endswith("main.py"):
    main(*sys.argv[1:])

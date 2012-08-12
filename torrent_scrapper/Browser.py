#import urllib3, urllib
import urllib.request
import urllib.parse
import os, http.cookiejar

from bs4 import BeautifulSoup

class Browser:
    
    def __init__(self, cookiePath="/tmp/torrent.cookie"):
        
        self.__cj = http.cookiejar.MozillaCookieJar()
        self.__cookiePath = cookiePath
        if not os.path.exists(cookiePath):
            self.__cj.save(cookiePath)
        else:
            self.__cj.load(cookiePath)
            
        self.__browser = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.__cj))

    def get(self, url, params=None):
        if params is not None:
            url += "?{0}".format(urllib.parse.urlencode(params))
            
        f = self.__browser.open(url)
        self.__cj.save(self.__cookiePath)
        
        return f.read().decode('utf-8')
    
    def get_file(self, url, params=None):
        if params is not None:
            url += "?{0}".format(urllib.parse.urlencode(params))
            
        f = self.__browser.open(url)
        self.__cj.save(self.__cookiePath)
        
        return f.read()
    
    def post(self, url, params=None):
        data = urllib.parse.urlencode(params)
        data = data.encode('utf-8')
        request = urllib.request.Request(url)
        # adding charset parameter to the Content-Type header.
        request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
        
        f = self.__browser.open(request, data)
        self.__cj.save(self.__cookiePath)
        return f.read().decode('utf-8')
        
    def get_soup(self, url, data=None):
        return BeautifulSoup(self.get(url, data))
    
    def post_soup(self, url, data=None):
        return BeautifulSoup(self.post(url, data))




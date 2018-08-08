"""

Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

"""

class Codec:
    def __init__(self):
        self.i = 0
        self.url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
    
        :type longUrl: str
        :rtype: str
        """
        self.i += 1
        self.url['http://tinyurl.com/' + str(self.i)] = longUrl
        return 'http://tinyurl.com/' + str(self.i)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.url[shortUrl]
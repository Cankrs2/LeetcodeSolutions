class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.url = "http://tinyurl.com/"
    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodeMap:
            tinyurl = self.url+ str(len(self.encodeMap) + 1)
            self.encodeMap[longUrl] = tinyurl
            self.decodeMap[tinyurl] = longUrl
        return self.encodeMap[longUrl]

    def decode(self, tinyurl: str) -> str:
        return self.decodeMap[tinyurl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
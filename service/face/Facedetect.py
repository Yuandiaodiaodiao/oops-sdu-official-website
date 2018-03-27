from qcloud_image import Client
from qcloud_image import CIUrl, CIFile, CIBuffer, CIUrls, CIFiles, CIBuffers
import json



class Faced(object):

    def __init__(self, appids, secid, seckey, buvke,url):
        client = Client(appids, secid, seckey, buvke)
        client.use_http()
        client.set_timeout(30)
        r=client.face_detect(CIUrl(url))
        # print(r)
        # print(r['code'])
        if str(r["code"])!="0":
            self.rjson="fail"
            return
        self.rjson=r["data"]["face"][0]["gender"]

    def getsex(self):
        if self.rjson=="fail":
            return "man"
        if(int(self.rjson)>=50):
            return "man"
        else:
            return "woman"
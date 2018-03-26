import tornado.options
import json
import Facepp
import Tencentface
import random
import os
import math

with open('temple.txt', 'r') as f:
    templesjson = f.read()
    templesjson = json.loads(templesjson)


def judges(s):
    if s != "" and s != "null" and s != "None":
        return True
    else:
        return False


class Face_Handler(tornado.web.RequestHandler):
    def post(self):
        print("gethttps")
        self.set_header("Access-Control-Allow-Origin", '*')
        jsonsx = json.loads(self.request.body)
        # 默认参数表
        randoms = 1  # 默认一比一调用api
        temple = "cf_movie_fengjiu"
        merge_rate = 100
        baseStr = jsonsx["baseStr"]
        ranges = "206,393,108,103"
        templeurl = "https://s1.ax1x.com/2018/03/21/97rgud.jpg"

        xc = random.randint(0, len(templesjson) - 1)
        merge_rate = templesjson[xc]["merage"]
        templeurl = templesjson[xc]["url"]
        range = templesjson[xc]["range"]

        if "random" in jsonsx:
            if judges(str(jsonsx["random"])):
                randoms = float(jsonsx["random"])
        if "temple" in jsonsx:
            if judges(str(jsonsx["temple"])):
                temple = jsonsx["temple"]
                print(temple)
        if "merge-rate" in jsonsx:
            if judges(str(jsonsx["merge-rate"])):
                merge_rate = jsonsx["merge-rate"]
            print(merge_rate)
        if "range" in jsonsx:
            if judges(str(jsonsx["range"])):
                ranges = jsonsx["range"]
                print(ranges)
        if "templeurl" in jsonsx:
            if judges(str(jsonsx["templeurl"])):
                templeurl = jsonsx["templeurl"]
                templeurl = str(templeurl)
                templeurl = templeurl.replace(" ", "")
                tempx = int(templeurl)-1
                merge_rate = templesjson[tempx]["merage"]
                range = templesjson[tempx]["range"]
                templeurl = templesjson[tempx]["url"]

                print(templeurl)
        randoms=0
        if float(randoms) > 1000:
            randoms = 1000
        randoms *= 1000
        randoms = math.ceil(randoms)
        rand2 = 1000 + randoms

        x = random.randint(0, rand2)
        if x >= 1000:
            print("tencent")
            Tencentface.facemerge(temple, baseStr, self)
        else:
            print("faceapp")
            matho="url"

            Facepp.facemerge(merge_rate, baseStr, ranges, templeurl, matho, self)


if __name__ == "__main__":
    app = tornado.web.Application([(r"/face", Face_Handler)])
    server = tornado.httpserver.HTTPServer(app, ssl_options={
        "certfile": os.path.join(os.path.abspath("."), "server.crt.txt"),
        "keyfile": os.path.join(os.path.abspath("."), "server.key.txt"),
    })

    server.listen(1024)
    print("运行于 1024")
    tornado.ioloop.IOLoop.current().start()

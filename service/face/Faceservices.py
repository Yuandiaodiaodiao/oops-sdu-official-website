import tornado.options
import tornado.web
import json
import Facepp
import Tencentface
import random
import os
import math
import Facedetect
import text2
import timedebug



def judges(s):
    if s != "" and s != "null" and s != "None":
        return True
    else:
        return False


class Face_Handler(tornado.web.RequestHandler):
    def post(self):
        print("建立连接" + str(self.request.headers)[str(self.request.headers).find("User-Agent"):str(self.request.headers).find("\n",str(self.request.headers).find("User-Agent"))-1])
        # if "User-Agent"in (json.loads(self.request.headers)):
        #     print("建立连接"+str(json.loads(self.request.headers)["User-Agent"]))
        # else:
        #     print("user-agent来源不明")
        timex=timedebug.timeclass()

        with open('temple.txt', 'r') as f:
            templesjson = f.read()
            templesjson = json.loads(templesjson)


        self.set_header("Access-Control-Allow-Origin", '*')
        jsonsx = json.loads(self.request.body)
        baseStr = jsonsx["baseStr"]
        sexx="man"
        timex.r()
        sexx = text2.judgeman(baseStr)
        timex.g("判断男女")
        print("性别="+sexx)
        # 默认参数表
        randoms = 1  # 默认一比一调用api
        temple = "cf_movie_fengjiu"
        if sexx=="man":

            templexa = ["cf_lover_fanli", "cf_lover_libai",  "cf_lover_wuque", "cf_movie_yehua"]
        else:
            templexa = [ "cf_lover_sunshang", "cf_lover_xishi","cf_lover_yuhuan", "cf_movie_baiqian", "cf_movie_fengjiu"]
        temple = templexa[random.randint(0, len(templexa) - 1)]

        merge_rate = 100









        ranges = "206,393,108,103"
        templeurl = "https://s1.ax1x.com/2018/03/21/97rgud.jpg"

        xc = random.randint(0, len(templesjson) - 1)
        xt=1
        while templesjson[xc]["sex"]!=sexx:
            print("随机性别次数"+str(xt),end="")
            xt+=1
            if xt>3:
                randoms=1001
                break
            xc = random.randint(0, len(templesjson) - 1)
        if xc==8:
            xc = random.randint(0, len(templesjson) - 1)
        merge_rate = templesjson[xc]["merage"]
        templeurl = templesjson[xc]["url"]
        ranges = templesjson[xc]["range"]
        print("")


        if "random" in jsonsx:
            if judges(str(jsonsx["random"])):
                if float(jsonsx["random"])<0.95 or float(jsonsx["random"])>1.05:
                    randoms = float(jsonsx["random"])

        if "temple" in jsonsx:
            if judges(str(jsonsx["temple"])):
                temple = jsonsx["temple"]
                print(temple)
        if "merge-rate" in jsonsx:
            if judges(str(jsonsx["merge-rate"])):
                merge_rate = jsonsx["merge-rate"]
                print(merge_rate)

        if "templeurl" in jsonsx:
            if judges(str(jsonsx["templeurl"])):
                templeurl = jsonsx["templeurl"]
                templeurl = str(templeurl)
                templeurl = templeurl.replace(" ", "")
                tempx = int(templeurl) - 1


                merge_rate = templesjson[tempx]["merage"]
                ranges = str(templesjson[tempx]["range"])

                templeurl = templesjson[tempx]["url"]
                print("temp id=" + str(tempx))
                print("rang=" + ranges)

                print(templeurl)
        if "range" in jsonsx:
            if judges(str(jsonsx["range"])):
                ranges = jsonsx["range"]
                print(ranges)


        if float(randoms) > 1000:
            randoms = 1000
        randoms = float(randoms)
        randoms *= 1000
        randoms = math.ceil(randoms)
        rand2 = 1000 + randoms

        x = random.randint(0, rand2)

        if x >= 1000:
            print("tencent")
            timex.r()
            Tencentface.facemerge(temple, baseStr, self)
            timex.g("腾讯api函数")
        else:
            print("faceapp")
            matho = "url"
            timex.r()
            Facepp.facemerge(merge_rate, baseStr, ranges, templeurl, matho,self)
            timex.g("faceapp函数")
        print("\n")

if __name__ == "__main__":
    app = tornado.web.Application([(r"/face", Face_Handler)])
    server = tornado.httpserver.HTTPServer(app, ssl_options={
        "certfile": os.path.join(os.path.abspath("."), "server.crt.txt"),
        "keyfile": os.path.join(os.path.abspath("."), "server.key.txt"),
    })

    server.listen(1024)
    print("运行于 1024")
    tornado.ioloop.IOLoop.current().start()

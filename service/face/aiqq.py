import json
import requests
import hashlib
import urllib
import apikey
import time
from urllib import parse
import string
import random


def facemerge(selfs):
    t = time.time()
    baseStr = json.loads(selfs.request.body)["baseStr"]
    tx = apikey.aiqq()
    appid = tx["app_id"]
    appkey = tx["appkey"]
    sign = ""
    datas = {
        "app_id": str(appid),

        "image": baseStr[baseStr.find(",") + 1:],
        "model": "7",
        "nonce_str": "".join(random.sample(string.ascii_letters + string.digits,17)),

        "time_stamp": str(int(t))
    }
    datax={
        "app_id":"10000",
        "key1": "腾讯AI开放平台",
        "key2": "示例仅供参考",
        "nonce_str": "20e3408a79",





        "time_stamp":"1493449657"

    }
    # appkey="a95eceb1ac8c24ee28b70f7dbba912bf"
    imagx=urllib.parse.quote(datas["image"].encode('utf8')).upper()
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))

    sign="app_id="+str(appid)+"&image="+imagx+"&model="+"7"+"&nonce_str="+nonce_str+"&time_stamp="+str(int(t))+"&app_key="+appkey
    m=hashlib.md5()
    m.update(sign.encode('utf8'))
    sign=m.hexdigest()
    sign=sign.upper()
    allsign="app_id="+str(appid)+"&image="+imagx+"&model="+"7"+"&nonce_str="+nonce_str+"&time_stamp="+str(int(t))+"&sign="+sign
    # sign = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest().upper()
    datas["sign"] = sign
    url = "https://api.ai.qq.com/fcgi-bin/ptu/ptu_facemerge"
    headersx = {"Content-Type": "application/x-www-form-urlencoded"}
    # print(datax)
    url=url+"?"+allsign
    r = requests.get(url)
    print(r.text)
    ret=r.json()["ret"]
    returns = {"imagetype": "base64", "error": "null"}
    if str(ret)!="0":
        returns["ifok"] = "false"
        returns["error"]=r.json()["msg"]
        print(r.json()["msg"])
    else:
        returns["ifok"] = "ok"
        returns["image"] = r.json()["data"]["image"]
    selfs.write(json.dumps(returns))

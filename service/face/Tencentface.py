import json
import requests
import TencentYoutuyun
import apikey
import time
import ssl
import base64
import sys
import timedebug
import warnings


def posts(url, datas, headersx, selfs, deep):
    deep += 1
    print("-1001重试次数=" + str(deep - 1))
    sess = requests.session()
    timex = timedebug.timeclass()
    timex.r()
    r = sess.post(url, data=json.dumps(datas), headers=headersx)
    # print(r.text)
    timex.g("post图片")
    ret = r.json()["ret"]
    returns = {"imagetype": "base64", "error": "null"}
    if str(ret) != "0":
        print("错误信息" + ret)
        returns["ifok"] = "false"
        if str(ret) == "1000":
            returns["error"] = "noface"
        else:

            if str(r.json()["ret"]) == "-1001":
                if deep > 5:
                    returns["error"] = "-1001"
                    selfs.write(json.dumps(returns))
                    return -1
                return deep
            returns["error"] = "other"
    else:
        returns["ifok"] = "true"
        returns["image"] = r.json()["img_base64"]
    print("api返回数据包" + str(round((len(str(returns)) * 1.0 / 1024), 2)) + "kb")
    timex.r()
    selfs.write(json.dumps(returns))
    timex.g("post给前端")

    return -1


def facemerge(temple, baseStr, selfs):
    timex = timedebug.timeclass()
    timex.r()
    s=""
    outs=sys.stdout
    errs=sys.stderr
    sys.stdout=s
    sys.stderr=s
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        rc = requests.get(baseStr)
    sys.stdout=outs
    sys.stderr=errs
    timex.g("下载图片")
    # print(rc.content)
    baseStr = str(base64.b64encode(rc.content))

    tx = apikey.tencentapi()
    appid = tx["appid"]
    secret_id = tx["secret_id"]
    secret_key = tx["secret_key"]
    userid = tx["userid"]
    end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT
    youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
    headersx = youtu.get_headers("233")
    headersx['Host'] = 'api.youtu.qq.com'
    url = 'http://api.youtu.qq.com/cgi-bin/pitu_open_access_for_youtu.fcg'
    datas = {
        'app_id': appid,
        'rsp_img_type': 'base64',
        'img_data': baseStr[baseStr.find(",") + 3:len(baseStr) - 1]

    }
    # print(str(datas))
    print("接收图片大小=" + str(round(len(datas["img_data"]) * 1.0 / 1024,2)) + "kb")
    print("使用模板=" + temple)
    params = {"model_id": temple}
    opdata = {"cmd": "doFaceMerge", "params": params}
    datas["opdata"] = [opdata]
    headersx['Content-Length'] = str(len(str(datas)))
    deep = 0
    while deep != -1:
        deep = posts(url, datas, headersx, selfs, deep)
        continue

    # print(returns)

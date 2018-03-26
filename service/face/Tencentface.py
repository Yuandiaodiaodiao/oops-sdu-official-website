import json
import requests
import TencentYoutuyun
import apikey
import time
import ssl
import base64

ssl._create_default_https_context = ssl._create_unverified_context
def posts(url, datas, headersx, selfs,deep):
    deep+=1
    print("deep="+str(deep))
    sess = requests.session()
    r = sess.post(url, data=json.dumps(datas), headers=headersx)
    # print(r.text)

    ret = r.json()["ret"]
    returns = {"imagetype": "base64", "error": "null"}
    if str(ret) != "0":
        returns["ifok"] = "false"
        if str(ret) == "1000":
            returns["error"] = "noface"
        else:
            print(r.text)
            if str(r.json()["ret"]) == "-1001":
                if deep>5:
                    returns["error"] = "-1001"
                    selfs.write(json.dumps(returns))
                    return -1
                return deep
            returns["error"] = "other"
    else:
        returns["ifok"] = "true"
        returns["image"] = r.json()["img_base64"]
    print(str(len(str(returns))*1.0/1024)+"kb")
    selfs.write(json.dumps(returns))

    return -1


def facemerge(temple, baseStr, selfs):



    rc=requests.get(baseStr,verify=False)
    rc.content
    baseStr=str(base64.b64encode(rc.content))




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
        'img_data': baseStr[baseStr.find(",") + 3:len(baseStr)-1]

    }
    # print(str(datas))
    print("imagelength=" + str(len(datas["img_data"]) * 1.0 / 1024)+"kb")
    print("temp="+temple)
    params = {"model_id": temple}
    opdata = {"cmd": "doFaceMerge", "params": params}
    datas["opdata"] = [opdata]
    headersx['Content-Length'] = str(len(str(datas)))
    deep=0
    while  deep!=-1:
        deep=posts(url, datas, headersx, selfs,deep)
        continue

    # print(returns)

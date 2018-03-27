import apikey
import json
import requests
import timedebug

def facemerge(mer_rate,baseStr,ranges,templeurl,metho,selfs):
    sess=requests.session()
    apikeys= apikey.facepp()

    url = 'https://api-cn.faceplusplus.com/imagepp/v1/mergeface'
    datas={
        "api_key":apikeys["api_key"],
        "api_secret":apikeys["api_secret"],
        'template_url': templeurl,
        'template_rectangle': ranges,

        'merge_rate': mer_rate
    }

    if metho=="url":
        datas["merge_url"]=baseStr
    else:
        datas['merge_base64']=baseStr[baseStr.find(",") + 1:]
    print("api数据包"+str(datas))
    timex = timedebug.timeclass()
    timex.r()
    r=sess.post(url,data=datas)
    timex.g("调用api")
    # print("Returnnnnnnn="+r.text)
    returns = {"imagetype": "base64", "error": "null"}
    # print(r.json())
    jsons=r.json()
    if len(jsons)!=0:
        if "error_message" in jsons:
            errors=jsons["error_message"]
            print("错误信息",end="")
            print(jsons)
            returns["ifok"] = "false"
            if errors.find("BAD_FACE")!=-1 or errors.find("NO_FACE_FOUND")==-1 :
                returns["error"]="noface"
            else:
                returns["error"]=errors
        else:
            returns["ifok"] = "true"
            returns["image"] = jsons["result"]
    timex.r()
    selfs.write(json.dumps(returns))
    timex.g("self.write")
import apikey
import json
import requests

def facemerge(mer_rate,baseStr,ranges,templeurl,metho,selfs):
    sess=requests.session()
    apikeys= apikey.facepp()
    templeurl="https://s1.ax1x.com/2018/03/21/97rgud.jpg"
    ranges="206,393,108,103"
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
    print("post+++++"+str(datas))
    r=sess.post(url,data=datas)
    # print("Returnnnnnnn="+r.text)
    returns = {"imagetype": "base64", "error": "null"}
    # print(r.json())
    jsons=r.json()
    if len(jsons)!=0:
        if "error_message" in jsons:
            errors=jsons["error_message"]
            print(errors)
            returns["ifok"] = "false"
            if errors.find("BAD_FACE")!=-1 or errors.find("NO_FACE_FOUND")==-1 :
                returns["error"]="noface"
            else:
                returns["error"]=errors
        else:
            returns["ifok"] = "true"
            returns["image"] = jsons["result"]
    selfs.write(json.dumps(returns))
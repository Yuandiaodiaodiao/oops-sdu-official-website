import requests
import Facedetect
import time
fappid="1256293253"
# fserid="AKIDve8MK2ghdMr54nqSO3YqulT3PYUDp16y"
# fserkey="mLhqlW9arvmQvDJFyUmrgFYaZMtAEsJU"
fserid="AKIDve8MK2ghdMr54nqSO3YqulT3PYUDp16y"
fserkey="mLhqlW9arvmQvDJFyUmrgFYaZMtAEsJU"
fbucket="oops-temp"
url="https://oops-temp-1256293253.cos.ap-chengdu.myqcloud.com/img/2018-03-28-0-36-56-TIM截图20180321173337.png"
bucketsx="http://oops-temp-1256293253.piccd.myqcloud.com/"

def judgeman(urls):
    urls=urls[urls.find("img"):]

    urls=bucketsx+urls
    print(urls)
    facex=Facedetect.Faced(fappid,fserid,fserkey,fbucket,urls)

    return facex.getsex()


#
# apikey2="DvrrBM_hSSqjTMNE2YvdyfIb4XxB7kME"
# apiser2="Bt1UUXx6TSrs-S4nbXEXW13hRZvaYV-u"
#
# datas={
#         "api_key":apikey2,
#     "api_secret":apiser2,
#         "image_url":url,
#
#        "return_attributes":"headpose"
#     }
# time1=time.time()
# url2="https://api-cn.faceplusplus.com/facepp/v3/detect"
# r=requests.post(url2,data=datas)
# print("timeused="+str(time.time()-time1))
# print(r.text)
# judgeman(url
#  rc = requests.get("https://oops-temp-1256293253.cos.ap-chengdu.myqcloud.com/img/5tim20180321172818.png")
if __name__=="__main__":



    time1 = time.time()
    judgeman(url)
    print("timeused=" + str(time.time() - time1))
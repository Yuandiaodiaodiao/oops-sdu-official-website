import random
import json
global keys
with open('api.txt', 'r') as f:
    keys=f.read()

def tencentapi():

    tx=(json.loads(keys))["tencent"]
    return tx[random.randint(0,len(tx)-1)]
def facepp():
    facex=(json.loads(keys))["facepp"]
    return facex[random.randint(0,len(facex)-1)]
def aiqq():
    facex=(json.loads(keys))["aiqq"]
    return facex[random.randint(0,len(facex)-1)]

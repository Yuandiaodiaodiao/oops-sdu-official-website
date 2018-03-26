import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
requests.adapters.DEFAULT_RETRIES = 30
url="http://www.baidu.com"
session = requests.Session()
session.keep_alive = False
r=session.get(url)
print(r.text)
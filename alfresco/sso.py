#!/usr/bin/env python

import requests
import string
import json

URL_TEMPLATE=string.Template('http://$host:$port/alfresco/service/api/people')
   

HEADERS={'content-type':'application/json','Accept':'application/json',
         'Authorization':'Negotiate YIIFXQYGKwYBBQUCoIIFUTCCBU2gJzAlBgkqhkiG9xIBAgIGBSsFAQUCBgkqhkiC9xIBAgIGBisGAQUCBaKCBSAEggUcYIIFGAYJKoZIhvcSAQICAQBuggUHMIIFA6ADAgEFoQMCAQ6iBwMFAAAAAACjggFoYYIBZDCCAWCgAwIBBaERGw9BUFBOT1ZBVElPTi5DT02iJjAkoAMCAQOhHTAbGwRIVFRQGxNkbmEuYXBwbm92YXRpb24uY29to4IBHDCCARigAwIBF6EDAgECooIBCgSCAQa2WuKlcxC/gKuPHAej2pMvVztN0LJjL59WXnB82KJjoOkSP3UiXO2LEX/J+8IaRag1tOXorAF6i81gvl5ZrsAfGaIISDEylvAfQIzado6iaJFyGsgmcjiMEobkNbE1Mgpu311Oh8BHxW9jm57H98h8v8NWlAyDSG9ezhVstioBjfmkftyl/2Hm7IlGeOlr9BY3BRloUfgMTPUXF+v/orYormFyRULOI6rd94CU7D7exvRnH4K8a8Yw+JQaszlr0TJQEvgLhyjmE1QOaPEw4qUTHIaW4Wdd8wxC3AUBijHHCdVCF0yGjC7knAAYEosBOTG1MaBwht6lxjdVGtywCKvgHXrzpds9pIIDgDCCA3ygAwIBF6KCA3MEggNvMXVBsvm1TdcokCfQOC8eIMuZk5qqfZo6kn5R4sMT+mvz0xd76frdMRbKup3h6Twc95aINAU0P/rgsRka6gHmoCINyW6Yk3Oai8kjxgWHRir3NskTz3gHchA1Mhz5u8XBEYtHHbgkq1O73wW4lSOo0idB+320vQS+PnrBXsXn7byqHUqBfXYkiBqDGYzr+OHBlxwPnVYiqi+5xdjCBsmYDMhF2JykZrn2a7opZPUsDPFGIEghbqhDexLKN5s4GaSC1/bU//0A8e75WuaYeNG+mrQamyu1MPrGw0tyAdByhdLhksbn/xPhrlhOPx9y7lbauRLBD28ylbc4NR3rSR3RoMyCbEW31bFa4F6CP4CfBBcV3e63Gdmlhp233U5qiP7/QpUUVQ5OHx0mMlM8VHYQHB/LEBjWxcQNu6oUl9vhcVLb9wttqCzx9ryJqYsE3RxQNAO00Ar0hkyewrEY3gjVBynQIpO5iZlI8infDP9CRB4/qicNhivOzeJxJr3rhA2DjuDwng8fYXnimRSl9RHfgZVYl6/PC8SF1fMJWmUal0w0TJsSFAvE4pdHe7jD2jjRIUZUtMdUXrYjXLd4F4dKGYXZex92L55DqzbnTpDHo5TiAUuhJ9oCW9hXARH00nsPtZYKGY9DbiL0qK/Xg6g3ZS7Z6N16eW7uTwpHj2jDL2YS6VOBAkkfTkHyMgIemGVke/HZhgRHU/Oim9S0e1gNjbxaJ4sfa7ozjA4d/V+Xb8IVfwwsyfBXtuOp0qBtxmeeHdjNIJ5wSb/DLlQ45txFRn9FGzDt6QMbR3lwZNjQUT52MEUsn4KtiJUiThu1/KFqXGnOTbFyCQ9z8esQ2vj/X8z/nXMLO359Z+owy3MUMwEOPdaf0AwmtjAl6do88i1mzhtJRaxb13fIvRdnL4AP7SL3vI5WxfhIq2dso44UdylcJtzb+N7AYt5vUmmX7ScZS6dknMVaz3bVvJf+nUvprl+hpO+caaFT0hlmbJEN8TVuvVWes9K7s7p3NVAEklPW6Z+UTjeeiZgscuL/ycsYA17R34umCkEXj0HTGrWAeU0QAHzA63p9htKHt7a0yF8Ktm2Q0C6+b+LrXtPXilXlkn4QFY8e/yr4VnQcB2aLm47rhi9suZrvSPeenS0idF0xesOMqQpx2kqODBPcKUnV'
         }


def test():
    
    url=URL_TEMPLATE.substitute(host='dna.appnovation.com',port='8080',)                        
                
    r=requests.get(url,headers=HEADERS)
    print r.content
    return json.loads(r.content)['people']
    


if __name__ == '__main__':
    print test()


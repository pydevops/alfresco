#!/usr/bin/env python
import json
from pprint import pprint
import requests
import urllib
import string


class AlfSession(object):

    # url templates
    URL_TEMPLATE_LOGIN=string.Template('http://$host:$port/alfresco/service/api/login')
    URL_TEMPLATE_LOGOUT=string.Template('http://$host:$port/alfresco/service/api/login/ticket/$alf_ticket?alf_ticket=$alf_ticket&format=json')
    URL_TEMPLATE=string.Template('http://$host:$port/alfresco/service/api/$func?alf_ticket=$alf_ticket')
    URL_TEMPLATE_SITES=string.Template('http://$host:$port/alfresco/service/api/sites/$site?alf_ticket=$alf_ticket')
    
    HEADERS={'content-type':'application/json'}
    
    def __init__(self,host,port,uid,pwd):
        self.host=host
        self.port=port
        url_login=AlfSession.URL_TEMPLATE_LOGIN.substitute(host=host,port=port)
        payload={'username':uid,'password':pwd}                
        r=requests.post(url_login,headers=AlfSession.HEADERS,data=json.dumps(payload))
        print r.status_code
        self.ticket=json.loads(r.content)['data']['ticket']
        

    def logout(self):
        
        url=AlfSession.URL_TEMPLATE_LOGOUT.substitute(host=host,port=port,alf_ticket=self.ticket)
            
        r=requests.delete(url,headers=AlfSession.HEADERS)
        response=json.loads(r.content)
        
        status_code=response['status']['code']
        
        return status_code==200
    
    
    
    def post(self,func,payload):    
    
        url=AlfSession.URL_TEMPLATE.substitute(func=func,host=self.host,port=self.port,alf_ticket=self.ticket)
            
        r=requests.post(url,headers=AlfSession.HEADERS,data=json.dumps(payload))
        return json.loads(r.content)

    def put(self,func,payload=None):
        
        url=AlfSession.URL_TEMPLATE.substitute(func=func,host=host,port=port,alf_ticket=self.ticket)
                
        r=requests.put(url,headers=AlfSession.HEADERS, data=json.dumps(payload))
        return json.loads(r.content)

    
    def get(self,func, data=None):
        
        url=AlfSession.URL_TEMPLATE.substitute(func=func,host=self.host,port=self.port,alf_ticket=self.ticket)
        
        if data:
            url=url+'/'+urllib.quote(data)
                
        r=requests.get(url,headers=AlfSession.HEADERS)
        return json.loads(r.content)
    
        
    def delete(self,url):
        
        r=requests.delete(url,headers=AlfSession.HEADERS)
        return r.content
    
    
    def create_site(self,site):
                
        return self.post('sites',site)

    def delete_site(self,site):
        url=AlfSession.URL_TEMPLATE_SITES.substitute(host=self.host,port=self.port,alf_ticket=self.ticket,site=urllib.quote(site))
        return self.delete(url)
        
    def sites(self):
        return self.get('sites')
    
    def users(self):
        return self.get('people')['people']
       
    def groups(self):
        return self.get('groups')['data']
        

# configuration
host='192.168.0.1'
port='8080'
uid='admin'
pwd='admin'

alf_session=AlfSession(host,port,uid,pwd)



#invite someone to the site



#create a site
site={'shortName':'site3','sitePreset':'site-dashboard','title':'Chapter3','description':'This is site 3'}
pprint(alf_session.create_site(site))

#site={'shortName':'site2','sitePreset':'site-dashboard','title':'Chapter2','description':'This is site 2'}
#site.update(ticket)
#pprint(alf_session.create_site(site))

# delete a site
#pprint(alf_session.delete_site('site2'))


# list all sites
print '******list sites*****'
pprint(alf_session.sites())


# create a user
#user={'userName':'u2','password':'incose','firstName':'first1','lastName':'last1','email':'u2@incose.org'}
#user.update(data)
#pprint(json.loads(post('people',user)))

# list all users
print '****users*****'
for p in alf_session.users():
    print p['userName']
    

# list all the groups
print '****groups******'
for g in alf_session.groups():
    print g['shortName']



# retrieve content
#node_ref='node/workspace/SpacesStore/7348b8e7-4651-4721-8ec5-36fcc15287ca'
#node=get(node_ref,data)
#print node

# log out
if alf_session.logout():
    print uid,' log out successfully'
else:
    print uid,'log out error'
    
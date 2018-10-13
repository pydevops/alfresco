#!/usr/bin/env python

#
#      Licensed to the Apache Software Foundation (ASF) under one
#      or more contributor license agreements.  See the NOTICE file
#      distributed with this work for additional information
#      regarding copyright ownership.  The ASF licenses this file
#      to you under the Apache License, Version 2.0 (the
#      "License"); you may not use this file except in compliance
#      with the License.  You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#      Unless required by applicable law or agreed to in writing,
#      software distributed under the License is distributed on an
#      "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#      KIND, either express or implied.  See the License for the
#      specific language governing permissions and limitations
#      under the License.
#
"""
Module containing the sample code for an Alfresco 4.0 EE installation
"""

import cmislib
import cmislib.model
import cmislibalf
import time, datetime
from pprint import pprint
from contextlib import closing



ROLES = dict(
CONSUMER = "{http://www.alfresco.org/model/content/1.0}cmobject.Consumer",
EDITOR = "{http://www.alfresco.org/model/content/1.0}cmobject.Editor",
CONTRIBUTOR = "{http://www.alfresco.org/model/content/1.0}cmobject.Contributor",
COLLABORATOR = "{http://www.alfresco.org/model/content/1.0}cmobject.Collaborator",
COORDINATOR = "{http://www.alfresco.org/model/content/1.0}cmobject.Coordinator",
)



def print_folder(folder):
    print '*****print childrens of the folder', folder.getName()
    for c in folder.getChildren():    
        print c.name
    print '*****print childrens of the folder', folder.getName()

    #acl=c.getACL()
    #pprint(acl.getEntries(),indent=4)
    #print '***ations:'
    #actions=c.getAllowableActions()
    #for k,v in actions.items():
    #    print k,':',v


''' print the document's properties (metadata)
'''
def print_doc(doc):
    print '*****print property of doc:',doc.getTitle()
    print 'isCheckedOut=',doc.isCheckedOut()
    for k,v in doc.properties.items():
        print "%s,%s\n" % (k,v)
    print '*****print property of doc:',doc.getTitle()


    
def print_rs(resultSet):
        iCount = 0
        for res in resultSet:
            print "----------------------\r\nResult %s:" % iCount
            print "id:%s" % res.id
            print "name:%s" % res.name
            print "created:%s" % res.properties['cmis:creationDate']
            iCount += 1



def print_acl(acl):
    for ace in acl.entries.values():
        print 'principal:%s has the following permissions...' % ace.principalId
        for perm in ace.permissions:
             print perm




def create_doc(folder):
    
    TYPE = 'whitepaper'
    NAME = 'sample'
    
    fileName = NAME + " (" + str(time.time()) + ")"

    properties = {}
    properties['cmis:objectTypeId'] = "D:sc:whitepaper"
    properties['cmis:name'] = fileName

    docText = "This is a sample whitepaper document called " + NAME

    doc = folder.createDocumentFromString(fileName, properties, contentString=docText, contentType="text/plain")
    
    # Add two custom aspects and set aspect-related properties
    doc.addAspect('P:sc:webable')
    doc.addAspect('P:sc:productRelated')
    props = {}
    props['sc:isActive'] = True
    props['sc:published'] = datetime.datetime(2012, 4, 1)
    props['sc:product'] = 'IncoseProduct'
    props['sc:version'] = '1.1'
    doc.updateProperties(props)

    print "isActive: %s" % doc.properties['sc:isActive']
    print "published: %s" % doc.properties['sc:published']
    print "product: %s" % doc.properties['sc:product']
    print "version: %s" % doc.properties['sc:version']

    return doc


def test():
    # log on to CMIS
    cmisClient = cmislib.CmisClient('http://localhost:8080/alfresco/s/cmis', 'admin', 'admin')
    #cmisClient = cmislib.CmisClient('http://localhost:8080/alfresco/s/cmis', 'mjackson', 'password')
    
    # root repo
    repo = cmisClient.defaultRepository
    print('repo permdef=',repo.getPermissionDefinitions())
    
    #print '*************repoinfo:'
    #for k,v in repo.getRepositoryInfo().items():
    #    print k,':',v
    #print '*************repoinfo:'
    
    #print '************perm defs:'
    #for permDef in repo.permissionDefinitions:
    #    print permDef
    #print '************perm defs:'
    
    # get the CMIS object for sample site 's documentLibrary
    dl_root= repo.getObjectByPath('/Sites/swsdp/documentLibrary')
    
    
    # get the CMIS sample folder and sample doc
    folder=repo.getObjectByPath('/Sites/swsdp/documentLibrary/Agency Files/Contracts/')
    print_folder(folder)
    doc=repo.getObjectByPath('/Sites/swsdp/documentLibrary/Agency Files/Contracts/Project Contract.pdf')
    print_doc(doc)
    
    # retrieve the content via getContentStream() and write a file locally
    with closing(doc.getContentStream()) as s:
        content=s.read()
    with open(doc.getTitle(),'w') as f:
        print >>f,content
    
    
    # check it out
    #if not doc.isCheckedOut():
    #    pwc=doc.checkout()
    ## check it in
    #if doc.isCheckedOut():
    #    with open('sample1.pdf','r') as f:
    #        pwc.setContentStream(contentFile=f)
    #    pwc.checkin()
    
    
    # create a folder and upload custom content via folder.createDocument
    
    #root = repo.getRootFolder()
    #folder=repo.createFolder(root,'demo')
    
    
    folder=repo.getObjectByPath('/demo')
    #doc=create_doc(folder)
    ##print the custom content
    #print_doc(doc)
    
    # Perform a CMIS query
    print 'CMIS query........'
    results = repo.query("select * from sc:doc")
    print_rs(results)    
    
    
    # add role
    print '**************add permission*********'
    group='GROUP_demogrp'
    acl =cmislib.model.ACL()
    acl.addEntry(cmislib.model.ACE(group,ROLES['CONTRIBUTOR'], 'true'))
    print folder.applyACL(acl)
    print_acl(folder.getACL())
    
    print '**************remove permission*******'
    # remove role
    acl = folder.getACL()
    #acl.removeEntry(group)
    print folder.applyACL(acl)
    print_acl(folder.getACL())

if __name__ == '__main__':
    test()

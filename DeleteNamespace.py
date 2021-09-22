import maya.cmds as cm
import pymel.core as pm

def CheckNamespace():
    global namespaces
    namespaces=cm.namespaceInfo(listOnlyNamespaces=True, recurse=True)
    return namespaces
    
def DeleteEmptyNamespace():
    for i in namespaces:
        if i=='UI':
            pass
        elif i=='shared':
            pass
        else:
            try:
                print i
                cm.namespace(rm=i)
            except:
                pass
                
def DeleteNamespace():
    refNode_List=[]
    Filter_namespace=[]
    for n in namespaces:
        if n=='UI':
            pass
        elif n=='shared':
            pass
        else:
            Filter_namespace.append(n)
    refs=pm.listReferences()
    for ref in refs:
        for_list=ref.namespace
        refNode_List.append(for_list)
    for refN in refNode_List:
        Filter_namespace.remove(refN)
    for det_nspace in Filter_namespace:
        try:
            cm.namespace(removeNamespace = det_nspace, mergeNamespaceWithParent = True)
        except:
            pass
                 
CheckNamespace()
DeleteEmptyNamespace()
CheckNamespace()
DeleteEmptyNamespace()
CheckNamespace()
DeleteEmptyNamespace()

DeleteNamespace()

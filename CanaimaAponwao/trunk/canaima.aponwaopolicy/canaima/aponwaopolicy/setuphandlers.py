from Products.CMFCore.utils import getToolByName
from StringIO import StringIO
from canaima.aponwaopolicy import AponwaoPolicyMessageFactory as _
from canaima.aponwaopolicy.config import *

def renameRichDocument(portal):
    portal_types = getToolByName(portal, 'portal_types')
    rich_document_fti = getattr(portal_types, 'RichDocument')
    rich_document_fti.title = "Web page"
    rich_document_fti.description = _(u'A Web page that will remplace Document')
    rich_document_fti.content_icon = 'webpage_icon.png'
    rich_document_fti.global_allow = True
    
def disabledDocument(portal):
    portal_types = getToolByName(portal, 'portal_types')
    document_fti = getattr(portal_types, 'Document')
    document_fti.global_allow = False

def addDefaultCategories(portal):
    out = StringIO()
    
    pm = portal.portal_metadata
    objdcmi = pm.DCMI
    if objdcmi <> None:
        objdcmi.updateElementPolicy("Subject","<default>",0,0,"",0,default_categories)
        print >> out, "Updated default subjects as %s" % (default_categories,)
    return out.getvalue()
    
def importVarious(context):
    """ Miscellanous steps import handle
    """
    
    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a 
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.
    
    if context.readDataFile('ubify.policy_various.txt') is None:
        return
    
    portal = context.getSite()
    #setupGroups(portal)
    #renameRichDocument(portal)
    #disableDocument(portal)
    logger = context.getLogger("canaima.aponwaopolicy")
    logger.info(setupGroups(portal))
    logger.info(renameRichDocument(portal))
    logger.info(disableDocument(portal))
    logger.info(addDefaultCategories(portal))


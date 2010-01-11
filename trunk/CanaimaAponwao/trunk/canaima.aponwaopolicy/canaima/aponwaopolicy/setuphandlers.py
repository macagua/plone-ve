from Products.CMFCore.utils import getToolByName

def renameRichDocument(portal):
    portal_types = getToolByName(portal, 'portal_types')
    rich_document_fti = getattr(portal_types, 'RichDocument')
    rich_document_fti.title = "Web page"
    
def disabledDocument(portal):
    portal_types = getToolByName(portal, 'portal_types')
    document_fti = getattr(portal_types, 'Document')
    document_fti.global_allow = False
    
def importVarious(context):
    """ Miscellanous steps import handle
    """
    
    portal = context.getSite()
    setupGroups(portal)
    renameRichDocument(portal)
    disableDocument(portal)
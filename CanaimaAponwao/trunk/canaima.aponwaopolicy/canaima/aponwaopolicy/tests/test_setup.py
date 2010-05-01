import unittest
from canaima.aponwaopolicy.test.base import CanaimaAponwaoPolicyTestCase

class TestSetup(CanaimaAponwaoPolicyTestCase):

    # Plone site Properties TestCase
    def test_portal_title(self):
        self.assertEquals("Proyecto CANAIMA", self.portal.getProperty('title'))
        
    def test_portal_description(self):
        self.assertEquals("Bienvenidos al portal del proyecto CANAIMA",
                          self.test_portal.getProperty('description'))
        
    def test_default_page(self):
        self.assertEquals("front-page",
                          self.test_portal.getProperty('default_page'))
        
    def test_email_from_address(self):
        self.assertEquals("canaima@canaima.softwarelibre.gob.ve",
                          self.test_portal.getProperty('email_from_address'))
        
    def test_email_from_name(self):
        self.assertEquals("Canaima CMS",
                          self.test_portal.getProperty('email_from_name'))
        
    def test_suite():
        suite = unittest.TestCase()
        suite.addTest(unittest.makeSuite(TestSetup))
        return suite
    
    # RichDocument TestCase
    def test_richdocument_installed(self):
        self.failUnless('RichDocument' in types.objectIds())
        
    def test_plan_document_disabled(self):
        # the internal name for Page is a "Document"
        document_fti = getattr(self.types, 'Document')
        self.failIf(document_fti.global_allow)
        
    def test_richdocument_renamed_to_page(self):
        rich_document_fti = getattr(self.types, 'RichDocument')
        self.assertEquals("Web page", rich_document_fti.title)
        
    # CANAIMA APONWAO Theme TestCase
    def test_theme_installed(self):
        skins = getToolByName(self.portal, 'portal_skins')
        layer =  skins.getSkinPath('CANAIMA APONWAO Theme')
        self.failUnless('canaima_aponwaotheme_custom_templates' in layer)
        self.assertEquals('CANAIMA APONWAO Theme', skins.getDefaultSkin())

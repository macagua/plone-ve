from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.viewlets import common

#class SiteLogoViewlet(ViewletBase):
#    render = ViewPageTemplateFile('templates/logo.pt')

class SiteLogoViewlet(common.LogoViewlet):
    """Alter the logo to include the description of our website
    """

    def update(self):
        super(SiteLogoViewlet, self).update()
        self.navigation_root_url = self.portal_state.navigation_root_url()
        portal = self.portal_state.portal()
        logoName = portal.restrictedTraverse('base_properties').logoName
        self.logo_tag = portal.restrictedTraverse(logoName).tag()
        self.portal_title = self.portal_state.portal_title()

    def render(self):
        """
        By doing this, we are subclassing the LogoViewlet class defined in common.py. Our
        subclass will automatically do everything the LogoViewlet parent class does, except
        where we override the parent by telling it to look for a page template known as
        logo.pt. You may remember that the original LogoViewlet class also used logo.pt
        ...but there's a big difference this time. Because the new class is inside
        our theme product, it will find our version of logo.pt, rather than the template in
        plone.app.layout. 
        """
        return self.index()
    
    index = ViewPageTemplateFile('templates/logo.pt')

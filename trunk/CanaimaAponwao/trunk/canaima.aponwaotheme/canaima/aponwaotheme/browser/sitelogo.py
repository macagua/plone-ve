from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class SiteLogoViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/logo.pt')


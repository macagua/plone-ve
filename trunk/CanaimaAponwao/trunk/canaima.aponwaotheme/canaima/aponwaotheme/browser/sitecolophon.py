from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class SiteColophonViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/colophon.pt')


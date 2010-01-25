from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class SiteBannerViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/banner.pt')

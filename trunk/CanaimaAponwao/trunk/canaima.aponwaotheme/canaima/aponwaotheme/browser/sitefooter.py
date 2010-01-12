from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class SiteFooterViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/footer.pt')
    
    def update(self):
        # seteamos los valores que queremos sacar con el template
        # ejemplo tonto:
        self.designer_theme = "Luis Alejandro Martínez Faneyth"
        self.developer_plone_theme = "Leonardo J. Caballero G."



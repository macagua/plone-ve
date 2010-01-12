from plone.theme.interfaces import IDefaultPloneLayer
from plone.app.layout.viewlets.interfaces import IPortalFooter
from zope.viewlet.interfaces import IViewletManager
#from plone.portlets.interfaces import IPortletManager

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "canaima.aponwaotheme" theme, this interface must be its layer
       (in aponwaotheme/viewlets/configure.zcml).
    """

# Viewlet Manager
class ISiteLogo(IViewletManager):
    """A viewlet manager to show logo of the site.
    """

class ISiteFooter(IPortalFooter):
    """A viewlet manager to show logo of the site.
    """

class ISiteColophon(IViewletManager):
    """A viewlet manager to show colophon for anonymous users
    """

# Portlet Manager

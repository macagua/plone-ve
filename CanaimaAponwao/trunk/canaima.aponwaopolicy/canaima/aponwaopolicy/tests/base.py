from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

# There are traditional products (in the Products namespace). They'd normally
# be loaded automatically, but in tests we hace to load them
# should happen at module level to make sure they are available early enough.
ztc.installProduct('SimpleAttachment')
ztc.installProduct('RichDocument')

@onsetup
def setup_canaima_aponwao_policy():
    """Set up the addicional products required for the CANAIMA GNU/Linux Website policy.
    
    The @onsetup decorator causes the excecution of this body to be deferred
    until the setup of the Plone site testing layer.    
    """
    
    # Load the ZCML configuration for the canaima.aponwaopolicy package.
    fiveconfigure.debuf_mode = True
    import canaima.aponwaopolicy
    zcml.load_config('configure.zcml', canaima.aponwaopolicy)
    fiveconfigure.debuf_mode = False
    
    # We need to tell the testing framework that these products
    # should be available. This can't happen until after we hace loaded
    # th ZCML.
    
    #ztc.installPackage('canaima.aponwaopolicy')
    ztc.installProduct('canaima.aponwaopolicy', package=True)
    ztc.installProduct('canaima.aponwaotheme', package=True)

# The order her is important: We first call the (deferred) function
# which installs the products we need for the CANAIMA package. Then,
# we let PloneTestCase set up this product on installation.

setup_canaima_aponwao_policy()
ptc.setPloneSite(products=['canaima.aponwaopolicy'])

class CanaimaAponwaoPolicyTestCase(ptc.PloneTestCase):
    """ We use this base class for all the tests in this packages. If necessary,
    we can pt common utility or setup code in here.
    """
from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='canaima.aponwaotheme',
      version=version,
      description="Provides the standard CANAIMA GNU/Linux Website look and feel, colors, css, etc.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone3 theme cms canama gnu linux venezuela',
      author='Leonardo J. Caballero G.',
      author_email='lcaballero@cenditel.gob.ve',
      url='http://plone.net/providers/leonardo-j-caballero-g',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['canaima'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

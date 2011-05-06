from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='iute.thememain',
      version=version,
      description="An installable theme for Plone 3.0",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme IUTE',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['iute'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'uwosh.core',
          'iute.themebase',
          'plone.browserlayer'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
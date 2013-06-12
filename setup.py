# -*- coding: utf-8 -*-

from distutils.core import setup
try:
    import pypandoc
    LDESC = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    LDESC = ''

setup(name='bottlelog',
      version = '0.1',
      description = 'Apache-like combined logging for Bottle Web Applications',
      long_description = LDESC,
      author = 'Philipp Klaus',
      author_email = 'philipp.l.klaus@web.de',
      url = 'https://github.com/pklaus/bottlelog',
      license = 'BSD',
      packages = ['bottlelog'],
      zip_safe = True,
      platforms = 'any',
      keywords = 'Bottle plugin Apache logging',
      requires = [
          'bottle (>=0.10)'
      ],
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Framework :: Bottle',
          'Environment :: Plugins',
          'Topic :: System :: Logging',
          'Topic :: Internet :: WWW/HTTP :: Site Management',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Natural Language :: English',
      ]
)

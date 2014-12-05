#!/usr/bin/env python

from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='tornadwwo',
      version='0.1',
      description='Async API calls for World Weather Online',
      keywords='tornado weather non-blocking api http',
      author='ALIANE Abdenour Abdelouahab',
      author_email='abdelouahab_al@yahoo.fr',
      url='https://github.com/abdelouahabb/tornadwwo',
      packages=['distutils', 'distutils.command'],
      install_requires=["tornado"],
      license='MIT',
     )


from setuptools import setup
from setuptools import find_packages
import os 

DOCLINES = (__doc__ or '').split("\n")
setup(name='rues',
      version='0.1',
      python_requires='>=3.6',
      description='rues - genetic algorithms in python',
      url='http://github.com/Kamuish/rues',
      author='Kamuish',
      long_description="\n".join(DOCLINES),
      author_email='amiguel@astro.up.pt',
      license='GNU General Public License v3.0',
      packages=find_packages(), 
      zip_safe=False,
      classifiers=[
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8'
      ]
      
      )

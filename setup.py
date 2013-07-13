import os
from setuptools import setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name='SpringGardensRestaurant',
    version='0.1',
    description='CIT Project delivered 2013',
    author='S seed , P truong , S Huynh',
    author_email='',
    install_requires=['Django<=1.4'],
)

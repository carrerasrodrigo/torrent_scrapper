import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='torrent-scrapper',
    version='0.2',
    packages=['torrent_scrapper'],
    include_package_data=True,
    license='BSD License',
    description='',
    long_description=README,
    url='',
    author='Rodrigo N. Carreras',
    install_requires=['beautifulsoup4', 'colorama', 'requests'],
    classifiers=[
        "Topic :: Internet :: WWW/HTTP"
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search"
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        'console_scripts': [
            'download_torrent = torrent_scrapper.main:main'
        ]
    }
)

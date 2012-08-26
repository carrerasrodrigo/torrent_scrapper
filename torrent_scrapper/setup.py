import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'beautifulsoup4',
]

setup(name='torrent_scrapper',
      version='0.0',
      description='Torrent Scrapper',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Topic :: Internet :: WWW/HTTP"
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search"
        "Programming Language :: Python :: 3",
        ],
      author='Rodrigo N. Carreras',
      author_email='',
      url='',
      keywords='torrent search beautifulsoup',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      #test_suite='rv',
      install_requires = requires,
      entry_points = """\
      [console_scripts]
      download_torrent = torrent_scrapper.main:main
      """,
      )

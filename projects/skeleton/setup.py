try:
    from setuptools import setuptools
except:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Kevin de Roulet',
    'url': 'url',
    'download_url': 'dlurl',
    'author_email': 'kevinderoulet@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
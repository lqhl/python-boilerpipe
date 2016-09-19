import tarfile
from fnmatch import fnmatch
from os.path import basename, exists, dirname, abspath, join
from distutils.core import setup

try:
    from urllib import urlretrieve
except:
    from urllib.request import urlretrieve

__version__ = '1.2.0.0'
boilerpipe_version = '2.0-SNAPSHOT'
DATAPATH = join(abspath(dirname((__file__))), 'src/boilerpipe/data')



setup(
    name='boilerpipe',
    version=__version__,
    packages=['boilerpipe', 'boilerpipe.extract'],
    package_dir={'': 'src'},
    package_data={
        'boilerpipe': [
            'data/boilerpipe-common-{version}/boilerpipe-common-{version}.jar'.format(version=boilerpipe_version),
            'data/boilerpipe-common-{version}/lib/*.jar'.format(version=boilerpipe_version),
        ],
    },
    install_requires=[
        'JPype1',
        'charade',
    ],
    author='Misja Hoebe',
    author_email='misja.hoebe@gmail.com',
    maintainer = 'Matthew Russell',
    maintainer_email = 'ptwobrussell@gmail.com',
    url = 'https://github.com/ptwobrussell/python-boilerpipe/',
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Natural Language :: English',
      ],
      keywords='boilerpipe',
      license='Apache 2.0',

    description='Python interface to Boilerpipe, Boilerplate Removal and Fulltext Extraction from HTML pages'
)

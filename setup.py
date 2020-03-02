from setuptools import setup
from sloth import __license__, __version__

long_description = open('README.md', 'r').read()

setup(
    name='sloth',
    version=__version__,
    packages=['sloth'],
    author='Legorooj',
    maintainer='Legorooj, FluffyKoalas',
    author_email='legorooj@protonmail.com',
    description='A python speedtesting library and command line tool',
    keywords='python speed speedtesting testing speedtest awesome cli',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kluffykoalas/sloth',
    project_urls={
        "Bug Tracker": 'https://github.com/fluffykoalas/sloth/issues',
        "Documentation": 'https://sloth-speedtest.readthedocs.io'
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Testing'
    ],
    python_requires='>=3.5',
    install_requires=[
        'tqdm>=4.0'
    ],
    license=__license__
)

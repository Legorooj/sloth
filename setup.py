from setuptools import setup
from sloth import __license__, __version__

long_description = open('README.md', 'r').read()

setup(
    name='sloth-speedtest',
    version=__version__,
    packages=['sloth', 'sloth.raw'],
    author='Legorooj',
    maintainer='Legorooj, FluffyKoalas',
    author_email='legorooj@protonmail.com',
    description='The best python speedtesting library and command line tool',
    keywords='python speed speedtesting testing speedtest awesome cli sloth',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/fluffykoalas/sloth',
    project_urls={
        'Bug Tracker': 'https://github.com/fluffykoalas/sloth/issues',
        'Documentation': 'https://sloth.fluffykoalas.org/en/stable',
        'Source Code': 'https://github.com/fluffykoalas/sloth'
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
    ],
    license=__license__,
    entry_points={
        'console_scripts': [
            'sloth=sloth.__main__:cli'
        ]
    }
)

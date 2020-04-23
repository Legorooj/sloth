from setuptools import setup, find_packages

long_description = open('README.md', 'r').read()

setup(
    name='sloth-speedtest',
    setup_requires="setuptools >= 40.0.0",
    packages=find_packages(where='src'),
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
    python_requires='>=3.6',
    install_requires=[
        # IMPORTANT: Keep aligned with requirements.txt
        'click',
        'setuptools >= 40.0.0',
    ],
    license='MIT',
    entry_points={
        'console_scripts': [
            'sloth = sloth.__main__:cli'
        ],
        'sloth.ext': [
            'compare = sloth.__main__:compare',
            'speedtest-file = sloth.__main__:speedtest_file',
            'speedtest-snippet = sloth.__main__:speedtest_snippet'
        ]
    }
)

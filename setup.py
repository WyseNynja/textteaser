#!/usr/bin/env python
"""TextTeaser is an automatic summarization algorithm."""
import setuptools

setuptools.setup(
    description=__doc__,
    entry_points={
        'console_scripts': [
            'textteaser-cli = textteaser.main:main',
            'textteaser-loop = textteaser.main:loop_main',
        ],
    },
    include_package_data=True,
    install_requires=[
        'nltk',
    ],
    name='textteaser',
    package_data={
        # If any package contains *.txt or *.pickle files, include them:
        'textteaser': ['trainer/*'],
    },
    packages=setuptools.find_packages(),
    version='1.0.0',
)

#!/usr/bin/env python
"""TextTeaser is an automatic summarization algorithm."""
import setuptools

setuptools.setup(
    name='textteaser',
    version='1.0.0',
    description=__doc__,
    packages=setuptools.find_packages(),
    install_requires=[
        'nltk',
    ],
    entry_points={
        'console_scripts': [
            'textteaser-cli = textteaser.main:main',
            'textteaser-loop = textteaser.main:loop_main',
        ],
    },
)

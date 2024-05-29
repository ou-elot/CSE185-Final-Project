import os
from setuptools import setup, find_packages
from mygwas.version import version

MAJ = 0
MIN = 1
REV = 0
VERSION = '%d.%d.%d' % (MAJ, MIN, REV)


setup(
    name='mygwas',
    version=VERSION,
    description='CSE185 Final GWAS',
    author='Elliott Ou, Lenny Lei',
    author_email='elou@ucsd.edu, wlei@ucsd.edu',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mygwas=mygwas.mygwas:main"
        ],
    },
)

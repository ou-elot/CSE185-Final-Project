import os
from setuptools import setup, find_packages
from gwas_tools.__version__ import __version__

MAJ = 0
MIN = 0
REV = 0
VERSION = '%d.%d.%d' % (MAJ, MIN, REV)


setup(
    name='mygwas',
    version=VERSION,
    description='CSE185 Final GWAS',
    author='Elliott Ou',
    author_email='elou@ucsd.edu',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mygwas=mygwas.mygwas:main"
        ],
    },
)

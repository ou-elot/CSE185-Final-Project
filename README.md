# CSE185-Final-Project
UCSD CSE 185 Spring 2024 Final Project Elliott Ou, Audria Montalvo, and Leny Lei

## Note to peer reviewers
The command currently does not run and we are working on fixing the main. In the meantime, please copy and paste the code from mygwas_tools.py into datahub. 

# MyGWAS

MyGWAS is a command line tool designed to perform Genome-Wide Association Studies (GWAS). It processes genotype and phenotype data, conducts linear regression to obtain statistical associations, and generates visualizations such as Manhattan plots and QQ plots.

## Features
- Read and preprocess genotype data from VCF files.
- Read phenotype data from text files.
- Conduct linear regression to obtain beta coefficients and p-values.
- Generate Manhattan plots and QQ plots for visualizing GWAS results.

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- qqman (or equivalent package for GWAS plotting)

## Installation
Clone the directory into your own terminal. 
```
git clone https://github.com/ou-elot/CSE185-Final-Project
```

Download the requirements.
```
pip install -r requirements.txt
```

Run the following commands in the terminal to ensure installation is successful.
```
export PATH=$PATH=$HOME/.local/bin
export PYTHONPATH=$HOME/lib/python3.9/site-packages
python setup.py install --prefix=$HOME
```

You should now be able to run the command. Type the following to check:
```
mygwas --help
```

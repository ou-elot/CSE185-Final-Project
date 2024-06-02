# CSE185-Final-Project
UCSD CSE 185 Spring 2024 Final Project Elliott Ou, Audria Montalvo, and Lenny Lei

![MyGWAS (1)](https://github.com/ou-elot/CSE185-Final-Project/assets/76548988/0a250a80-426d-4cd0-ac96-cb94e33740d9)

MyGWAS is a command line tool designed to perform **Genome-Wide Association Studies (GWAS)**. It processes genotype and phenotype data, conducts linear regression to obtain statistical associations, and generates Manhattan plots and QQ plots as visualization.

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
Now change directory into the project folder:

```
cd CSE185-Final-Project
```
Download the requirements. QQman package requires its own command. 
```
pip install -r requirements.txt
pip install qqman
```

Run the following commands in the terminal before installation to ensure installation is successful.
```
export PATH=$PATH:$HOME/.local/bin
export PYTHONPATH=$HOME/lib/python3.9/site-packages
```

Both installation commands below need to be ran:
```
python setup.py install --prefix=$HOME
pip install . #do not forget the period!
```

You should now be able to run the command. Type the following to check:
```
mygwas --help

```
>[!IMPORTANT]
>  Try the following if the command above doesnt work
> ```
>  mygwas -h
>  ```



Should see:

![help_message](https://github.com/ou-elot/CSE185-Final-Project/assets/76548988/81f6033d-3860-43ce-ae4c-179fd70a5369)


## Usage
The MyGwas tool is a command line tool that takes in a vcf file containing genotypes and a csv file containing phenotypes, and ouputs files to the current directory. In the current version, the program only takes files as input if they are in the current working directory.
```
usage: mygwas --geno [genotype file] --pheno [phenotype file] 
example: mygwas --geno geno.vcf --pheno pheno.phen
testing: mygwas --geno gwas_test.vcf  --pheno lab3_gwas.phen
```
Output files will be named the following:
```
p-values and beta values: linreg.txt
qq-plot: qq.png
manhattan plot: manhattan.png
```

import argparse
from mygwas.mygwas_tools import *
import argparse
import os
import sys

def main():
    """
    This function serves as the entry point for the command line script `mygwas`.
    It parses command line arguments to perform GWAS, including reading genotype
    and phenotype files, conducting linear regression, and generating plots.
  
    Command Line Arguments:
    -----------------------
    --geno (str): Path to the VCF file containing genotype data.
    --pheno (str): Path to the text file containing phenotype data.
    """
    parser = argparse.ArgumentParser(
        prog = "mygwas",
        description = "Command Line Script to perform gwas"
    )
    #Input
    parser.add_argument("--geno", help="vcf file of a genome that contains genotype", type = str)
    parser.add_argument("--pheno", help="txt file that contains phenotypes of a genome", type = str)
    args = parser.parse_args()

    if not os.path.isfile(args.geno) or not os.path.isfile(args.pheno):
        print("Invalid file path.")
        sys.exit(1)
    else:
        geno = args.geno
        pheno = args.pheno
        gwas(geno, pheno)
        sys.exit(0)
  
if __name__ == "__main__":
    main()     

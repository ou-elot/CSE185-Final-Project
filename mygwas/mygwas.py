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
    
    #ANSI color codes for formatting
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m' 
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    
    #Pareser setup
    parser = argparse.ArgumentParser(
        #prog = "mygwas",
        #description = "Command Line Script to perform gwas"
        prog=f"{BLUE}mygwas",
        description=(
            f"{PINK}============================================================\n"
            f"{BOLD}                 GWAS Command Line Tool \n"
            "============================================================\n"
            f"This tool performs {CYAN}Genome-Wide Association Studies (GWAS){PINK}.\n"         
            "It processes genotype and phenotype data, conducts linear regression \n"
            "to obtain statistical associations, and generates visualizations such \n" 
            "as Manhattan plots and QQ plots.\n"
            "------------------------------------------------------------\n"
            f"Example usage:\n"
            f"{BLUE}mygwas --geno path/to/genotype.vcf --pheno path/to/phenotype.phen {PINK}\n"
            "============================================================ {WHITE} "
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    #Input
    #parser.add_argument("--geno", help="vcf file of a genome that contains genotype", type = str)
    #parser.add_argument("--pheno", help="txt file that contains phenotypes of a genome", type = str)
    parser.add_argument(
        "--geno", 
        help=f"{BLUE}VCF file that contains genotype data{PINK}", 
        type = str,
        required = True
    )
    parser.add_argument(
        "--pheno", 
        help = f"{BLUE}PHENO file that contains phenotype data {WHITE}", 
        type = str,
        required = True
    )
    args = parser.parse_args()

    #Check if file exists
    if not os.path.isfile(args.geno) or not os.path.isfile(args.pheno):
        print("Invalid file path.")
        sys.exit(1)
    else:
        #Inputs as parameters for GWAS program
        geno = args.geno
        pheno = args.pheno
        gwas(geno, pheno) 
        print("Complete!")
        sys.exit(0)
  
if __name__ == "__main__":
    main()     

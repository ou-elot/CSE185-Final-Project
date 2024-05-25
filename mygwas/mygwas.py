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
  --output (str): Directory where the output files will be saved. Must include trailing '/'.
  --graphs (bool): Flag indicating whether to generate Manhattan and QQ plots.
  --linreg (bool): Flag indicating whether to conduct linear regression to obtain beta and p-values.
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
  if not os.path.isdir(args.out):
      print("Invalid output directory.")
  else:
  print("Reading statistics file...")
  geno = args.geno
  pheno = args.pheno
  print("conducting linear regression...")
  gwas(geno, pheno)
  sys.exit(0)
  
if __name__ == "__main__":
  main()     

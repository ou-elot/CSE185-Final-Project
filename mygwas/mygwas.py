import argparse
from mygwas.mygwas_tools import *
import argparse
import os

def main():
  parser = argparse.ArgumentParser(
    prog = "mygwas",
    description = "Command Line Script to perform gwas"
  )

  #Input
  parser.add_argument("geno", help="vcf file of a genome that contains genotype", type = str)
  parser.add_argument("pheno", help="txt file that contains phenotypes of a genome", type = str)

  parser.add_argument("--manhattan", help="plot manhattan plot")
  parser.add_argument("--qq", help="plot QQ plot")
  parser.add_argument("--linreg", help="conduct linear regression to obtain beta and p-values")
  
  args = parser.parse_args()

  if args.input == '-h' or args.out == '-h':
    parser.print_help()
  elif not os.path.isfile(args.geno) or not os.path.isfile(args.pheno):
      print("Invalid file path.")
  elif not os.path.isdir(args.out):
      print("Invalid output directory.")
  else:
    print("Reading statistics file...")
    df = pd.read_csv(args.input, sep='\t')
    if args.linreg:
      print("conducting linear regression...")
      gwas(args.geno, args.pheno)

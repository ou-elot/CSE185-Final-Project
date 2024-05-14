import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def get_vcf(vcf_file):
  with gzip.open(vcf_path, "rt") as file:
          for line in file:
            if line.startswith("#CHROM"):
                  vcf = [x for x in line.split('\t')]
                  break
    file.close()
    return vcf

names = get_vcf('file.vcf.gz')
vcf = pd.read_csv('file.vcf.gz', compression='gzip', comment='#', chunksize=10000, delim_whitespace=True, header=None, names=names)

wget -O - "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000_genomes_project/release/20190312_biallelic_SNV_and_INDEL/ALL.chr14.shapeit2_integrated_snvindels_v2a_27022019.GRCh38.phased.vcf.gz" >> ~/Final/test.vcf.gz

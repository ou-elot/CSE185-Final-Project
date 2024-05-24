import io
import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from qqman import qqman

def genotype(genotype_path):
    """
    This function processes a genotype file and converts genotype data from a 
    string representation of alleles to their numeric sum. It reads the input
    file, iterates over the data, and updates the genotype values.

    Parameters
    ----------
    genotype_path (str): The path to the genotype file. The file is expected 
                         to be tab-separated and may contain comments starting
                         with '#'.
    Returns
    -------
    pd.DataFrame: A pandas DataFrame with updated genotype values, where each 
                  genotype is the sum of its alleles.
    """
    geno= pd.read_csv(genotype_path, comment="#", sep="\t", header = None)
    y=-1
    for index, row in geno.iterrows():
        y=y+1
        for i in range (9, len(geno.axes[1]) ):
            gt = row[i]
            alleles = gt.split("|") 
            alleles = [int(item) for item in alleles]
            final_genotype = sum(alleles)
            geno.at[y, i] = final_genotype 
    return geno


def getPhenotype(phenotype_path):
    phen = pd.read_csv(phenotype_path, sep='\t', header =None)
    return phen

def Linreg(gts, pts):
    """
    Perform a GWAS between the genotypes and phenotypes
    
    Parameters
    ----------
    gts : np.array of floats
        Genotypes (scaled to have mean 0, variance 1)
        of each person
    pts : np.array och personf floats
        Simulated phenotype value of each person
        
    Returns
    -------
    beta : float
        Estimated effect size
    pval : float
        P-value
    """
    X = sm.add_constant(gts)
    model = sm.OLS(pts, X)
    results = model.fit()
    beta = results.params[1]
    pval = results.pvalues[1]
    return beta, pval

def gwas (geno_file, pheno_file, output):
    """
     This function performs a Genome-Wide Association Study (GWAS) by 
    analyzing genotype and phenotype data. It reads the genotype and 
    phenotype files, performs linear regression for each SNP, and 
    outputs the results.

    Parameters
    ----------
    geno_file (str): The path to the genotype file (expected in VCF format).
    pheno_file (str): The path to the phenotype file.
    output (str): The path for the output file to save the GWAS results.

    Returns
    -------
    pd.DataFrame: A pandas DataFrame containing the GWAS results, with columns
                  for chromosome, SNP ID, base pair position, p-value, and 
                  regression coefficient (beta).
    """
    a = []
    genoCopy = genotype('gwas_test.vcf')
    geno = genotype('gwas_test.vcf')
    geno.drop(geno.columns[[0,1,2,3,4,5,6,7,8]], axis=1, inplace=True)
    pheno = getPhenotype('lab3_gwas.phen')
    pts = pheno[2]
    for index, row in geno.iterrows():
        gts = geno.iloc[index].to_numpy()
        gts = gts.astype(np.float)
        beta, pval = Linreg(gts, pts);
        b = [genoCopy[0][index], genoCopy[2][index], genoCopy[1][index], pval, beta]
        a.append(b)
    data = pd.DataFrame(a, columns = ['CHR', 'SNP', 'BP', 'P', 'BETA'])
    data.to_csv(output+'beta_pval.txt', sep='\t', index=False)
    return data

def graphs (gwas_data, output):
    """
    This function creates visualizations for Genome-Wide Association Study (GWAS) results.
    It reads the GWAS results from a file and generates a Manhattan plot and a QQ plot using the
    `qqman` library, then saves these plots to specified output files.

    Parameters
    ----------
    gwas_data (str): The path to the file containing GWAS results. The file is expected to be
                     in tab-separated format with columns for chromosome (CHR), SNP, base pair position (BP),
                     p-value (P), and beta coefficient (BETA).
    output (str): The base path for the output files to save the plots. The function will save
                  two plots: a Manhattan plot and a QQ plot, with filenames derived from this base path.
    """
    gwas = pd.read_csv((gwas_data), sep='\t')
    fig, (ax0, ax1) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [2, 1]})
    fig.set_size_inches((15, 5))
    qqman.manhattan(gwas, ax=ax0, out= output+"Manhattan.png")
    qqman.qqplot(gwas, ax=ax1, out=output+"qq.png")

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
    y = -1
    for index, row in geno.iterrows():
        y = y+1
        for i in range (9, len(geno.axes[1]) ):
            gt = row[i]
            alleles = gt.split("|") 
            alleles = [int(item) for item in alleles]
            final_genotype = sum(alleles)
            geno.at[y, i] = final_genotype 
    return geno


def getPhenotype(phenotype_path):
    phen = pd.read_csv(phenotype_path, sep='\t', header = None)
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
    
    # Getting the effect size anf p-val from results
    beta = results.params[1]
    pval = results.pvalues[1]
    return beta, pval


def filter_by_maf(geno_df, threshold):
    maf_filtered_columns = []
    for column in geno_df.columns:
        allele_counts = geno_df[column].value_counts()
        if len(allele_counts) < 2:
            continue
        maf = min(allele_counts[0], allele_counts[1]) / sum(allele_counts)
        if maf >= threshold:
            maf_filtered_columns.append(column)
    return geno_df[maf_filtered_columns]


def handle_missing_sex(phenotype_df):
    phenotype_df.fillna({'sex': 'Unknown'}, inplace=True)
    return phenotype_df


def gwas (geno_file, pheno_file):
    """
    This function performs a Genome-Wide Association Study (GWAS) by 
    analyzing genotype and phenotype data. It reads the genotype and 
    phenotype files, performs linear regression for each SNP, plots the 
    data into qq and manhattan plots, and exports the pvalues, qq plots, 
    and manhattan plots as files into the current directory.

    Parameters
    ----------
    geno_file (str): The path to the genotype file (expected in VCF format).
    pheno_file (str): The path to the phenotype file.

    Returns
    -------
    pd.DataFrame: A pandas DataFrame containing the GWAS results, with columns
                  for chromosome, SNP ID, base pair position, p-value, and 
                  regression coefficient (beta).
    """
    results = []
    print("In progress: Reading files...")
    genoCopy = genotype(geno_file)
    geno = genotype(geno_file)
    genoCopy.drop(genoCopy.columns[[0,1,2,3,4,5,6,7,8]], axis=1, inplace=True)
    
    pheno = getPhenotype(pheno_file)
    print("In progress: Conducting Linear Regression...")
    pts = pheno[2]

    # Linear Regression for each SNP
    for index, row in genoCopy.iterrows():
        gts = genoCopy.iloc[index].to_numpy()
        gts = gts.astype(np.float)
        beta, pval = Linreg(gts, pts);
        toAdd = [geno[0][index], geno[2][index], geno[1][index], pval, beta]
        results.append(toAdd)

    # Dataframe from results
    data = pd.DataFrame(results, columns = ['CHR', 'SNP', 'BP', 'P', 'BETA'])
    
    # Save dataframe of GWAS results 
    data.to_csv('linreg.txt', sep='\t')

    # Perform Manhattan plot
    print("In progress: Generating Manhattan plot...")
    fig = plt.figure()
    fig, (ax0) = plt.subplots(1, gridspec_kw={'width_ratios': [1]})
    fig.set_size_inches((5, 5))
    qqman.manhattan(data, ax=ax0, out= "Manhattan.png")

    # Perform QQ plot
    print("In progress: Generating QQ plot...")
    fig2 = plt.figure()
    fig2.set_size_inches((5, 5))
    fig2, (ax1) =  plt.subplots(1, gridspec_kw={'width_ratios': [1]})
    qqman.qqplot(data, ax=ax1, out= "qq.png")
    return data

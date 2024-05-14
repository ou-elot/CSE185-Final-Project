import numpy as np
import statsmodels.api as sm

def LinearRegression(geno, pheno):
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

def getGenotype(vcf_file):
    pd.read_csv(vcf_file, comment="#", sep="\t", names=column_name)
    column_name = []
    with open(vcf_file, 'r') as file:
        for line in file:
            if line.startswith('#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT'):
                column_name = line.split('\t')
                column_name[0] = column_name[0][1:]  # remove #
                column_name[-1] = column_name[-1][:-1]  # remove \n
        
        
    pd.read_csv(vcf_file, comment="#", sep="\t", names=column_name)

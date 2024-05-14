import numpy as np

def SimulateGenotypes(maf, N):
    """
    Simulate genotypes for N samples with minor 
    allele frequency maf (assuming HWE)
    
    Parameters
    ----------
    maf : float
        Minor allele frequency of the SNP
    N : int
        Sample size (number of people)
        
    Returns
    -------
    gts : np.array of floats
        Genotypes (scaled to have mean 0, variance 1)
        of each person
    """
    gts = []
    for i in range(N):
        gt = sum(random.random() < maf)+sum(random.random() < maf)
        gts.append(gt)
    # Technical note: scale to have mean 0 var 1
    gts = np.array(gts)
    gts = (gts-np.mean(gts))/np.sqrt(np.var(gts))
    return gts

def SimulatePhenotype(gts, Beta):
    """
    Simulate phenotypes under a linear model Y=beta*X+error
    
    Parameters
    ----------
    gts : np.array of floats
        Genotypes of each person
    Beta : float
        Effect size
        
    Returns
    -------
    pts : np.array och personf floats
        Simulated phenotype value of each person
    """
    if Beta<-1 or Beta>1:
        print("Error: Beta should be between -1 and 1")
        return [None]*len(pts)
    pts = Beta*gts + np.random.normal(0, np.sqrt(1-Beta**2), size=len(gts))
    return pts

import statsmodels.api as sm

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

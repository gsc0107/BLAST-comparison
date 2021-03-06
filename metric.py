import numpy as np
import pandas as pd
import ml_metrics as metrics
import sys
import os

# input all methods Blast,Diamond...
file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]
file4 = sys.argv[4]
file5 = sys.argv[5]
file6 = sys.argv[6]
file7 = sys.argv[7]
n=0

#extract name of file
base = os.path.basename(file1)
base = os.path.splitext(base)[0]
prot, no = base.split("_", 1)

blast = pd.read_csv(file1, sep='\t', header=None)
diamond = pd.read_csv(file2, sep='\t', header=None)
clustal = pd.read_csv(file3, sep='\t', header=None)
usearch = pd.read_csv(file4, sep='\t', header=None)
blastfast = pd.read_csv(file5,sep='\t', header=None)
mmseq = pd.read_csv(file6,sep='\t', header=None)
uselocal = pd.read_csv(file7, sep='\t', header=None)

#change column name
blast.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
diamond.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
clustal.columns = ['id_orth', 'id_prot', 'persent']
usearch.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
blastfast.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
mmseq.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
uselocal.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']

id_orth_blast = blast['id_orth']
id_orth_diam = diamond['id_orth']
id_orth_clust = clustal['id_orth']
id_orth_use = usearch['id_orth']
id_orth_blastfast = blastfast['id_orth']
id_orth_mmseq = mmseq['id_orth']
id_orth_useloc = uselocal['id_orth']

# identify column lengh 
k_blast = len(id_orth_blast.index)
k_dia = len(id_orth_diam.index)
k_use = len(id_orth_use.index)
k_blastfast = len(id_orth_blastfast.index)
k_mmseq = len(id_orth_mmseq.index)
k_useloc = len(id_orth_useloc.index)

print ("BLAST")
print ("DIAMOND")
print ("USEARCH")
print ("BLAST_FAST", "k")
print ("MMSEQ2")
print ("USE_LOCAL")

# function of metric
def stop (x,y,z):
    if len(x) > z:
       sys.exit()
    else:
       return metrics.apk(x,y,z)

# metric calculation
while n < 100:
    actual = id_orth_clust.to_list()[:n]
    n = n + 1
    apk_blast = stop(actual,id_orth_blast.to_list(), k_blast)
    apk_blastfast = stop(actual,id_orth_blastfast.to_list(), k_blastfast)
    apk_dia = stop(actual,id_orth_diam.to_list(), k_dia)
    apk_use = stop(actual,id_orth_use.to_list(), k_use)
    apk_mmseq = stop(actual,id_orth_mmseq.to_list(), k_mmseq)
    apk_useloc = stop(actual,id_orth_useloc.to_list(), k_useloc)
    print (apk_blast)
    print (apk_blastfast, n)
    print (apk_dia)
    print (apk_use)
    print (apk_mmseq)
    print (apk_useloc)


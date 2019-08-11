import pandas as pd
import sys

SMILES = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        SMILES.append(line.split()[0])

df = pd.DataFrame(SMILES, columns=['structure'])
df.to_hdf(sys.argv[2], "table")
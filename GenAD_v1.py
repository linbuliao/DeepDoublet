import numpy as np
import random
import pandas as pd
import os
import argparse
from scipy import sparse

parser = argparse.ArgumentParser(description='Generate artificial doublets'
           'Gene count matrices normalized to CPM are saved as .npy files.'
           'Sources of single cells and mixing factors are save in *_meta.csv.')

parser.add_argument('--s1',\
                    type = str,\
                    help = 'Path to processed singlets 1 UMI .csv file.'
                    'The first column of the file should contain gene names.'
                    'The first row of the file should contain cell names.',\
                    required = True)

parser.add_argument('--s2',\
                    type = str,\
                    help = 'Path to processed singlets 2 UMI .csv file.'
                    'The first column of the file should contain gene names.'
                    'The first row of the file should contain cell names.',\
                    required = True)

parser.add_argument('--sampleSize',\
                    type = int,\
                    help = 'Number of artificial doublets.',\
                    required = True)

parser.add_argument('--name1',\
                    type = str,\
                    help = 'Cell type of singlets 1. Default s1.',\
                    required = False)

parser.add_argument('--name2',\
                    type = str,\
                    help = 'Cell type of singlets 2. Default s2.',\
                    required = False)

parser.add_argument('--output',\
                    type = str,\
                    help = 'Output prefix. Default ADoub.')

parser.add_argument('--outdir',\
                    type = str,\
                    help = 'Output directory. Default None.')

parser.add_argument('--sparse',\
                    action = 'store_true',
                    help = 'Output artificial doublet matrix in scipy sparse matrix format.')

parser.add_argument('--indir',\
                    type = str,\
                    help = 'Input directory. Default None.')

args = parser.parse_args()

if(args.name1 == None):
    name1 = 's1'
else:
    name1 = args.name1

if(args.name2 == None):
    name2 = 's2'
else:
    name2 = args.name2

if(args.output == None):
    output = 'ADoub'
else:
    output = args.output

if(args.outdir == None):
    outdir = ''
else:
    outdir = args.outdir + '/'
    if not os.path.exists(outdir):
        os.makedirs(outdir)

if(args.indir == None):
    indir = ''
else:
    indir = args.indir + '/'

s1_mat = pd.read_csv(indir + args.s1, index_col=0).values
s2_mat = pd.read_csv(indir + args.s2, index_col=0).values

def gen_adoub(s1_mat,\
              s2_mat,\
              s1_name = '1',\
              s2_name = '2',\
              sample_size = 1000,\
              MFs = np.array(range(1, 10))/ 10):
    
    s1_list = list(range(s1_mat.shape[1]))
    s2_list = list(range(s2_mat.shape[1]))

    random_cell_1 = random.choices(s1_list, k = sample_size)
    random_cell_2 = random.choices(s2_list, k = sample_size)

    MF1 = np.array(random.choices(MFs, k = sample_size))
    MF2 = 1 - MF1

    ADoub = MF1 * s1_mat[:, random_cell_1] + MF2 * s2_mat[:, random_cell_2]

    columns = [s1_name, 'MF_'+s1_name, s2_name, 'MF_' + s2_name]
    ADoub_meta = pd.DataFrame([random_cell_1, MF1, random_cell_2, MF2]).T
    ADoub_meta.columns = columns
        
    return ADoub.T, ADoub_meta

ADoub, ADoub_meta = gen_adoub(s1_mat,\
                              s2_mat,\
                              name1, name2, sample_size = args.sampleSize)

ADoub = ADoub / ADoub.sum(axis = 1).reshape((-1, 1)) * 1e6

ADoub_meta.to_csv(outdir + output + '_meta.csv', index = None)

if(args.sparse):
    ADoubs_sparse = sparse.csr_matrix(ADoub.values)
    sparse.save_npz(outdir + output + '_sparse.npz', ADoub_sparse)
else:
    np.save(outdir + output + '.npy', ADoub)

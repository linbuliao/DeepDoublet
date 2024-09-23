DeepDoublet: A tool for high-resolution doublet decomposition based on deep learning
====================================================================================
A tool for decomposing a doublet (mixed two single cells when sequencing) into two single cells based on their trascriptome.

The matrices in "umi" folder only included expression values of 8,676 selected genes, while the matrices in "FullGenes" folder reserved information of all available genes.
## Hardware requirement
* Disk space and memory  
To generate 400k artificial doublets wiht around 9k genes included, you will need around 30GB disk space and 60GB memory.
* GPU  
To train a model on 400k artificial doublets with information of 9k genes. At least a 10GB GTX 3080 is required.  
In our application, we finished the training in half an hour with a 24GB Titan RTX.   
## Environment
Anaconda is needed to set a proper Python environment for running DeepDoublet:
```
conda env create --file environment.yml
source activate DeepDoublet
```
## Generate artificial doublets
```
python GenAD_v1.py -h
```
* Example
Generate 400,000 hepatocyte-LEC doublets
```
python GenAD_v1.py --s1 umi/hep_umi.csv --s2 umi/LEC_umi.csv --sampleSize 400000 --outdir ADoub_new
```

# Artificial Doublets Storage and Composition

The artificial doublets are organized and stored as follows:

## Directory Structure

- **Folder:** `ADoub_new`
  - **Files:**
    - `ADoub.npy`  
      Contains all artificial doublets as a NumPy array.
    - `ADoub_meta.csv`  
      Stores the composition metadata for each artificial doublet.

- **Folder:** `umi`
  - **Files:**
    - `LEC_umi.csv`  
      Contains UMI (Unique Molecular Identifier) counts for LEC cells.
    - `hep_umi.csv`  
      Contains UMI counts for HEP cells.

## Metadata File: `ADoub_meta.csv`

This CSV file contains the composition information for each artificial doublet. Each row corresponds to an artificial doublet stored in `ADoub.npy`.

| Column  | Description                                      |
|---------|--------------------------------------------------|
| `s1`    | Index of the first single cell                   |
| `MF_s1` | Proportion of the first single cell (`s1`)       |
| `s2`    | Index of the second single cell                  |
| `MF_s2` | Proportion of the second single cell (`s2`)      |

## Single Cell Data

Single cell transcriptome information is stored in the `umi` folder. The folder contains two CSV files:

- **Files:**
  - `LEC_umi.csv`  
    - **Row Names:** Gene names  
    - **Column Names:** Cell names  
    - **Description:** UMI counts for LEC cells. Only selected genes are included.
  
  - `hep_umi.csv`  
    - **Row Names:** Gene names  
    - **Column Names:** Cell names  
    - **Description:** UMI counts for HEP cells. Only selected genes are included.

**Notes:**
- Ensure that the gene names across `LEC_umi.csv` and `hep_umi.csv` are consistent if they are to be used together.
- The selected genes in these CSV files should correspond to the genes used in downstream analyses.

## Transcriptome Calculation

The transcriptome of each artificial doublet is calculated using the following formula:

Transcriptome_ADoub = Transcriptome_s1 X MF_s1 + Transcriptome_s2 X MF_s2

**Where:**
- **Transcriptome\_s1**: Transcriptome data of the first single cell (`s1`)
- **MF\_s1**: Proportion of the first single cell in the doublet
- **Transcriptome\_s2**: Transcriptome data of the second single cell (`s2`)
- **MF\_s2**: Proportion of the second single cell in the doublet

For example, if `s1`, `MF_s1`, `s2`, `MF_s2` are `596`, `0.7`, `250`, `0.3` respectively. The corresponding artificial doublet is

Transcriptome_s1_596 X 0.7 + Transcriptome_s2_250 X 0.3


## Example Implementation in Python

```python
import numpy as np
import pandas as pd

# Paths to the metadata and doublets
meta_path = 'ADoub_new/ADoub_meta.csv'
doublets_path = 'ADoub_new/ADoub.npy'
lec_umi_path = 'umi/LEC_umi.csv'
hep_umi_path = 'umi/hep_umi.csv'

# Load metadata
metadata = pd.read_csv(meta_path)

# Load single cell transcriptomes
# Load LEC and HEP UMI counts
lec_umi = pd.read_csv(lec_umi_path, index_col=0)
hep_umi = pd.read_csv(hep_umi_path, index_col=0)

# Load artificial doublets
ADoub = np.load(doublets_path)


## Workflow
* Train Decomposition Model  
Decomposition_Training.ipynb
* Predict with Decomposition Model  
Decomposition_Predict.ipynb
* Differential Expression Analysis\
DEA.ipynb
## Logistic Regression
* Program\
LR.py
* LOG file\
LR.log

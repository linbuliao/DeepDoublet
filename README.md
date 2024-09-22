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
The artificial doublets were saved to the folder ADoub_new under the current path. The composition information of the artificial doublets is stored in ADoub_meta.csv. The first column "s1" is the order of the first single cell. The second column "MF_s1" indicates the proportion of the first single cell. The third column "s2" is the order of the second single cell. The fourth column "MF_s2" is the proportion of the second single cell.
__Transcriptome_ADoub = Transcriptome_s1 * MF_s1 + Transcriptome_s2 * MF_s2__
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

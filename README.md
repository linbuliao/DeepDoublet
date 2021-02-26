DeepDoublet: A Deep-learning-based Doublet Decomposition Tool
================================================================
A tool for decomposing doublet (mixed two single cells when sequencing) to two single cells based on their trascriptome.

The matrices in "umi" folder only included expression values of 8,676 selected genes, while the matrices in "FullGenes" folder reserved information of all available genes.
## Hardware requirement
* Disk space and memory  
To generate 400k artificial doublets wiht around 9k genes included, you will need around 30 GigaByte disk space and 60 GigaByte memory.
* GPU  
To train a model on 400k artificial doublets with information of 9k genes. At least a 10 GB GTX 3080 is required.  
In our application, we finished the training in half an hour with a Titan RTX.   
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

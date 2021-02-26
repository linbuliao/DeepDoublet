DeepDoublet: A Deep-learning-based Doublet Decomposition Tool
================================================================
A tool for decomposing doublet (mixed two single cells when sequencing) to two single cells based on their trascriptome.

## Generate artificial doublets
* Example
```
python GenAD_v1.py -h
```
Generate 400,000 hepatocyte-LEC doublets
```
python GenAD_v1.py --s1 umi/hep_umi.csv --s2 umi/LEC_umi.csv --sampleSize 400000 --outdir ADoub_new
```
## Workflow
* Train Decomposition Model
Decomposition_Training.ipynb
* Predict with Decomposition Model
Decomposition_Predict.ipynb
* Differential Expression Analysis
DEA.ipynb
## Logistic Regression
__Program__ LR.py
__LOG file__ LR.log

DeepDoublet: A Deep-learning-based Doublet Decomposition Tool
================================================================
A tool for decomposing doublet (mixed two single cells when sequencing) to two single cells based on their trascriptome.

## Generate artificial doublets
* Example
Generate 400,000 hepatocyte-LEC doublets
```
python GenAD_v1.py --s1 umi/hep_umi.csv --s2 umi/LEC_umi.csv --sampleSize 400000 --outdir ADoub_new
```
## Workflow


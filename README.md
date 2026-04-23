# SMAHD：a scalable graph autoencoder for spatial multi-omics analysis of high-resolution spatial transcriptomics data

<img width="2850" height="1924" alt="框架图" src="https://github.com/user-attachments/assets/7689fb76-6bab-4f3f-a8ca-010c46686150" />

High-resolution spatial multi-omics technologies now enable the joint measurement of transcriptomic, proteomic, and epigenomic signals within intact tissues,
but the resulting datasets remain difficult to analyze because of severe crossmodal heterogeneity, transcriptomic sparsity, and the memory cost of full-graph
learning. Existing integration methods perform well on moderate-scale data, yet
often become impractical when spatial resolution increases or when multiple
omics views must be modeled jointly.
We present SMAHD (Scalable graph autoencoder for spatial Multi-omics Analysis of High-resolution spatial omics Data), a scalable graph autoencoder for
high-resolution spatial multi-omics integration. SMAHD combines micro-clusterbased subgraph sampling with parallel view-specific graph attention encoders and
a weighted multi-view reconstruction objective. This design preserves local spatial topology while enabling efficient training on large graphs under limited GPU
memory.
Across simulated and real spatial multi-omics datasets, including human tonsil,
mouse brain transcriptome–epigenome data, and large Stereo-CITE-seq mouse
spleen data, SMAHD achieves strong clustering accuracy, favorable algorithmic
stability, and substantially lower memory usage than competing methods. In
particular, SMAHD maintains a peak GPU memory footprint below 500 MiB
across Stereo-CITE-seq resolution levels up to 756,430 spatial locations while
preserving robust performance under extreme high-resolution sparsity.
These results show that SMAHD provides a practical and accurate framework for
scalable spatial multi-omics integration in next-generation high-resolution spatial
omics studies.

# Installation

SMAHD is built with Scanpy, PyTorch, and PyG, and supports both GPU (preferred) and CPU execution.
First clone the repository.

```
git clone https://github.com/Little-Eel/SMAHD.git
cd SMAHD
```

It's recommended to create a separate conda environment for running SMAHD:

```
#create an environment called env_SMAHD
conda create -n env_SMAHD python=3.8

#activate your environment
conda activate env_SMAHD
```

Install all the required packages.
For Linux

```
pip install -r requirements.txt
```

For MacOS

```
pip install -r requirements_for_macOS.txt
```

The use of the mclust algorithm requires the rpy2 package (Python) and the mclust package (R). See https://pypi.org/project/rpy2/ and https://cran.r-project.org/web/packages/mclust/index.html for detail.

The torch-geometric library is also required, please see the installation steps in https://github.com/pyg-team/pytorch_geometric#installation

Install SMAHD.

```
python setup.py build
python setup.py install
```

# Datasets

All spatial transcriptomics datasets used in this study are publicly available. Detailed sources and download links are listed below:10x Visium human dorsolateral prefrontal cortex (DLPFC) da-taset and tutorials:
https://support.10xgenomics.com/spatial-gene-expression/datasets/1.2.0/V1_Human_DLPFC .

Xenium platform whole adult mouse brain dataset (xenium_whole_adult_mouse),including data and tutorials:
https://www.10xgenomics.com/datasets/xenium-prime-ffpe-neonatal-mouse. 

CosMx SMI human lymph node dataset (Cosmx lymph) from NanoS-tring:https://nanostring.com/products/cosmx-spatial-molecular-imager/ffpe-dataset/cosmx-human-lymph-node-ffpe-dataset/. 

10x Genomics Visium-HD human breast cancer dataset (FFPE-IF):
https://www.10xgenomics.com/datasets/visium-hd-cytassist-gene-expression-libraries-human-breast-cancer-ffpe-if. 

10x Genomics Visium-HD human tonsil dataset (fresh frozen, IF):
https://www.10xgenomics.com/datasets/visium-hd-cytassist-gene-expression-human-tonsil-fresh-frozen-if

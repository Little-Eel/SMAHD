# SMAHD：a scalable graph autoencoder for spatial multi-omics analysis of high-resolution spatial transcriptomics data

<img width="2850" height="1924" alt="框架图" src="https://github.com/user-attachments/assets/7689fb76-6bab-4f3f-a8ca-010c46686150" />

High-resolution spatial multi-omics technologies now enable the joint measurement of transcriptomic, proteomic, and epigenomic signals within intact tissues, but the resulting datasets remain difficult to analyze because of severe crossmodal heterogeneity, transcriptomic sparsity, and the memory cost of full-graph learning.Existing integration methods perform well on moderate-scale data, yet often become impractical when spatial resolution increases or when multiple omics views must be modeled jointly.

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



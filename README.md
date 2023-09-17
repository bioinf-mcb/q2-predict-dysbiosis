# q2-predict-dysbiosis

QIIME 2 plugin for calculating the dysbiosis score from gut microbiome data. 

## Installation

To install the most up to date version of the plugin:

- Install and activate conda environment with QIIME 2 (see [docs](https://docs.qiime2.org/2020.11/install/native/)), e.g. for Linux 64-bit:
    ```
    wget https://data.qiime2.org/distro/core/qiime2-2022.2-py38-linux-conda.yml
    conda env create -n qiime2-2022.2 --file qiime2-2022.2-py38-linux-conda.yml
    rm qiime2-2022.2-py38-linux-conda.yml
    source activate qiime2-2022.2
    qiime --help
    ```
Note that the plugin was tested with `qiime2-2022.2` .

- Fetch the repository and go to main folder:
    ```
    git clone https://github.com/Kizielins/q2-predict-dysbiosis.git
    cd q2-predict-dysbiosis
    ```
- Install plugin:
    `pip install -e`
    `python setup.py install`
  
- Test plugin e.g.: `qiime predict-dysbiosis --help`





## Acknowledgements

We would like to acknowledge the Authors of the q2-health-index plugin, whose scripts formed the foundation of our work. 

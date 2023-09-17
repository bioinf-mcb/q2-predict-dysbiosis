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
    ```
    pip install -e
    python setup.py install
    ```
  
- Test plugin e.g.: `qiime predict-dysbiosis --help`

**Input prep:**

Sample inputs can be found in the "test_data" folder.

- Taxonomy table: standard QIIME 2 *qza feature table, collapsed to species level, with removed "s__" and underscores instead of spaces (ie "Escherichia_coli")
- Stratified pathways table: standard QIIME 2 *qza feature table, collapsed to species level, with underscores instead of spaces (ie ANAEROFRUCAT-PWY:_homolactic_fermentation|g__Citrobacter.s__Citrobacter_freundii)
- Unstratified pathways table: standard QIIME 2 *qza feature table with underscores instead of spaces (ie AEROBACTINSYN-PWY:_aerobactin_biosynthesis)
- Metadata: standard QIIME 2 metadata format, with "id" and <custom> columns representing sample IDs and <custom> labelling.

The values in all tables should be expressed as relative abundance.

**Usage:** `qiime health-index gmhi-predict [OPTIONS]`  
Dysbiosis index predicts the gut microbiome health index for each sample in the abundance table. 

**Inputs:**  

`--i-table	ARTIFACT	FeatureTable[Frequency] or FeatureTable[RelativeFrequency]`  
Abundance table artifact on which GMHI will be computed.

**Parameters:**  

| Parameter   |  Type  |  Optional / required / default      |  Description |
|:-----|:-----:|:-------------:|:------|
| `--p-healthy-species-fp` | TEXT |  optional | Path to file with healthy species (taxonomy is based on MetaPhlAn 2). |
| `--p-non-healthy-species-fp` | TEXT |    optional   |   Path to file with non-healthy species (taxonomy is based on MetaPhlAn 2). |
| `--p-mh-prime`  | INTEGER | default: 7 |  Median from the top 1% healthy samples in training dataset (see Gupta et al. 2020 Methods section). |
| `--p-rel-thresh` | NUMBER  | default: 1e-05 | Median from the top 1% non-healthy samples in training dataset (see Gupta et al. 2020 Methods section).  |
| `--p-rel-thresh` | NUMBER | default: 1e-05 | Relative frequency based threshold for discarding insignificant OTU. |
| `--p-log-thresh` | NUMBER | default: 1e-05 | Normalization value for `log10` in the last step of GMHI calculation.  |

**Outputs:**

`--o-gmhi-results	ARTIFACT SampleData[AlphaDiversity]` Predicted GMHI in tabular form.





## Acknowledgements

We would like to acknowledge the Authors of the q2-health-index plugin, whose scripts formed the foundation of our work. 

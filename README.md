# q2-predict-dysbiosis

QIIME 2 plugin for calculating dysbiosis score from gut microbiome data. 

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
    pip install -e .
    python setup.py install
    ```
  
- Test plugin e.g.: `qiime predict-dysbiosis --help`

## Input prep:

Sample inputs can be found in the "test_data" folder.

- Taxonomy table: standard QIIME 2 *qza feature table, collapsed to species level, with removed "s__" and underscores instead of spaces (ie "Escherichia_coli")
- Stratified pathways table: standard QIIME 2 *qza feature table, collapsed to species level, with underscores instead of spaces (ie ANAEROFRUCAT-PWY:_homolactic_fermentation|g__Citrobacter.s__Citrobacter_freundii)
- Unstratified pathways table: standard QIIME 2 *qza feature table with underscores instead of spaces (ie AEROBACTINSYN-PWY:_aerobactin_biosynthesis)
- Metadata: standard QIIME 2 metadata format, with "id" and <custom> columns representing sample IDs and <custom> labelling.

The values in all tables should be expressed as relative abundance.

## Predict dysbiosis index
**Usage:** `qiime predict-dysbiosis calculate-index [OPTIONS]`  
Dysbiosis index predicts the gut microbiome health index for each sample in the abundance table. 

**Inputs:**  

`--i-table	ARTIFACT	FeatureTable[RelativeFrequency]`  
Abundance table artifact with taxonomy collapsed to species level.

`--i-pathways-stratified	ARTIFACT	FeatureTable[RelativeFrequency]`  
Abundance table artifact with stratified pathways.

`--i-pathways-unstratified	ARTIFACT	FeatureTable[RelativeFrequency]`  
Abundance table artifact with unstratified pathways.

**Outputs:**

`--o-dysbiosis-predictions	ARTIFACT SampleData[AlphaDiversity]`  
Predicted dysbiosis index in tabular form.

## Predict and visualize dysbiosis index

**Usage:** `qiime predict-dysbiosis calculate-index-viz [OPTIONS]`  
Dysbiosis index predicts the gut microbiome health index for each sample in the abundance table. 

**Inputs:**  

`--i-table	ARTIFACT	FeatureTable[RelativeFrequency]`  
Abundance table artifact with taxonomy collapsed to species level.

`--i-pathways-stratified	ARTIFACT	FeatureTable[RelativeFrequency]`  
Abundance table artifact with stratified pathways.

`--i-pathways-unstratified	ARTIFACT	FeatureTable[RelativeFrequency]`  
Abundance table artifact with unstratified pathways.

`--m-metadata-file	ARTIFACT`  
Metadata file.

**Outputs:**

`--o-index_results	ARTIFACT SampleData[AlphaDiversity]`  
Predicted dysbiosis index in tabular form.

`--o-index_results	ARTIFACT Visualization`  
Predicted dysbiosis index visualization file.



## Acknowledgements

We would like to acknowledge the Authors of the q2-health-index plugin, whose scripts formed the foundation of our work. 

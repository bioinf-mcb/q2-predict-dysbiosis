# q2-predict-dysbiosis

QIIME 2 plugin for calculating dysbiosis score from gut microbiome data. A greater score indicates better health.

## Installation

To install the most up to date version of the plugin:

- Install and activate conda environment with QIIME 2 (see [docs](https://docs.qiime2.org/2020.11/install/native/)), e.g. for Linux 64-bit. Note that this plugin is currently only available in the QIIME 2 dev version. This should only take a few minutes:
    ```
    wget https://raw.githubusercontent.com/qiime2/environment-files/master/latest/staging/qiime2-latest-py38-linux-conda.yml
    conda env create -n qiime2-dev --file qiime2-latest-py38-linux-conda.yml
    rm qiime2-latest-py38-linux-conda.yml
    source activate qiime2-2022.2
    conda activate qiime2-dev
    qiime info
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
- Stratified pathways table: standard QIIME 2 *qza feature table, produced by HUMAnNN, collapsed to species level, with underscores instead of spaces (ie ANAEROFRUCAT-PWY:_homolactic_fermentation|g__Citrobacter.s__Citrobacter_freundii)
- Unstratified pathways table: standard QIIME 2 *qza feature table, produced by HUMAnNN, with underscores instead of spaces (ie AEROBACTINSYN-PWY:_aerobactin_biosynthesis)
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
 
## Sample use

Calculate index: 
```
qiime predict-dysbiosis calculate-index --i-table test_files/taxonomy.qza --i-pathways-stratified test_files/pathways_stratified.qza --i-pathways-unstratified test_files/pathways_unstratified.qza --o-dysbiosis-predictions results.qza
```
Calculate and visualize index:
```
qiime predict-dysbiosis calculate-index-viz --i-table test_files/taxonomy.qza --i-pathways-stratified test_files/pathways_stratified.qza --i-pathways-unstratified test_files/pathways_unstratified.qza --m-metadata-file test_files/metadata.txt --o-index-results results.qza --o-index-plot visualization.qzv
```
## Acknowledgements

We would like to acknowledge the Authors of the q2-health-index plugin, whose scripts formed the foundation of our work. 

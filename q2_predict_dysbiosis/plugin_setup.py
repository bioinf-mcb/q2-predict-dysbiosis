# -----------------------------------------------------------------------------
# Copyright (c) 2023, Bioinformatics at Małopolska Centre of Biotechnology
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------


from qiime2.plugin import (Int, Str, Float, Plugin, Citations, Metadata,
                           Visualization)
from q2_types.feature_table import FeatureTable, Frequency, RelativeFrequency
from q2_types.sample_data import SampleData, AlphaDiversity

import q2_predict_dysbiosis

from q2_predict_dysbiosis._dysbiosis_predictor import calculate_index, calculate_index_viz


basic_parameters = {}

basic_parameters_descriptions = {}

plugin = Plugin(
    name='predict-dysbiosis',
    version=q2_predict_dysbiosis.__version__,
    website='https://github.com/Kizielins/q2-predict-dysbiosis',
    package='q2_predict_dysbiosis',
    citations=Citations.load('citations.bib', package='q2_predict_dysbiosis'),
    description=('This QIIME 2 plugin predicts the degree of dysbiosis in human gut microbiome samples.'),
    short_description='Human gut microbiome dysbiosis predictor.'
)

plugin.pipelines.register_function(
    function=calculate_index,
    inputs={'table': FeatureTable[Frequency | RelativeFrequency], 'pathways_stratified': FeatureTable[Frequency | RelativeFrequency], 'pathways_unstratified': FeatureTable[Frequency | RelativeFrequency]},
    parameters=basic_parameters,
    outputs=[
        ('dysbiosis_predictions', FeatureTable[Frequency]) #SampleData[AlphaDiversity]) #FeatureTable[Frequency | RelativeFrequency]), # ),
    ],
    input_descriptions={'table': 'The feature frequency table with species', 'pathways_stratified': 'The feature frequency table with stratified pathways','pathways_unstratified': 'The feature frequency table with unstratified pathways'},
    parameter_descriptions=basic_parameters_descriptions,
    output_descriptions={
        'dysbiosis_predictions': 'Calculated GMHI in tabular form.',
    },
    name='Predict dysbiosis',
    description='Calculate Gut Microbial Health Index based on input data. '
)


plugin.pipelines.register_function(
    function=calculate_index_viz,
    inputs={'table': FeatureTable[Frequency | RelativeFrequency], 'pathways_stratified': FeatureTable[Frequency | RelativeFrequency], 'pathways_unstratified': FeatureTable[Frequency | RelativeFrequency]},

    parameters={
        **basic_parameters,
        'metadata': Metadata,
    },
    outputs=[
        ('index_results', SampleData[AlphaDiversity]),
        ('index_plot', Visualization)
    ],
    input_descriptions={'table': 'The feature frequency table with species', 'pathways_stratified': 'The feature frequency table with stratified pathways','pathways_unstratified': 'The feature frequency table with unstratified pathways'},
    parameter_descriptions={
        **basic_parameters_descriptions,
        'metadata': 'Metadata used for dysbiosis prediction visualization.',
    },
    output_descriptions={
        'index_results': 'Calculated dysbiosis score in tabular form.',
        'index_plot': 'Bar plot showing calculated dysbiosis score distribution.'
    },
    name='Calculate & visualize dysbiosis score',
    description='Calculate and plot dysbiosis predictions.'
)

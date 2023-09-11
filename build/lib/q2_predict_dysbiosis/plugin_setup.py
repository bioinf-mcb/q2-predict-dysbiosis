# -----------------------------------------------------------------------------
# Copyright (c) 2023, Bioinformatics at Małopolska Centre of Biotechnology
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

import q2_predict_dysbiosis

from q2_predict_dysbiosis._dysbiosis_predictor import calculate_index
from qiime2.plugin import (Int, Str, Float, Plugin, Citations, Metadata,
                           Visualization)
from q2_types.feature_table import FeatureTable, Frequency, RelativeFrequency
from q2_types.sample_data import SampleData, AlphaDiversity


basic_parameters = {}

basic_parameters_descriptions = {
        'healthy_species_fp': 'Path to file with healthy species (taxonomy ' 
                              'is based on MetaPhlAn 2).',
        'non_healthy_species_fp': 'Path to file with non-healthy species ' 
                                  '(taxonomy is based on MetaPhlAn 2).',
        'mh_prime': 'Median from the top 1% healthy samples in training  '
                    'dataset (see Gupta et al. 2020 Methods section).',
        'mn_prime': 'Median from the top 1% non-healthy samples in training '
                    'dataset (see Gupta et al. 2020 Methods section).',
        'rel_thresh': 'Relative frequency based threshold for discarding '
                      'insignificant OTU.',
        'log_thresh': 'Normalization value for log10 in the last step of '
                      'GMHI calculation.',
    }

plugin = Plugin(
    name='predict-dysbiosis',
    version=q2_predict_dysbiosis.__version__,
    #website="https://github.com/bioinf-mcb/q2-health-index",
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
        ('dysbiosis_predictions', FeatureTable[Frequency | RelativeFrequency]), # SampleData[AlphaDiversity]),
    ],
    input_descriptions={'table': 'The feature frequency table to calculate '
                                 'Gut Microbiome Health Index from.', 'pathways_stratified': 'The feature frequency table to calculate '
                                 'Gut Microbiome Health Index from.', 'pathways_unstratified': 'The feature frequency table to calculate '
                                 'Gut Microbiome Health Index from.'},
    parameter_descriptions=basic_parameters_descriptions,
    output_descriptions={
        'dysbiosis_predictions': 'Calculated GMHI in tabular form.',
    },
    name='Calculate GMHI',
    description='Calculate Gut Microbial Health Index based on input data. '
)

'''
plugin.pipelines.register_function(
    function=gmhi_predict_viz,
    inputs={
        'table': FeatureTable[Frequency | RelativeFrequency],
    },
    parameters={
        **basic_parameters,
        'metadata': Metadata,
    },
    outputs=[
        ('gmhi_results', SampleData[AlphaDiversity]),
        ('gmhi_plot', Visualization)
    ],
    input_descriptions={'table': 'The feature frequency table to calculate '
                                 'Gut Microbiome Health Index from.',
                        },
    parameter_descriptions={
        **basic_parameters_descriptions,
        'metadata': 'Metadata used for visualization [REQUIRED].',
    },
    output_descriptions={
        'gmhi_results': 'Calculated GMHI in tabular form.',
        'gmhi_plot': 'Bar plot showing calculated GMHI distribution.'
    },
    name='Calculate & visualize GMHI',
    description='Calculate and plot Gut Microbial Health Index based on '
                'input data and metadata. '
)
'''
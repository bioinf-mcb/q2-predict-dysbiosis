# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021, Bioinformatics at Małopolska Centre of Biotechnology
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

import pandas as pd
import pkg_resources

from qiime2.plugin import Metadata

def _load_file(file: str = None):
    with open(file, 'r') as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def _load_metadata(metadata: Metadata = None):
    if not metadata:
        raise ValueError('Metadata parameter not provided!')
    metadata = metadata.to_dataframe()
    return metadata


# Borrowed from q2_longitudinal
def _validate_metadata_is_superset(metadata: pd.DataFrame = None,
                                   table: pd.DataFrame = None):
    metadata_ids = set(metadata.index.tolist())
    table_ids = set(table.index.tolist())
    missing_ids = table_ids.difference(metadata_ids)
    if len(missing_ids) > 0:
        raise ValueError(f'Missing samples in metadata: {missing_ids}')
    # keep only relevant metadata
    metadata = metadata.loc[table_ids]
    return metadata


'''
def _validate_and_extract_healthy_states(metadata: pd.DataFrame = None,
                                         healthy_column: str = None,
                                         healthy_states: str = None,
                                         non_healthy_states: str = None):
    # Basic validations
    if not healthy_column:
        raise ValueError('healthy_column parameter not provided!')
    if not healthy_states:
        raise ValueError('healthy_states parameter not provided!')
    if not non_healthy_states:
        raise ValueError('non_healthy_states parameter not provided!')
    if healthy_column not in metadata.columns:
        raise ValueError(f'\'{healthy_column}\' is not a column in your '
                         f'metadata.')
    # States validation
    if not healthy_states == 'rest':
        healthy_states = list(set(healthy_states.split(",")))
        for state in healthy_states:
            if state not in metadata[healthy_column].values:
                raise ValueError(f'Healthy state \'{state}\' is not '
                                 f'represented by any members of '
                                 f'\'{healthy_column}\' column in metadata. '
                                 f'Consider using a different healthy_column '
                                 f'or state value.')
    if not non_healthy_states == 'rest':
        non_healthy_states = list(set(non_healthy_states.split(",")))
        for state in non_healthy_states:
            if state not in metadata[healthy_column].values:
                raise ValueError(f'Non-healthy state \'{state}\' is not '
                                 f'represented by any members of '
                                 f'\'{healthy_column}\' column in metadata. '
                                 f'Consider using a different healthy_column '
                                 f'or state value.')
    if sorted(healthy_states) == sorted(non_healthy_states):
        raise ValueError('healthy_states and non_healthy_states '
                         'parameters cannot be equal.')
    if not healthy_states == 'rest' and not non_healthy_states == 'rest':
        number_of_state_values = sum([(metadata[healthy_column] == i).sum()
                                      for i in healthy_states +
                                      non_healthy_states])
        if number_of_state_values != len(metadata):
            raise ValueError('Number of healthy and non-healthy state '
                             'values is not equal to the number of '
                             'rows in metadata.')
    return healthy_states, non_healthy_states
'''
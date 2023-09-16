# -----------------------------------------------------------------------------
# Copyright (c) 2023, Bioinformatics at Małopolska Centre of Biotechnology
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

from ._dysbiosis_predictor import calculate_index, calculate_index_viz
from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

__all__ = ['calculate_index','calculate_index_viz']

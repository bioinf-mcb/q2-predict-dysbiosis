# -----------------------------------------------------------------------------
# Copyright (c) 2023, Bioinformatics at Małopolska Centre of Biotechnology
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name="q2-predict-dysbiosis",
    packages=find_packages(),
    author="Kinga Zielińska",
    author_email="kinga.zielinska@uj.edu.pl",
    description="Determine dysbiosis in human gut microbiome samples",
    license='BSD-3-Clause',
    url="https://qiime2.org",
    entry_points={
        'qiime2.plugins':
        ['q2-predict-dysbiosis=q2_predict_dysbiosis.plugin_setup:plugin']
    },
    package_data={
        'q2-predict-dysbiosis.tests': ['data/*'],
        'q2-predict-dysbiosis': ['data/*', 'assets/index.html', 'citations.bib']},
    zip_safe=False,
)

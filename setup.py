#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="SRGSSR PDP Team",
    author_email='pdp@srgssr.ch',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python client library to conveniently query the publication data of SRG/SSR",
    # entry_points={
    #     'console_scripts': [
    #         'srgssr_publication_data_api=srgssr_publication_data_api.cli:main',
    #     ],
    # },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history, # TODO rewrite this one
    include_package_data=True,
    keywords='srgssr metadata pdp publication data',
    name='srgssr-publication-data-api',
    packages=find_packages(include=['srgssr_publication_data_api']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/SRGSSR/pdp_graphql_client_python',
    version='0.3.0',
    zip_safe=False,
)

python_requires='>=3.6'

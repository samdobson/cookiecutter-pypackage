#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [{%- if command_line_interface|lower == 'click' %}'Click>=7.0',{%- endif %} ]

setup_requirements = [{%- if use_pytest == 'y' %}'pytest-runner',{%- endif %} ]

test_requirements = [{%- if use_pytest == 'y' %}'pytest>=3',{%- endif %} ]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    author="{{ full_name.replace('\"', '\\\"') }}",
    author_email='{{ email }}',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if open_source_license in license_classifiers %}
        '{{ license_classifiers[open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="{{ project_short_description }}",
    {%- if 'no' not in command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ project_slug }}={{ project_slug }}.cli:main',
        ],
    },
    {%- endif %}
    install_requires=requirements,
{%- if open_source_license in license_classifiers %}
    license="{{ open_source_license }}",
{%- endif %}
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='{{ project_slug }}',
    name='{{ project_slug }}',
    packages=find_packages(include=['{{ project_slug }}', '{{ project_slug }}.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ github_username }}/{{ project_slug }}',
    version='{{ version }}',
    zip_safe=False,
)

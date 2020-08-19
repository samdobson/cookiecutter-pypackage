#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ command_line_interface|lower }}':
        cli_file = os.path.join('{{ project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ open_source_license }}':
        remove_file('LICENSE')

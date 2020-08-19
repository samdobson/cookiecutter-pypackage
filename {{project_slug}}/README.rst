{% set is_open_source = open_source_license != 'Not open source' -%}
{% for _ in project_name %}={% endfor %}
{{ project_name }}
{% for _ in project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ project_slug }}

.. image:: https://img.shields.io/travis/{{ github_username }}/{{ project_slug }}.svg
        :target: https://travis-ci.com/{{ github_username }}/{{ project_slug }}

.. image:: https://readthedocs.org/projects/{{ project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

{% if add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/github/{{ github_username }}/{{ project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ github_username }}/{{ project_slug }}/
     :alt: Updates
{% endif %}


{{ project_short_description }}

{% if is_open_source %}
* Free software: {{ open_source_license }}
* Documentation: https://{{ project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

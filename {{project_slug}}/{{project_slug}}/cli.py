"""Console script for {{ project_slug}}."""

{%- if command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if command_line_interface|lower == 'click' %}
import click
{%- endif %}

{% if command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
    """Console script for {{ project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{ project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
{%- endif %}
{%- if command_line_interface|lower == 'argparse' %}
def main():
    """Console script for {{ project_slug}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{ project_slug}}.cli.main")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

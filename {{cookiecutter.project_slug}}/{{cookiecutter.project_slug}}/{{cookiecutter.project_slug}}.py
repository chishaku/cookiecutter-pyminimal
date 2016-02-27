# -*- coding: utf-8 -*-
{% if cookiecutter.add_cli_entry_point  == 'y' %}
import click

@click.group()
def cli():
    """{{ cookiecutter.project_name }} command line interface."""

@cli.command()
@click.option('--flag', is_flag=True)
@click.argument('argument')
def command(flag, argument):
	"""A sample command."""

{% endif %}

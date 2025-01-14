#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import click
from waclient.waclient_app import WitnessAngelClientApp

os.environ["KIVY_NO_ARGS"] = "1"


@click.command()
@click.option(
    "-l",
    "--language",
    help="Default language of the App",
    default="en",
    type=click.Choice(["en", "es", "de", "fr"]),
)
def main(language):
    """Run WitnessAngelClientApp with the given language setting.
    """
    WitnessAngelClientApp(language).run()

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'movie-service'
copyright = '2023, Shamsul Arefin'
author = 'Shamsul Arefin'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import os
import sys

# Assuming your Django microservice is in the parent directory
sys.path.insert(0, os.path.abspath('../..'))

# Set the Django project settings module for the microservice
os.environ['DJANGO_SETTINGS_MODULE'] = 'movie-service.main.settings'  # Adjust for each microservice


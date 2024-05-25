# How to configure and Run API DOC Sphinx

- Dont need a docker container. Its a generated HTML file from sphinx.
- install sphinx, myst-parser.
- In the parent folder, run sphinx-quickstart, all enter for options.
- In each subfolders, run sphinx-quickstart, all enter for options. Configure path in the config file, that is needed for apidoc maybe.
- For readme support myst-parser installation, and adding it in the config file is needed. Only adding in the root is fine.

# To run in Linux
- first install sphinx for linux: ``apt-get install python3-sphinx``
- install myst parser, ``pip install myst-parser``
- in the documentation folder where you find config.py file and Makefile, run this command make html
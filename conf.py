# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from subprocess import Popen, PIPE

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Matplotlib Governance Documents"
copyright = "2022, Matplotlib Development Team"
author = "Matplotlib Steering Council"
pipe = Popen("git describe --tags --always", stdout=PIPE, shell=True)
git = pipe.stdout.read().decode("utf-8").rstrip()
release = git.lstrip("R")
version = "-".join(release.split("-")[0:2])
print(version)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "README.md",
    "LICENSE.md",
    "projectlicense.md",
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "mpl_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# Fix for table wrapping
# https://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html

html_css_files = []


html_sidebars = {
    "index": [],
    "**": ["globaltoc.html"],
}

is_release_build = tags.has("release")  # noqa


html_theme_options = {
    "navbar_links": ("absolute", "server-stable"),
    "collapse_navigation": not is_release_build,
    "show_prev_next": False,
    # Toc options
    "navigation_depth": 2,
}

include_analytics = is_release_build
if include_analytics:
    html_theme_options["google_analytics_id"] = "UA-55954603-1"

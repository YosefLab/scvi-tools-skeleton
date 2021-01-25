#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# scvi documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path[:0] = [str(HERE.parent), str(HERE / "extensions")]

import scskeleton  # noqa


# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "3.0"  # Nicer param docs

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "nbsphinx_link",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",  # needs to be after napoleon
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosummary",
    "scanpydoc.elegant_typehints",
    "scanpydoc.definition_list_typed_field",
    "scanpydoc.autosummary_generate_imported",
    *[p.stem for p in (HERE / "extensions").glob("*.py")],
]

# nbsphinx specific settings
exclude_patterns = ["_build", "**.ipynb_checkpoints"]
nbsphinx_execute = "never"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# Generate the API documentation when building
autosummary_generate = True
autodoc_member_order = "bysource"
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_use_rtype = True  # having a separate entry generally helps readability
napoleon_use_param = True
napoleon_custom_sections = [("Params", "Parameters")]
todo_include_todos = False
numpydoc_show_class_members = False
annotate_defaults = True  # scanpydoc option, look into why we need this
nbsphinx_prolog = r"""
.. raw:: html

    <style>
        .nbinput .prompt,
        .nboutput .prompt {
            display: none;
        }
        p {
            padding-top: 5px;
        }
        .nboutput .stderr{
            display: none;
        }
    </style>

{% set docname = env.doc2path(env.docname, base=None).split("/")[-1] %}

.. raw:: html

    <div class="admonition note">
    <p class="admonition-title">Note</p>
    <p>
      This page was generated from
      <a class="reference external" href="https://github.com/yoseflab/scvi-tutorials/">{{ docname|e }}</a>.
      Interactive online version:
      <span style="white-space: nowrap;"><a href="https://colab.research.google.com/github/yoseflab/scvi_tutorials/blob/master/{{ docname|e }}"><img alt="Colab badge" src="https://colab.research.google.com/assets/colab-badge.svg" style="vertical-align:text-bottom"></a>.</span>
    </p>
    </div>
"""
# The master toctree document.
master_doc = "index"


intersphinx_mapping = dict(
    anndata=("https://anndata.readthedocs.io/en/stable/", None),
    ipython=("https://ipython.readthedocs.io/en/stable/", None),
    matplotlib=("https://matplotlib.org/", None),
    numpy=("https://docs.scipy.org/doc/numpy/", None),
    pandas=("https://pandas.pydata.org/pandas-docs/stable/", None),
    python=("https://docs.python.org/3", None),
    scipy=("https://docs.scipy.org/doc/scipy/reference/", None),
    sklearn=("https://scikit-learn.org/stable/", None),
    torch=("https://pytorch.org/docs/master/", None),
    scanpy=("https://scanpy.readthedocs.io/en/stable/", None),
    pytorch_lightning=("https://pytorch-lightning.readthedocs.io/en/stable/", None),
)


# General information about the project.
project = u"scskeleton"
copyright = u"2021, Yosef Lab, UC Berkeley"
author = u"Adam Gayoso"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = scskeleton.__version__
# The full version, including alpha/beta/rc tags.
release = scskeleton.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
pygments_dark_style = "monokai"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}


html_theme_options = {
    "github_url": "https://github.com/YosefLab/scvi-tools",
    "twitter_url": "https://twitter.com/YosefLab",
    # "use_edit_page_button": True,
}
html_context = dict(
    # display_github=True,  # Integrate GitHub
    github_user="YosefLab",  # Username
    github_repo="scvi-tools",  # Repo name
    github_version="master",  # Version
    doc_path="docs/",  # Path in the checkout to the docs root
)
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = ["css/user_guide.css", "css/custom.css"]

html_show_sphinx = False


# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "scvidoc"

mathjax_config = {
    "extensions": ["tex2jax.js"],
    "jax": ["input/TeX", "output/HTML-CSS"],
    "tex2jax": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "displayMath": [["$$", "$$"], ["\\[", "\\]"]],
        "processEscapes": True,
    },
}

# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, "scvi.tex", u"scskeleton Documentation", u"Adam Gayoso", "manual")
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "scskeleton", u"scskeleton Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "scskeleton",
        u"scskeleton Documentation",
        author,
        "scvi",
        "One line description of project.",
        "Miscellaneous",
    )
]

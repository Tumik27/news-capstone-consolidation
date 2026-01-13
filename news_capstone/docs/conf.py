# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

import django
from decouple import config as env_config

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------

# Add the project root (news_capstone/) to sys.path so autodoc can find modules.
sys.path.insert(0, os.path.abspath(".."))

# ---------------------------------------------------------------------------
# Django setup (safe defaults so docs build without needing env vars)
# ---------------------------------------------------------------------------

# Force SQLite for documentation builds unless explicitly overridden
os.environ.setdefault("DB_ENGINE", "sqlite")

# Set required Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# If your settings still read DB_* vars somewhere, provide safe fallbacks:
os.environ.setdefault("DB_NAME", str(env_config("DB_NAME", default="")))
os.environ.setdefault("DB_USER", str(env_config("DB_USER", default="")))
os.environ.setdefault("DB_PASSWORD", str(env_config("DB_PASSWORD", default="")))
os.environ.setdefault("DB_HOST", str(env_config("DB_HOST", default="")))
os.environ.setdefault("DB_PORT", str(env_config("DB_PORT", default="")))

django.setup()

# ---------------------------------------------------------------------------
# Project information
# ---------------------------------------------------------------------------

project = "News Capstone"
copyright = "2026, Tumelo Kgatshe"
author = "Tumelo Kgatshe"
release = "1.0"

# ---------------------------------------------------------------------------
# General configuration
# ---------------------------------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",   # adds links to highlighted source code
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Autodoc defaults: makes documentation consistent and readable
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

napoleon_google_docstring = True
napoleon_numpy_docstring = False

# ---------------------------------------------------------------------------
# HTML output
# ---------------------------------------------------------------------------

html_theme = "alabaster"
html_static_path = ["_static"]

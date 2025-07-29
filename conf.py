# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information




# for web:
author = 'Swaroop Chitlur <a href="https://www.swaroopch.com/">www.swaroopch.com</a>, translator: Daria JENS <a href="https://github.com/Daria-Jens">github.com/Daria-Jens</a>'
project = 'A Byte of Python (ukraine)'
# for pdf:
#author = 'author: Swaroop Chitlur Translator: Daria JENS'
#project = '"Байт Пайтона" (українська версія)'

release = '2025'
copyright = 'creative commons share-alike 4.0 license (cc-by-sa 4.0)'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser",
              "sphinx_design",
              'sphinx_togglebutton']

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "attrs_block",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    #"linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

myst_html_meta = {
    "description lang=en": "Ukrainian translation of the 'A byte of Python' tutorial from Swaroop CH. A tutorial for learning the Python programming language.",
    "description lang=uk": "Український переклад посібника «A byte of Python» від Swaroop CH. Посібник з вивчення мови програмування Python.",
    "keywords": "Python, Tutorial, Ukraine, ukrainian, learning, cc-by-sa, creative commons, free licensed, book, self-learn, study, teach, learn to program, code, Sphinx, MyST",
    "original author": "Swaroop CH",
    "author": "Daria JENS",
    "translator": "Daria JENS",
    "license": "creative commons attribution share-alike cc-by-sa 4.0",
    "og:locale": "uk",
    "og:type": "website",
    "og:url": "https://spielend-programmieren.at/byte_of_python_ukraine/",
    "og:image": "https://spielend-programmieren.at/byte_of_python_ukraine/_images/daria.jpeg",
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'uk'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster' # gut
#html_theme = "classic"   # toc / seiten verschwinden
#html_theme = "sphinxdoc"  # fehler, aber besser, sidebar ist rechts
#html_theme = "scrolls"     # good, no sidebar,
#html_theme = "agogo"      # super, aber die note boxen shaun blöd aus
#html_theme = "traditional" # boring
#html_theme = "nature"       # toc expands to the left
#html_theme = "haiku"        # full screen width, no toc
#html_theme = "pyramid"       # boring, toc left expanded
#html_theme = "bizstyle"
html_theme = "sphinx_book_theme"   # from myst


html_static_path = ['_static']

# -- HTML output -------------------------------------------------


#html_logo = "_static/logo-wide.svg"
#html_favicon = "_static/logo-square.svg"
#html_title = ""
html_theme_options = {
    "rightsidebar": "false",
    #  "relbarbgcolor": "black"
    "home_page_in_toc": True,
    # "github_url": "https://github.com/executablebooks/MyST-Parser",
    "repository_url": "https://github.com/Daria-Jens/byte-of-python/",
    "repository_branch": "master",
    #"path_to_docs": "docs",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    # "announcement": "<b>v3.0.0</b> is now out! See the Changelog for details",
}
html_last_updated_fmt = ""


# --- latexpdf ----


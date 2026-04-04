project = 'PSSTools'
copyright = '2024, PSSTools Contributors'
author = 'PSSTools Contributors'

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'navigation_depth': 3,
    'titles_only': False,
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

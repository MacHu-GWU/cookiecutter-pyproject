# -*- coding: utf-8 -*-

from pathlib_mate import Path

dir_here = Path.dir_here(__file__)
PACKAGE_NAME = dir_here.basename

dir_project_root = Path.dir_here(__file__).parent

# ------------------------------------------------------------------------------
# Virtual Environment Related
# ------------------------------------------------------------------------------
dir_venv = dir_project_root / ".venv"
dir_venv_bin = dir_venv / "bin"

# virtualenv executable paths
bin_pytest = dir_venv_bin / "pytest"

# test related
dir_htmlcov = dir_project_root / "htmlcov"
path_cov_index_html = dir_htmlcov / "index.html"
dir_unit_test = dir_project_root / "tests"

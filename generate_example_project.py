# -*- coding: utf-8 -*-

"""
I would like to include an example project that is generated from this template.
This script can automatically generate the example project.
"""

import shutil
from pathlib import Path
from cookiecutter.main import cookiecutter


dir_here: Path = Path(__file__).absolute().parent
dir_output = dir_here.joinpath("my_package-project")

shutil.rmtree(dir_output, ignore_errors=True)
cookiecutter(
    template=f"{dir_here}",
    output_dir=f"{dir_here}",
    extra_context={
        "package_name": "my_package",
        "package_name_slugify": "my-package",
        "github_username": "my-github-username",
        "author_name": "Firstname Lastname",
        "author_email": "firstname.lastname@email.com",
        "maintainer_name": "Firstname Lastname",
        "maintainer_email": "firstname.lastname@email.com",
        "semantic_version": "0.1.1",
        "py_ver_major": "3",
        "py_ver_minor": "8",
        "py_ver_micro": "11",
        "readthedocs_username": "MyReadthedocsUsername",
        "codecov_token_name": "MyCodecovTokenName",
        "github_token_name": "MyGithubTokenName",
        "readthedocs_token_name": "MyReadthedocsTokenName"
    },
    no_input=True,
)

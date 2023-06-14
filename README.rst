.. image:: https://readthedocs.org/projects/cookiecutter-pyproject/badge/?version=latest
    :target: https://cookiecutter-pyproject.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/cookiecutter-pyproject/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/cookiecutter-pyproject


``cookiecutter-pyproject``
==============================================================================
`FULL DOCUMENT IS HERE <https://cookiecutter-pyproject.readthedocs.io/en/latest/>`_


Summary
------------------------------------------------------------------------------
This is an Python open source library project template I used for years. You can easily generate a folder structure with everything you need and start development, then publish to `PyPI <https://pypi.org/>`_.

Best practices and automation features included in this template:

- Virtualenv management
- Dependencies management
- Local unit test and code coverage test
- Build and preview documentation site locally
- Use `GitHub Action <https://github.com/features/actions>`_ for CI
- Use `Codecov <https://about.codecov.io/>`_ for code coverage report
- Use `Read the Docs <https://readthedocs.org/>`_ for documentation site hosting


Disclaimer
------------------------------------------------------------------------------
All the best practice used in this repo is based on my career experience, and my personal opinion. I have done `over 90+ open source Python library projects <https://pypi.org/manage/projects/>`_ and 50+ internal Python libraries for Enterprise. It is the best practice I am using for years. It allow me to publish a new Python library to PyPI in one hour when I got an idea. Again, it is my personal best practice, **please use it at your own risk**.


Usage
------------------------------------------------------------------------------
Enter the following command, it will use the latest template.

.. code-block:: bash

    pip install cookiecutter
    cookiecutter https://github.com/MacHu-GWU/cookiecutter-pyproject

Or, you can use a specific released version, you can find `full list of release at here <https://github.com/MacHu-GWU/cookiecutter-pyproject/releases>`_.

.. code-block:: bash

    # use specific version
    cookiecutter https://github.com/MacHu-GWU/cookiecutter-pyproject --checkout tags/${version}
    # for example (v1 is the latest as of 2023-06-13)
    cookiecutter https://github.com/MacHu-GWU/cookiecutter-pyproject --checkout tags/v1

Then fill in some information::

    package_name [your_package_name_with_underscore]: ...
    package_name_slug [your-package-name-with-hyphen]: ...
    github_username [your-github-username]: ...
    author_name [Firstname Lastname]: ...
    author_email [firstname.lastname@email.com]: ...
    ...

Then it will generate a Git repo folder structures like this:

- ``/.github/``: GitHub action configuration
- ``/${package_name}/...`` your python project source code
- ``/tests/...``: unit test
- ``/.coveragerc``: code coverage test config
- ``/pyproject_ops.json``: the `pyproject_ops <https://github.com/MacHu-GWU/pyproject_ops-project>`_ CLI automation tool config file

We have an example project generated from this template `my_package-project <./my_package-project>`_. Please take a look at it.

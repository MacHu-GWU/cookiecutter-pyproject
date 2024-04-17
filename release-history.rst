.. _release_history:

Release and Version History
==============================================================================


Backlog (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


V4 (2023-04-17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Minor Improvements**

- Upgrade ``docfly`` to ``2.0.3``.
- Upgrade main Python version to 3.10.
- Ignore ``${package_name}/tests/`` folder when packaging distribution.
- Add ``python_requires`` in ``setup.py``.
- Bump CI and setup requirements to ``>=3.8``.


V3 (2023-09-25)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Allow to use jupyter notebook as the documentation source.
- Enable sphinx search in furo theme.
- Adapt the Readthedocs new convention using the ``.readthedocs.yml`` file.


V2 (2023-06-14)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- fix a bug that we should use standard library ``pathlib``, not ``pathlib_mate`` in ``${package_name}/paths.py``


v1 (2023-06-13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First Release
- Virtualenv management
- Dependencies management
- Local unit test and code coverage test
- Build and preview documentation site locally
- Use `GitHub Action <https://github.com/features/actions>`_ for CI
- Use `Codecov <https://about.codecov.io/>`_ for code coverage report
- Use `Read the Docs <https://readthedocs.org/>`_ for documentation site hosting

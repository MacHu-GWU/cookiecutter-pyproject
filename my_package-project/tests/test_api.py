# -*- coding: utf-8 -*-

from my_package import api


def test():
    _ = api


if __name__ == "__main__":
    from my_package.tests import run_cov_test

    run_cov_test(__file__, "my_package.api", preview=False)

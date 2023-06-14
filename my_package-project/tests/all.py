# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from my_package.tests import run_cov_test

    run_cov_test(__file__, "my_package", is_folder=True, preview=False)

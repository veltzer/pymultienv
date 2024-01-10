from typing import List


console_scripts: List[str] = [
    "pymultienv=pymultienv.me:cli",
]
dev_requires: List[str] = [
    "pypitools",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "gitpython",
    "pyfakeuse",
]
make_requires: List[str] = [
    "pymakehelper",
    "pyclassifiers",
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires

""" python deps for this project """

console_scripts: list[str] = [
    "pymultienv=pymultienv.me:cli",
]

config_requires: list[str] = [
    "pyclassifiers",
]
install_requires: list[str] = [
    "gitpython",
    "pyfakeuse",
]
build_requires: list[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires

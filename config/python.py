import config.project

package_name = config.project.project_name

console_scripts = [
    "pymultienv=pymultienv.me:cli",
]

install_requires = [
    "gitpython",
    "pyfakeuse",
]

test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
]

dev_requires = [
    "pyclassifiers",
    "pypitools",
    "pydmt",
    "Sphinx",
    "pymakehelper",
]

python_requires = ">=3.9"
test_os = ["ubuntu-20.04"]
test_python = ["3.9"]

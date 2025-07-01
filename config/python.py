""" python deps for this project """

import config.shared

install_requires: list[str] = [
    "gitpython",
    "pyfakeuse",
]
build_requires: list[str] = config.shared.PBUILD
test_requires: list[str] = config.shared.PTEST
requires = install_requires + build_requires + test_requires

scripts: dict[str,str] = {
    "pymultienv": "pymultienv.me:cli",
}

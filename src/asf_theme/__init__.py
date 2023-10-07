"""An extension of the MkDocs Material Theme for ASF"""

from importlib.metadata import PackageNotFoundError, version

_pip_name = 'mkdocs-asf-theme'
try:
    __version__ = version(_pip_name)
except PackageNotFoundError:
    print(f'{_pip_name} package is not installed!\n'
          f'Install in editable/develop mode via (from the top of this repo):\n'
          f'   python -m pip install -e .\n'
          f'Or, to just get the version number use:\n'
          f'   python setup.py --version')

__all__ = [
    '__version__',
]

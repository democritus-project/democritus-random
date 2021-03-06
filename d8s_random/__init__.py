try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import PackageNotFoundError, version  #type: ignore

try:
    __version__ = version('d8s_random')
except PackageNotFoundError:
    message = 'Unable to find a version number for "d8s_random". This likely means the library was not installed properly. Please re-install it and, if the problem persists, raise an issue here: https://github.com/democritus-project/democritus-random/issues.'
    print(message)

__author__ = '''Floyd Hightower'''
__email__ = 'floyd.hightower27@gmail.com'

from .random_wrapper import *

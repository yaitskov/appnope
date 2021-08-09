__version__ = '0.1.2'

import sys
import platform
from distutils.version import LooseVersion as V

from ._dummy import *

del sys, platform, V

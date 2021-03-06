#!/usr/bin/env python
"""
Check for required dependencies for the 2016 AAS "Using Python for
Astronomical Data Analysis" workshop.

Usage::

  % python check_env.py
"""

from distutils.version import LooseVersion


def check_package(package_name, minimum_version=None):
    errors = False
    try:
        pkg = __import__(package_name)
    except ImportError as err:
        print('Error: Failed import: {0}'.format(err))
        errors = True
    else:
        if minimum_version is not None:
            if package_name == 'xlwt':
                installed_version = pkg.__VERSION__
            else:
                installed_version = pkg.__version__
            if (LooseVersion(installed_version) <
                    LooseVersion(str(minimum_version))):
                print('Error: {0} version {1} or later is required, you '
                      'have version {2}'.format(package_name, minimum_version,
                                                installed_version))
                errors = True
    return errors


pkgs = {'IPython': '4.0',
        'jupyter': '1.0',
        'numpy': '1.6',
        'scipy': '0.15',
        'matplotlib': '1.3',
        'astropy': '1.1',
        'photutils': '0.2',
        'skimage': '0.11',
        'pandas': '0.17.1',
        'xlwt': '1.0.0',
        'astroquery': '0.2.6',
        'glue': None,
        }

errors = []
for package_name, min_version in pkgs.items():
    errors.append(check_package(package_name, minimum_version=min_version))
if any(errors):
    print('\nThere are errors that you must resolve before running the '
          'tutorials.')
else:
    print('\nYour Python environment is good to go!')

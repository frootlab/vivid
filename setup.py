#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Frootlab
# Copyright (C) 2013-2019 Patrick Michl
#
# This file is part of Vivid Code, https://www.frootlab.org/vivid
#
#  Vivid Code is free software: you can redistribute it and/or modify it under
#  the terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Vivid Code is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
#  A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License along with
#  Vivid Code. If not, see <http://www.gnu.org/licenses/>.
#
"""Setuptools based installation."""

__version__ = '19.09-3'
__license__ = 'GPLv3'
__copyright__ = '2019 Frootlab'
__description__ = 'Enterprise Machine-Learning and Predictive Analytics'
__url__ = 'https://www.frootlab.org/vivid'
__organization__ = 'Frootlab'
__author__ = 'Frootlab Developers'
__email__ = 'contact@frootlab.org'
__authors__ = ['Patrick Michl <patrick.michl@frootlab.org>']
__maintainer__ = 'Patrick Michl'
__credits__ = ['Willi Jäger']
__docformat__ = 'google'

import pathlib
import setuptools

def install() -> None:
    """Setuptools based installation script."""

    # Install package
    setuptools.setup(
        name='vivid',
        version=__version__,
        description=__description__,
        long_description=pathlib.Path('.', 'README.md').read_text(),
        long_description_content_type='text/markdown',
        classifiers=[
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 3',
    		'Programming Language :: Python :: 3.7',
            'Operating System :: OS Independent',
            'Topic :: Software Development :: Libraries :: Python Modules'],
        keywords=(
            'collaborative-research '
            'data-science '
            'machine-learning '
            'framework '
            'artificial-intelligence '
            'artificial-neural-networks '
            'platform '
            'python '
            'python-library '
            'collaborative-data-science '
            'automated-machine-learning '),
        url=__url__,
        author=__author__,
        author_email=__email__,
        license=__license__,
        packages=setuptools.find_packages(exclude=['docs', 'tests']),
        python_requires='>=3.7',
        install_requires=[
            'vivid-db>=0.1.11',
            'vivid-node>=0.5.582',
            'vivid-store>=0.0.1']
    )

if __name__ == '__main__':
    install()

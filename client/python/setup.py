#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    pyhfcus Python HFCuS Client.
#    Copyright (c) 2017 Be The Match operated by National Marrow Donor Program. All Rights Reserved.
#
#    This library is free software; you can redistribute it and/or modify it
#    under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation; either version 3 of the License, or (at
#    your option) any later version.
#
#    This library is distributed in the hope that it will be useful, but WITHOUT
#    ANY WARRANTY; with out even the implied warranty of MERCHANTABILITY or
#    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
#    License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this library;  if not, write to the Free Software Foundation,
#    Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA.
#
#    > http://www.fsf.org/licensing/licenses/lgpl.html
#    > http://www.opensource.org/licenses/lgpl-license.php
#



from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    "urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyhfcus',
    version='0.0.1',
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    long_description=readme,
    author="Mike Halagan",
    author_email='mhalagan@nmdp.org',
    url='https://github.com/nmdp-bioinformatics/service-haplotype-frequency-curation',
    packages=[
        'pyhfcus',
        'pyhfcus.models',
        'pyhfcus.api'
    ],
    package_dir={'pyhfcus':
                 'pyhfcus'},
    include_package_data=True,
    install_requires=requirements,
    license="LGPL 3.0",
    zip_safe=False,
    keywords='pyhfcus',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    scripts=['bin/hfcus-import', 'bin/hfcus-extract'],
    test_suite='tests',
    tests_require=test_requirements
)

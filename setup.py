#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os
import sys
import shutil

setup = os.path.abspath(sys.argv[0])
parent = os.path.dirname(setup)
pkg = os.path.basename(parent)

if pkg.startswith("py-mapzen"):
    pkg = pkg.replace("py-", "")
    pkg = pkg.replace("-", ".")

    egg_info = "%s.egg-info" % pkg
    egg_info = os.path.join(parent, egg_info)

    if os.path.exists(egg_info):
        shutil.rmtree(egg_info)

# Okay carry on as usual... well, except for all the requires stuff
# below (20160128/thisisaaronland)

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read()
version = open("VERSION").read()

setup(
    name='mapzen.whosonfirst',
    namespace_packages=[],
    version=version,
    description='A package to install all the other Who\'s On First Python packages',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst',
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst/releases/tag/' + version,
    license='BSD',
    install_requires=[
        'boto',
        'geojson',
        'geojson',
        'atomicwrites',
        'shapely',
        'requests',
        'deepdiff',
        'tenacity', # TBD - does the default system/ubuntu installation of six play nice with this (20170720/thisisaaronland)
        'machinetag',
        'mapzen-whosonfirst-machinetag',
        'mapzen-whosonfirst-elasticsearch',
        'mapzen-whosonfirst-bundles',
        'mapzen-whosonfirst-diff',
        'mapzen-whosonfirst-export',
        'mapzen-whosonfirst-geojson',
        'mapzen-whosonfirst-git',
        'mapzen-whosonfirst-languages',
        'mapzen-whosonfirst-mapshaper',
        'mapzen-whosonfirst-meta',
        'mapzen-whosonfirst-names',
        'mapzen-whosonfirst-pip',
        'mapzen-whosonfirst-placetypes',
        'mapzen-whosonfirst-search',
        'mapzen-whosonfirst-sources',
        'mapzen-whosonfirst-uri',
        'mapzen-whosonfirst-utils',
        'mapzen-whosonfirst-validator',
        'mapzen-whosonfirst-properties',
        'mapzen-whosonfirst-hierarchy',
        'mapzen-whosonfirst-spatial'],
    dependency_links=[
        'https://github.com/whosonfirst/py-machinetag/tarball/master#egg=machinetag-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-machinetag/tarball/master#egg=mapzen-whosonfirst-machinetag-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-elasticsearch/tarball/master#egg=mapzen-whosonfirst-elasticsearch-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-bundles/tarball/master#egg=mapzen-whosonfirst-bundles-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-diff/tarball/master#egg=mapzen-whosonfirst-diff-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-export/tarball/master#egg=mapzen-whosonfirst-export-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-geojson/tarball/master#egg=mapzen-whosonfirst-geojson-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-git/tarball/master#egg=mapzen-whosonfirst-git-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-languages/tarball/master#egg=mapzen-whosonfirst-languages-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-mapshaper/tarball/master#egg=mapzen-whosonfirst-mapshaper-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-meta/tarball/master#egg=mapzen-whosonfirst-meta-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-names/tarball/master#egg=mapzen-whosonfirst-names-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-pip/tarball/master#egg=mapzen-whosonfirst-pip-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-placetypes/tarball/master#egg=mapzen-whosonfirst-placetypes-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-search/tarball/master#egg=mapzen-whosonfirst-search-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-sources/tarball/master#egg=mapzen-whosonfirst-sources-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-uri/tarball/master#egg=mapzen-whosonfirst-uri-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-utils/tarball/master#egg=mapzen-whosonfirst-utils-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-validator/tarball/master#egg=mapzen-whosonfirst-validator-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-properties/tarball/master#egg=mapzen-whosonfirst-properties-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-hierarchy/tarball/master#egg=mapzen-whosonfirst-hierarchy-0',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-spatial/tarball/master#egg=mapzen-whosonfirst-spatial-0'])

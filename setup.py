# coding: utf-8

"""
    Fabric Credential Manager API

    This is Fabric Credential Manager API  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: kthare10@unc.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "fabric-credmgr-client"
VERSION = "0.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="Fabric Credential Manager API",
    author_email="kthare10@unc.edu",
    url="",
    keywords=["Swagger", "Fabric Credential Manager API"],
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
)

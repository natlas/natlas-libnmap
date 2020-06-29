# -*- coding: utf-8 -*-
import setuptools
from distutils.core import setup
import libnmap

with open("README.md") as rfile:
    long_description = rfile.read()

setup(
    name="natlas-libnmap",
    version=libnmap.__version__,
    author="0xdade",
    author_email="dade@actualcrimes.org",
    packages=["libnmap", "libnmap.objects"],
    url="http://pypi.python.org/pypi/natlas-libnmap/",
    license='Creative Common "Attribution" license (CC-BY) v3',
    description=(
        "Python NMAP library enabling you to start async nmap tasks, "
        "parse and compare/diff scan results"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: System :: Networking",
    ],
    install_requires=["defusedxml"],
)

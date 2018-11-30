#!/usr/bin/env python

import os
import platform
import subprocess
import tarfile
import shutil

try:
    import sysconfig
except ImportError:
    # Python 2.6
    from distutils import sysconfig

from setuptools import setup
from distutils.extension import Extension
from distutils.command.build_ext import build_ext


def path_in_dir(relative_path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class jq_build_ext(build_ext):
    def run(self):
        build_ext.run(self)

jq_lib_dir = path_in_dir("jq-jq-1.5")
oniguruma_lib_install_dir = path_in_dir("onig-install-5.9.6")
    

jq_extension = Extension(
    "jq",
    sources=["jq.c"],
    include_dirs=[jq_lib_dir],
    extra_objects=[
        os.path.join(jq_lib_dir, ".libs/libjq.a"),
        os.path.join(oniguruma_lib_install_dir, "lib/libonig.a"),
    ],
)

setup(
    name='jq',
    version='0.1.6',
    description='jq is a lightweight and flexible JSON processor.',
    long_description=read("README.rst"),
    author='Michael Williamson',
    url='http://github.com/mwilliamson/jq.py',
    license='BSD 2-Clause',
    ext_modules = [jq_extension],
    cmdclass={"build_ext": jq_build_ext},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)


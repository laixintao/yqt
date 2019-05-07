# -*- coding: utf-8 -*-


from distutils.core import setup
from os import path

setup(
    name="yqt",
    version="0.0.3",
    description="Yuque command line tools",
    author="laixintao",
    author_email="laixintaoo@gmail.com",
    url="https://github.com/laixintao/yqt",
    entry_points={"console_scripts": ["yqt = upload:main"]},
    scripts=["upload.py"],
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["yuque", "markdown"],
)

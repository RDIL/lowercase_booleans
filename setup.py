"""Builds the package."""

import setuptools

# Package version:
VERSION = "1.0.0"

# Read the long description:
with open("README.md", mode="r") as FILE_HANDLER:
    LONG_DESCRIPTION = FILE_HANDLER.read()

# Keywords:
TAGS = [
    "lowercase",
    "booleans"
]

# Classifiers:
CLASSIFIERS = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Operating System :: Microsoft",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "Operating System :: Microsoft :: Windows :: Windows 8",
    "Operating System :: Microsoft :: Windows :: Windows 8.1",
    "Operating System :: Microsoft :: Windows :: Windows 7",
    "Operating System :: MacOS",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Other OS",
    "Intended Audience :: Developers",
    "Intended Audience :: End Users/Desktop",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
    "Development Status :: 5 - Production/Stable",
    "Framework :: IDLE",
    "Natural Language :: English"
]

# GitHub URL:
MainURL = "https://github.com/RDIL/lowercase_booleans"

# Other Project URLs:
URLs = {
    "Bug Tracker": "https://github.com/RDIL/lowercase_booleans/issues",
    "Source Code": "https://github.com/RDIL/lowercase_booleans",
}


setuptools.setup(
    name="lcbools",
    version=VERSION,
    author="RDIL",
    author_email="me@rdil.rocks",
    description="Lowercase booleans",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=MainURL,
    packages=setuptools.find_packages(),
    classifiers=CLASSIFIERS,
    project_urls=URLs,
    keywords=TAGS,
    include_package_data=True,
    zip_safe=False
)

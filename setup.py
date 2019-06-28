import setuptools

# Read the long description:
with open("README.md", mode="r") as FILE_HANDLER:
    LONG_DESCRIPTION = FILE_HANDLER.read()

TAGS = [
    "lowercase",
    "booleans"
]

CLASSIFIERS = [
    "Programming Language :: Python",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
    "Development Status :: 7 - Inactive",
    "Framework :: IDLE",
    "Natural Language :: English"
]

# GitHub URL:
MainURL = "https://github.com/RDIL/lowercase_booleans"

# Other Project URLs:
URLs = {
    "Bug Tracker": MainURL + "/issues",
    "Source Code": MainURL,
}


setuptools.setup(
    name="lcbools",
    version="1.0.3",
    author="Reece Dunham",
    author_email="me@rdil.rocks",
    description="lowercase booleans - Deprecated",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=MainURL,
    packages=setuptools.find_packages(),
    classifiers=CLASSIFIERS,
    project_urls=URLs,
    keywords=TAGS
)

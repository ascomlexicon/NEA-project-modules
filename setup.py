# Set-up file for project_package
"""
This is the set-up file for the project package.
"""
from setuptools import setup

setup(
    name='project_package',
    version="0.0.1",
    author="Ascomicon",
    author_email="jethroramos274@gmail.com",
    packages=["nea_module", "nea_module.tests"],
    scripts=[],
    url="",
    license="LICENSE.txt",
    description="A package used for my NEA projects and prototypes.",
    long_description=open("README.txt").read(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "beautifulsoup4",
    ]
)

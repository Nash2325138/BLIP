import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="blip",
    py_modules=["models"],
    version="1.0",
    description="",
    author="salesforce",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True,
    extras_require={'dev': ['pytest']},
    package_data={'configs': ['med_config.json']},
)

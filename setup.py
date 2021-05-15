import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="iamunused",
    version="0.2.9",
    description="Scan and remediate unused permissions within IAM Policies",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/chrisdunne/iamunused",
    author="Chris Dunne",
    author_email="contact@chrisdunne.net",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["iamunused"],
    include_package_data=True,
    install_requires=["boto3"],
    entry_points={
        "console_scripts": [
            "iamunused=iamunused.__main__:main",
        ]
    },
)
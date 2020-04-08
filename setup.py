import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="github-ci-status",
    version="0.0.1",
    author="Xavier Duran",
    author_email="xavier.duran@pm.me",
    description="GitHub Developer REST API v3 helpers for CI",
    long_description=long_description,
    url="https://github.com/xdurana/github-ci-status",
    license="GPL-3.0",
    packages=setuptools.find_packages(),
)

from setuptools import setup, find_packages


setup(
    name="mote-lib-base",
    description="The base set of patterns for Mote",
    long_description = open("README.rst", "r").read() + open("AUTHORS.rst", "r").read() + open("CHANGELOG.rst", "r").read(),
    version="0.1",
    author="Praekelt Consulting",
    author_email="dev@praekelt.com",
    license="BSD",
    url="http://github.com/praekelt/mote-lib-base",
    packages = find_packages(),
    dependency_links = [
    ],
    install_requires = [
    ],
    tests_require = [
        "tox",
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
    include_package_data=True,
)

from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Generate latex'

setup(
    name="texlib",
    version=VERSION,
    author="Astronomax",
    author_email="fgfgfb93@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'latex'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

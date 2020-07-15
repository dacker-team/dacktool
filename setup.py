import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dacktool",
    version="0.0.4",
    author="Dacker",
    author_email="hello@dacker.co",
    description="Some python tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dacker-team/dacktool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    install_requires=[
    ],
)

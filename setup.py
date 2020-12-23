  
"""Setup configuration."""
import setuptools

with open("README.md", "r") as fh:
    LONG = fh.read()
setuptools.setup(
    name="pytracktry",
    version="0.1",
    author="Concentricc",
    author_email="Concentricc@gmail.com",
    description="A python wrapper for the TrackTry API",
    long_description=LONG,
    install_requires=['aiohttp', 'async_timeout'],
    long_description_content_type="text/markdown",
    url="https://github.com/concentricc/pytracktry",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
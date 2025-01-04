from setuptools import setup, find_packages

setup(
    name="mymodule",  # Name of your package
    version="0.1",  # Package version
    packages=find_packages(),  # Finds all packages automatically
    install_requires=[],  # List dependencies if needed
    author="Felix Omondi",
    author_email="felixomosh7@gmail.com",
    description="A simple Python module for greeting and addition",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Felix-svg/my_module",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

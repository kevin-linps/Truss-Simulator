import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requires = ["numpy",
            "matplotlib",
            "tabulate",
            "pytest"]

setuptools.setup(
    name="truss",
    version="0.0.1",
    author="kevin-linps",
    author_email="kevin.linps@hotmail.com",
    description="A 2D truss solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kevin-linps/Truss-Solver",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

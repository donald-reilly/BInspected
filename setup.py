from setuptools import setup, find_packages

setup(
    name="BInspected",
    version="0.1.0",
    author="Donald Reilly",
    author_email="donald.reilly.jr@outlook.com",
    description="Intropection package for python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/donald-reilly/BInspected",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.13.1"
)

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysql-pkg-ushergodwin",
    version="0.0.1",
    author="Tumuhimbise Usher Godwin",
    author_email="godwintumuhimbise96.com",
    description="A lightweight mysql package that works with either pymysql, mysqlclient or mysql connectore",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ushergodwin/pysql",
    project_urls={
        "Bug Tracker": "https://github.com/ushergodwin/pysql/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
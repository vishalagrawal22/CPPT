from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cppt",
    version="1.3.0",
    author="Vishal Agrawal",
    author_email="vishalagrawalva22@gmail.com",
    description="Command line tool to automate your competitive programming workflow without cluttering your workspace with testcase data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vishalagrawal22/CPPT",
    py_modules=["cppt.bin.cppt"],
    include_package_data=True,
    install_requires=[
        "click",
        "pyyaml",
    ],
    packages=[
        "cppt.utils",
        "cppt.commands.create",
        "cppt.commands.fetch",
        "cppt.commands.run",
        "cppt.commands.config",
        "cppt.commands.compile",
        "cppt.commands.tc",
        "cppt.commands.tc.add",
        "cppt.commands.tc.edit",
        "cppt.commands.tc.view",
        "cppt.commands.tc.delete",
        "cppt.commands.test",
        "cppt.commands",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "cppt = cppt.bin.cppt:cli",
        ],
    },
)

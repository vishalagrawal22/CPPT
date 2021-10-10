from setuptools import setup, find_packages

setup(
    name="cppt",
    version='0.1.0',
    py_modules=['src.interface'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'cppt = src.interface:cli',
        ],
    },
)
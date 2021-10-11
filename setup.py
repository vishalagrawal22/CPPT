from setuptools import find_packages, setup

setup(
    name="cppt",
    version='0.5.0',
    py_modules=['cppt.bin.cppt'],
    include_package_data=True,
    install_requires=[
        'click',
        'pyyaml',
    ],
    packages=["cppt.utils", "cppt.commands.create", "cppt.commands.fetch", "cppt.commands.addtc", "cppt.commands.run", "cppt.commands.config", "cppt.commands"],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'cppt = cppt.bin.cppt:cli',
        ],
    },
)

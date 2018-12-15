from setuptools import setup

setup(
    name="quickstats",
    version="0.1",
    packages=["quickstats"],
    install_requires=[
        "psutil",
        "click"
    ],
    entry_points={
        "console_scripts": [
            "quickstats = quickstats.cli:cli"
        ]
    },

)

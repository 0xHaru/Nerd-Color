from pathlib import Path

from setuptools import find_packages, setup

CURRENT_DIR = Path(__file__).parent

with open(f"{CURRENT_DIR}/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Nerd-Color",
    description="A simple CLI colorizer.",
    version="0.1.0",
    license="GPLv3",
    author="0xHaru",
    author_email="0xharu.git@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="color colour colorscheme terminal",
    url="https://github.com/0xHaru/Nerd-Color",
    project_urls={
        "Bug Tracker": "https://github.com/0xHaru/Nerd-Color/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires=">=3.6",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "nerdcolor=nerdcolor.__main__:main",
        ]
    },
)

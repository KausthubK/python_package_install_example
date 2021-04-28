from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

pkgs = find_packages(exclude=['test'])

setup(
    name = 'kk_pkgs',
    version = '2.0.0',
    author = 'Kausthub Krishnamurthy',
    author_email = 'kausthub.krishnamurthy@live.com',
    description = 'Example python installation.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/KausthubK/python_package_install_example',
    packages = pkgs,
    install_requires = [requirements],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: Unix",
        "Environment :: GPU :: NVIDIA CUDA :: 11.2"
    ],
    entry_points={
        "console_scripts": [
            "mod1 = kkpkgs.kkpkg1.mod1:main",
        ]
    },
    scripts=[
        'kkpkgs/kkpkg1/mod1.py'
    ]
)

from colorama import Fore

print(Fore.GREEN + "Installed packages:" + Fore.RESET)
for pkg in pkgs:
    print(Fore.GREEN + pkg + Fore.RESET)
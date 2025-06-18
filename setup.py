from setuptools import setup, find_packages

setup(
    name="mathsqt",
    version="1.0.3",
    packages=find_packages(),
    install_requires=[
        'rich',
        'sympy',
        'numpy',
        'pyfiglet',
    ],
    entry_points={
        'console_scripts': [
            'mathsqt=mathsqt.main:main',
        ],
    },
    author="Thomas",
    description="A comprehensive CLI math toolkit",
    license="MIT",
    keywords="math cli calculator",
)

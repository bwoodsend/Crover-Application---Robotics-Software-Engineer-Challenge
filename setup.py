from setuptools import setup, find_packages
from pathlib import Path

setup(
    author="Brénainn Woodsend",
    author_email='bwoodsend@gmail.com',
    python_requires='>=3.6',
    description="A coding challenge for a Twig application.",
    install_requires=[],
    name='crover_challenge',
    packages=find_packages(include=['crover_challenge', 'crover_challenge.*']),
    url='https://github.com/bwoodsend/crover_challenge',
    version="0.1.0",
)

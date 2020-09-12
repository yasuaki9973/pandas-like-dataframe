
from setuptools import setup, find_packages
import pathlib


setup(

    name='pandola',

    version='0.1.2',

    description='pandas like dataframe library',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(exclude=('tests')),

    python_requires='>=3.7',

)

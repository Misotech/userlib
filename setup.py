# yapf: disable
from setuptools import setup, find_packages

setup(
    name='userlib',
    version='0.3.0',
    description='Rockstat user library',
    url='http://rock.st',

    author='Dmitry Rodin',
    author_email='madiedinro@gmail.com',

    license='Apache-2.0',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries'
    ],
    packages=find_packages(exclude=['examples', 'docs', 'tests*']),

    install_requires=[
        # common
        'ujson',
        'band',
        # crypto
        'base58',
        'pycryptodomex'
    ],
    # setup_requires=['pytest-runner', 'flake8'],
    # tests_require=['pytest', 'testfixtures']
)

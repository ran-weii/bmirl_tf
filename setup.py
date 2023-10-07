from distutils.core import setup
from setuptools import find_packages

setup(
    name='rambo',
    packages=find_packages(),
    version='0.0.1',
    description='A Bayesian approach to robust inverse reinforcement learning',
    long_description=open('./README.md').read(),
    author='Ran Wei',
    author_email='rw422@tamu.edu',
    entry_points={
        'console_scripts': (
            'rambo=rambo.scripts.console_scripts:main'
        )
    },
    requires=(),
    zip_safe=True,
    license='MIT'
)

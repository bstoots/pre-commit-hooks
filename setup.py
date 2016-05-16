from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_hooks',
    description='Additional pre-commit hooks.',
    url='https://github.com/bstoots/pre-commit-hooks',
    version='0.0.1',

    author='Brian Stoots',
    author_email='bstoots@gmail.com',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    # packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=[
        # nothing that I'm aware of
    ],
    entry_points={
        'console_scripts': [
            'always-fail = pre_commit_hooks.always_fail:main'
        ],
    },
)

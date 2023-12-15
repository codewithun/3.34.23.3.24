
### `setup.py`

from setuptools import setup, find_packages

setup(
    name='gold-3.34.23.3.24',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'gold-3.34.23.3.24 = uas_3.34.23.3.24:main',
        ],
    },
    author='Untara Saputra',
    author_email='untara337@gmail.com',
    description='Python package for basic math operations and Golden Ratio calculation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/codewithun/gold3.34.23.3.24',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

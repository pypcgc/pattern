from setuptools import setup, find_packages


NAME = '{{PROJECT}}'
DESCRIPTION = '{{DESCRIPTION}}'
URL = '{{URL}}'
EMAIL = '{{EMAIL}}'
AUTHOR = '{{NAME}}'
REQUIRES_PYTHON = '{{REQUIRES_PYTHON}}'
VERSION = '{{VERSION}}'
LICENSE = '{{PROJECT_LICENSE}}'
CLASSIFIERS = [
        'Programming Language :: Python'
    ]
# CONSOLE_SCRIPTS = ['NAME=NAME:cli']


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    # entry_points={
    #     'console_scripts': CONSOLE_SCRIPTS,
    # }
)

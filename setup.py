from distutils.core import setup

with open('requirements.txt') as f:
    requires = f.read().splitlines()

setup(
    name='ibm-cp4s-client',
    version='0.0.3',
    author='Raymund Lin',
    author_email='raymundl@tw.ibm.com',
    packages=['cp4s', 'cp4s/atk'],
    scripts=[],
    url='https://github.com/ibm/ibm-cp4s-client',
    license="Apache License 2.0",
    description='A python module for interacting with CP4S.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=requires,
)

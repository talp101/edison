from distutils.core import setup
from pip.req import parse_requirements
from setuptools import find_packages

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='edison',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/talp101/edison',
    license='MIT',
    author='Tal Peretz',
    install_requires=reqs,
    author_email='13@1500.co.il',
    description='Authentication middleware for JWT auth in Flask and Django apps'
)

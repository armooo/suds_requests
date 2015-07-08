from setuptools import setup


setup(
    name='suds_requests',
    version='0.2',
    description=open('README.rst').read(),
    author='Jason Michalski',
    author_email='armooo@armooo.net',
    py_modules=['suds_requests'],
    install_requires=['requests', 'suds'],
)

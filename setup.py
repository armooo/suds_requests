from setuptools import setup


setup(
    name='suds_requests',
    version='0.2',
    description='A suds transport implemented with requests',
    long_description=open('README.rst').read(),
    author='Jason Michalski',
    author_email='armooo@armooo.net',
    py_modules=['suds_requests'],
    install_requires=['requests', 'suds'],
    license='MIT',
    url='https://github.com/armooo/suds_requests',
)

from distutils.core import setup

setup(
    name='boa',
    version='0.1.0',
    packages=['boa'],
    scripts=['/scripts/boa.py'],
    url='https://github.com/Morgul/boa',
    license='MIT',
    author='Christopher S. Case',
    author_email='chris.case@g33xnexus.com',
    description='A BDD style test framework, based off Mocha'
)

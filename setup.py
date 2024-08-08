
from setuptools import setup, find_packages

setup(
    name = 'sode', 
    version = '0.1',
    packages = find_packages(), 
    install_requires = [
    'tabulate', 
	'networkx', 
	'matplotlib', 
	'google.generativeai', 
	'numpy', 
	'scipy', 
	'pandas', 
	'astor'
    ], 
)

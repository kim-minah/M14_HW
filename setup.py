from setuptools import setup, find_packages

setup(
    name='loversPackage',
    version='1.0.0',
    url='https://github.com/kim-minah/M14_HW.git',
    author='Minah Kim',
    author_email='mk7kc@virginia.edu',
    description='Contains module booklover for booklovers',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)

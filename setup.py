from setuptools import setup, find_packages

setup(name='bayesnet_em',
    version='0.0.0',
    description='Fill in data of a single hidden node using the EM algorithm',
    url='https://github.com/nnvutisa/EM_BayesNet',
    author='Nalin V',
    author_email='nnvutisa@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'numpy>=1',
        'pomegranade==0.9'],
    zip_safe=False)

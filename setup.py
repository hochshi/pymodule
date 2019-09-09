import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name='pymodule',
    version='0.1',
    description='Python module interface',
    long_description=readme(),
    url='https://github.com/Fleishman-Lab/flab',
    author='Shi Hoch',
    author_email='hochshi@gmail.com',
    packages=setuptools.find_packages(),
)

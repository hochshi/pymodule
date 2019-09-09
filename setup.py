import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name='pymodule',
    version='0.1-alpha',
    license='GPL-3.0',
    description='Python module interface',
    long_description=readme(),
    url='https://github.com/hochshi/pymodule',
    download_url=
    'https://github.com/hochshi/pymodule/archive/v0.1-alpha.tar.gz',
    keywords=['RHEL', 'module'],
    author='Shi Hoch',
    author_email='hochshi@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Operating System',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

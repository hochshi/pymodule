import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name='pymodule',
    version='0.2-alpha',
    license='GPL-3.0',
    description='Python module interface',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/hochshi/pymodule',
    download_url=
    'https://github.com/hochshi/pymodule/archive/v0.2-alpha.tar.gz',
    keywords=['RHEL', 'module'],
    author='Shi Hoch',
    author_email='pymodule@mailinator.com',
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

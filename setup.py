from setuptools import setup

setup(
    name='pybackup',
    version='1.0',
    description='Recursive file backup',
    url='http://github.com/harsh8398/pybackup',
    author='Harsh Patel',
    author_email='pharsh58@gmail.com',
    scripts=['bin/pybackup'],
    packages=['pybackup'],
    data_files=[("", ["LICENSE.txt"])],
    install_requires=[
        'nose',
    ],
    zip_safe=False)

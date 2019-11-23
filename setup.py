from distutils.core import setup

setup(
    name='pybackup',
    version='1.0',
    description='Recursive and Incremental backup utility',
    url='http://github.com/harsh8398/pybackup',
    author='Harsh Patel',
    author_email='pharsh58@gmail.com',
    scripts=['bin/pybackup'],
    packages=['pybackup'],
    data_files=[("", ["LICENSE.txt"])],
    install_requires=[
    ],
    zip_safe=False)

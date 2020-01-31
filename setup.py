from distutils.core import setup

setup(
    name='backup.py',
    version='0.1',
    description='Recursive and Incremental backup utility',
    url='http://github.com/harsh8398/backup.py',
    author='Harsh Patel',
    author_email='pharsh58@gmail.com',
    scripts=['bin/pybackup'],
    packages=['backup'],
    data_files=[("", ["LICENSE.txt"])],
    install_requires=[
        "tqdm"
    ],
    zip_safe=False)

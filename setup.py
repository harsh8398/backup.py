import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='backup.py',
    version='0.1.1',
    author='Harsh Patel',
    author_email='pharsh58@gmail.com',
    description='Recursive and Incremental backup utility',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/harsh8398/backup.py',
    packages=['backup'],
    scripts=['bin/pybackup'],
    package_data={"": ["LICENSE.txt"]},
    install_requires=[
        "tqdm"
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    zip_safe=False
)

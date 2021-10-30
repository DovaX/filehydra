import setuptools
    
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='filehydra',
    version='0.1.0',
    author='DovaX',
    author_email='dovax.ai@gmail.com',
    description='A Python package focusing on file management and routine file operations',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DovaX/filehydra',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          
     ],
    python_requires='>=3.6',
)
    
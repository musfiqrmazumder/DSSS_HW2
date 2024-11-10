from setuptools import setup, find_packages

setup(
    name='math_quiz',  # Name of your package
    version='0.1',
    description='A math quiz package with functions and unit tests',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Md Musfiqur Rahman Mazumder',
    author_email='musfiqrmazumder@gmail.com',
    url='https://github.com/musfiqrmazumder/DSSS_HW2.git',
    packages=find_packages(),
    install_requires=[  # project dependencies

    ],
    classifiers=[  # Optional: provides additional metadata
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    license="Apache License 2.0",
)

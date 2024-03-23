from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='laeplooth',
    packages=find_packages(include=['laeplooth']),
    version='0.2.2',
    description='Translator for loo language',
    author='most.warong',
    install_requires=[
       'Thaispoon==0.0.2'
    ],
    entry_points={
        'console_scripts': [
            'laeplooth = laeplooth:loo'
        ]
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)

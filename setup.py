from setuptools import setup, find_packages

setup(
    name="wimh",
    version=open('wimh/_version').read(),
    description="wimh What's inside my home",
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    author='alekgr',
    author_email='alek.grigorian@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown', 
    url='https://gitlab.com/Alekgr/wimh',
    entry_points={
        "console_scripts": [
            "wimh=wimh.wimh:main",
            ]
    },
   
    install_requires=[
        'argparse',
        'python-magic'
    ]

)

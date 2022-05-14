"""
Lab setup 

"""
from setuptools import setup

setup(
    name="LAB",
    version="1.0.0",
    description="Automated LAB",
    packages=['LAB'],
    
    install_requires=[
        "click",
        "questionary"
    		],
    
    entry_points={
        'console_scripts': ['LAB=LAB.__main__:main']
                },

)


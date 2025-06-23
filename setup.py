## why this file
# It allows developers to specify information such as the package name, version, dependencies, and other details required for packaging and distribution.

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='ML_project',
version='0.0.1',
author='Ayush Kumar',
author_email='pawar85060@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)


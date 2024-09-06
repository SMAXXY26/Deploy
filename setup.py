from setuptools import find_packages,setup
from typing import List
DOT="-e ."

def get_req(file_path:str)->List[str]:
    """
    this function will return requirements
    """
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n", " ") for req in requirements]
        if DOT in requirements:
            requirements.remove(DOT)
    return requirements


setup(
    name='deploy',
    author='Vinesh Sinku',
    author_email='Vineshsinku@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requirements=get_req('requirements.txt')
)
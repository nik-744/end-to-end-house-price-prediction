from setuptools import find_packages,setup
from typing import List

def get_req(file_path :str)-> List[str]:

    HYPEN_E_DOT = '-e .'
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='house price prediction',
    version='0.0.1',
    author='nikhil',
    author_email='kanojiyanikhil233@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')

)

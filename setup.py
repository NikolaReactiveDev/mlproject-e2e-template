from setuptools import find_packages, setup
from  typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function should read requirements.txt file or any other given file,
    in order to read and return list of strings 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements ]
    if "-e ." in requirements:
        requirements.remove("-e .")
    return requirements

setup(
    name="mlproject-e2e-template",
    version="0.0.1",
    author="NikolaReactiveDev",
    author_email="nikolareactivedev@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
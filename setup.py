from setuptools import find_packages, setup
from typing import List

HYPEN_E_EDOT = '-e.'

def get_requirements(file_path: str) -> List[str]:
    '''
    The function returns the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_EDOT in requirements:
            requirements.remove(HYPEN_E_EDOT)

    return requirements

setup(
    name='ml_fb_comment',
    version='0.01',
    author='Olu Sobayo',
    author_email='holukayodeh@yahoo.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

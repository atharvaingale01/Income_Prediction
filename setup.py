from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = '-e .'

def get_requirements(filepath: str) -> List[str]:
    requirement = []

    with open(filepath) as file_obj:
        requirement = file_obj.readlines()
        requirement = [i.replace("\n","") for i in requirement]

        if HYPHON_E_DOT in requirement:
            requirement.remove(HYPHON_E_DOT)

setup(name='ML_Pipeline',
      version="0.0.1",
      description="Income Prediction",
      author='Atharva Ingale',
      author_email='atharvaingale01@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements('requirement.txt')
      )


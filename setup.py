from setuptools import find_packages, setup

HYPHEN_DOT_E = '-e .'
def get_requirements(file_path:str):
    req = []
    with open(file_path) as f:
        req = f.readlines()
        req = [req.replace("\n","") for req in req]

        if HYPHEN_DOT_E in req:
            req.remove(HYPHEN_DOT_E)
    
setup(
    name='mlproject',
    packages=find_packages(),
    version='0.0.1',
    description='A short description of the project.',
    author='Shubham',
    install_requires=get_requirements('requirements.txt'),
)
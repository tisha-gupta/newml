from setuptools import find_packages, setup
#find_packages -- this is find all the packages that are available in the entire ML directory that we hv made
from typing import List
#'List[str]' for this to work 

#HYPHEN_E_DOT = '-e .'

#Creating a function for importing packages
#'file_path: str' --- this tells that we have to take txt file
#'->List[str]' --- this tells us that the function will return a list, list of text in the .txt file
def get_requirements(file_path: str) ->List[str]: 
    '''
    this function will return a list of requirement
    '''
    requirements=[]

    #opening a file as a temporary file object i.e. 'file_obj'
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()#readlines helps reading lines one by one 
        #Whenever we readlines '\n' is also added, so we will replace '\n' with a blank
        requirements = [req.replace("\n", "") for req in requirements]

        #In order to not get '-e .' from the requirements
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements




#Detals about our package i.e. the project we are creating
setup(
    name = 'newml',
    version = '0.0.1',
    author = 'Tisha',
    author_email = 'tishacourage@gmail.com',
    packages = find_packages(),

    #install_requires = ['pandas','numpy','seaborn'] #The list of names of package we require to be installed
    #So there will be a scenario where we eill be requiring 100s of packages to be imported 
    #So this way of importing all packages is not a feasible way

    #So what we can do is, we can create a function in which we import all the requirements 
    #And that function we can call it here
    #the text file that we are using 
    #And in this file we can mention the names of the packages that we want to import
    install_requires = get_requirements('requirements.txt')
)
from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='starsmiles',
      version="0.0.0",
      description="Star Smiles Model (First local test)",
      license="MIT",#???
      author="Tanja Durova",
      author_email="tatyana.durova@gmail.com",
      #url="https://github.com/tdurova/starsmiles",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests", #???
      # include_package_data: to install data from MANIFEST.in ???
      include_package_data=True,
      zip_safe=False)

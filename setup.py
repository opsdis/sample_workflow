


#from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import setup, find_packages

from manage_version import get_version


def read(fname):
    return open(join(dirname(__file__), fname)).read()


setup(
    name='hello',
    version=get_version(),
    packages=find_packages(),
    author='thenodon',
    author_email='anders@opsdis.com',
    url='https://github.com/opsdis/sample_workflow',
    license='GPLv3',
    include_package_data=True,
    zip_safe=False,
    description='HelloWorld',
    install_requires=read('requirements.txt').split(),
    python_requires='>=3.6',
)

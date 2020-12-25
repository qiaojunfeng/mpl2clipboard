
from setuptools import setup, find_packages

setup(
    name='mpl2clipboard',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Copy matplotlib image to clipboard',
    long_description=open('README.md').read(),
    install_requires=['matplotlib', 'PySide2'],
    url='https://github.com/qiaojunfeng/mpl2clipboard',
    author='Junfeng Qiao',
    author_email='qiaojunfeng@outlook.com'
)

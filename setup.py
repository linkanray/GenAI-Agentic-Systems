from setuptools import setup, find_packages

setup(
    name='genai agentic systems examples',
    # url='',
    author='liray',
    # Needed to actually package something
    packages=find_packages(),
    # Needed for dependencies
    install_requires=['numpy'],
    version='v1',
    # The license can be anything you like
    license='MIT',
    description='Examples of agentic systems.',
)
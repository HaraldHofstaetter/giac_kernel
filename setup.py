from setuptools import setup

setup(name='giac_kernel',
      version='0.0.1',
      description='Giac kernel for Jupyter',
      author='Harald Hofstätter',
      author_email='hofi@harald-hofstaetter.at',
      url='https://github.com/HaraldHofstaetter/giac_kernel',
      packages=['giac_kernel'],
      scripts=['giac_kernel/install.py'],
      keywords=['jupyter', 'notebook', 'kernel', 'giac'],
      include_package_data=True
      )

from setuptools import setup
from Cython.Build import cythonize

setup(name='simpy-cython',
      version='0.0.1',
      description='Simpy fork, that is compiled with cython',
      url='https://github.com/chaosmail/simpy-cython',
      author='Christoph Koerner',
      author_email='office@chaosmail.at',
      license='MIT',
      packages=['simpyx'],
      ext_modules = cythonize("simpyx/*.pyx"),
      install_requires=[
          'simpy==3.0.2',
      ],
      zip_safe=False)

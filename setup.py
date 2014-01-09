from setuptools import setup
from Cython.Build import cythonize

setup(name='simpyx',
      version='0.0.1',
      description='Simpy fork, that is compiled with cython',
      url='https://github.com/chaosmail/simpy-cython',
      author='Christoph Koerner',
      author_email='office@chaosmail.at',
      license='MIT',
      packages=['simpyx'],
      ext_modules = cythonize(["simpyx/*.py","simpyx/resources/*.py"]),
      zip_safe=False)

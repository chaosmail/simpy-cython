from setuptools import setup
from Cython.Build import cythonize

ext_options = {"compiler_directives": {"profile": True}, "annotate": True}

setup(name='simpyx',
      version='0.0.1',
      description='Simpy fork, that is compiled with cython',
      url='https://github.com/chaosmail/simpy-cython',
      author='Christoph Koerner',
      author_email='office@chaosmail.at',
      license='MIT',
      requires=['cython'],
      ext_modules=cythonize(["simpyx/*.py"], nthreads=4, **ext_options),
      zip_safe=False)

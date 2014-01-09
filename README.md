# Simpy 3.0.2 Fork :: Compiled with Cython

## Dependencies for compiling with cython

* Install Cython
* Install gcc

## Installation

```
python setup.py install
```

## Usage

In your existing code, make this change:
``` python
import simpyx as simpy
```

## Reults of Simple Benchmark

[Bank Renege](https://simpy.readthedocs.org/en/latest/examples/bank_renege.html)
```
('simpy: ', 0.004045009613037109)
('simpyx:', 0.001714944839477539)
```

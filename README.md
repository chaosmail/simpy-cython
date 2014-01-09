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

For running the benchmarks there should also be the pure python simpy-3.0.2 installed.

[Bank Renege](https://simpy.readthedocs.org/en/3.0.2/examples/bank_renege.html)
```
('simpy: ', 0.004045009613037109)
('simpyx:', 0.001714944839477539)
```

[Movie Renege](https://simpy.readthedocs.org/en/3.0.2/examples/movie_renege.html)
```
('simpy: ', 0.009849071502685547)
('simpyx:', 0.007219076156616211)
```

[Machine Shop](https://simpy.readthedocs.org/en/3.0.2/examples/machine_shop.html)
```
('simpy: ', 0.2819509506225586)
('simpyx:', 0.24776101112365723)
```

[Gas Station Refueling](https://simpy.readthedocs.org/en/3.0.2/examples/gas_station_refuel.html)
```
('simpy: ', 0.0065860748291015625)
('simpyx:', 0.004212856292724609)
```
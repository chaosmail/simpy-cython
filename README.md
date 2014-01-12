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
simpy:  0.00413833856583
simpyx: 0.001937520504
```

[Movie Renege](https://simpy.readthedocs.org/en/3.0.2/examples/movie_renege.html)
```
simpy:  0.0102033233643
simpyx: 0.00770617961884
```

[Machine Shop](https://simpy.readthedocs.org/en/3.0.2/examples/machine_shop.html)
```
simpy:  0.292090582848
simpyx: 0.264786791801
```

[Gas Station Refueling](https://simpy.readthedocs.org/en/3.0.2/examples/gas_station_refuel.html)
```
simpy:  0.00685012340546
simpyx: 0.0042598772049
```
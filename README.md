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

## Results of simpy-benchmark

The source of the benchmark can be found here: https://bitbucket.org/chaosmail/simpy-benchmarks

```
Best of 20 runs:
Running benchmarks for rev. 3.0.2 ...
Running simpy3[3.0.2].simple_sim(316, 316) ...
... 0.36s
Running simpy3[3.0.2].simple_sim(10, 10000) ...
... 0.32s
Running simpy3[3.0.2].simple_sim(10000, 10) ...
... 0.44s
Running simpy3[3.0.2].wait_for_proc(100, 100) ...
... 0.19s
Running simpy3[3.0.2].condition_events(10000) ...
... 0.50s
Running simpy3[3.0.2].condition_wait(10000) ...
... 0.92s

Running benchmarks for rev. None ...
Running simpy3x[None].simple_sim(316, 316) ...
... 0.27s
Running simpy3x[None].simple_sim(10, 10000) ...
... 0.23s
Running simpy3x[None].simple_sim(10000, 10) ...
... 0.34s
Running simpy3x[None].wait_for_proc(100, 100) ...
... 0.16s
Running simpy3x[None].condition_events(10000) ...
... 0.41s
Running simpy3x[None].condition_wait(10000) ...
... 0.77s
```

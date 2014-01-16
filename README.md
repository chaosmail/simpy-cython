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

## Optimizations

Here is a profile of the [Machine Shop](https://simpy.readthedocs.org/en/3.0.2/examples/machine_shop.html) Demo, which shows the functions, that should be optimized.
```
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    36195    0.076    0.000    0.249    0.000 demos/machine-shop-profile.py:63(working)
    41449    0.069    0.000    0.403    0.000 core.py:194(step)
    32785    0.054    0.000    0.075    0.000 /usr/lib/python2.7/random.py:382(normalvariate)
    38494    0.041    0.000    0.317    0.000 events.py:276(_resume)
    36910    0.029    0.000    0.051    0.000 events.py:169(__init__)
    41466    0.027    0.000    0.027    0.000 core.py:181(schedule)
        1    0.016    0.016    0.419    0.419 core.py:87(run)
    32785    0.015    0.000    0.090    0.000 demos/machine-shop-profile.py:44(time_per_part)
    46489    0.014    0.000    0.014    0.000 {math.log}
     3855    0.012    0.000    0.020    0.000 resource.py:209(_do_put)
    91564    0.008    0.000    0.008    0.000 {method 'random' of '_random.Random' objects}
     1584    0.005    0.000    0.005    0.000 resource.py:108(append)
     1584    0.004    0.000    0.020    0.000 base.py:32(__init__)
     1375    0.004    0.000    0.007    0.000 events.py:252(interrupt)
     1579    0.004    0.000    0.017    0.000 resource.py:47(__exit__)
     1579    0.004    0.000    0.009    0.000 base.py:80(__init__)
    37325    0.004    0.000    0.004    0.000 core.py:155(now)
     1579    0.004    0.000    0.015    0.000 base.py:171(_trigger_put)
     1584    0.003    0.000    0.023    0.000 resource.py:80(__init__)
     3855    0.003    0.000    0.006    0.000 resource.py:162(_do_put)
```

"""
Movie renege example

Covers:

- Resources: Resource
- Condition events
- Shared events

Scenario:
  A movie theatre has one ticket counter selling tickets for three
  movies (next show only). When a movie is sold out, all people waiting
  to buy tickets for that movie renege (leave queue).

"""
import timeit
import sys, os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def avg(l):
    return sum(l) / float(len(l))

setup = """
import collections
import random


RANDOM_SEED = 42
TICKETS = 50  # Number of tickets per movie
SIM_TIME = 120.0  # Simulate until

def moviegoer(env, movie, num_tickets, theater):
    with theater.counter.request() as my_turn:
        # Wait until its our turn or until the movie is sold out
        result = yield my_turn | theater.sold_out[movie]

        # Check if it's our turn of if movie is sold out
        if my_turn not in result:
            theater.num_renegers[movie] += 1
            env.exit()

        # Check if enough tickets left.
        if theater.available[movie] < num_tickets:
            # Moviegoer leaves after some discussion
            yield env.timeout(0.5)
            env.exit()

        # Buy tickets
        theater.available[movie] -= num_tickets
        if theater.available[movie] < 2:
            # Trigger the "sold out" event for the movie
            theater.sold_out[movie].succeed()
            theater.when_sold_out[movie] = env.now
            theater.available[movie] = 0
        yield env.timeout(1)


def customer_arrivals(env, theater):
    while True:
        yield env.timeout(random.expovariate(1 / 0.5))

        movie = random.choice(theater.movies)
        num_tickets = random.randint(1, 6)
        if theater.available[movie]:
            env.process(moviegoer(env, movie, num_tickets, theater))


Theater = collections.namedtuple('Theater', 'counter, movies, available, '
                                            'sold_out, when_sold_out, '
                                            'num_renegers')


# Setup and start the simulation
#print('Movie renege')
random.seed(RANDOM_SEED)
env = simpy.Environment()

# Create movie theater
counter = simpy.Resource(env, capacity=1)
movies = ['Python Unchained', 'Kill Process', 'Pulp Implementation']
available = {movie: TICKETS for movie in movies}
sold_out = {movie: env.event() for movie in movies}
when_sold_out = {movie: None for movie in movies}
num_renegers = {movie: 0 for movie in movies}
theater = Theater(counter, movies, available, sold_out, when_sold_out, num_renegers)

# Start process and run
env.process(customer_arrivals(env, theater))

"""

setup_simpy = "import simpy" + setup
setup_simpyx = "import simpyx as simpy" + setup

print "simpy: ", avg(timeit.Timer('env._now=0; env.run(until=SIM_TIME)', setup=setup_simpy).repeat(100, 1000))
print "simpyx:", avg(timeit.Timer('env._now=0; env.run(until=SIM_TIME)', setup=setup_simpyx).repeat(100, 1000))

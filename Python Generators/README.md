# Generators, Context Managers and

## Generators

### What is a generator

- A simple way to create an iterator

### Generator function vs normal function

- Generator function contains one or more `yield` statements.
- When called, it returns an object (iterator) but does not start execution immediately.
- Methods like `__iter__()` and `__next__()` are implemented automatically. So we can iterate through the items using next().
- Once the function yields, the function is paused and the control is transferred to the caller.
- Local variables and their states are remembered between successive calls.
- When the function terminates, StopIteration (use except to catch) is raised automatically on further calls.
- Unlike normal functions, the local variables are not destroyed when the function yields. Furthermore, the generator object can be iterated only once.
- Generators can be used in for loops directly

```Python
def generator_function(x):
  for x in range(-x,x+1):
    yield x

for i in generator_function(100):
  print(i)
```

## Generator pattern:

1. Function that defines a generator
   1. Calling the function to get a generator object (the actual generator)
2. Create an iterable by putting the iterable in `iter(iterable)`

```Python
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

next(my_gen)
next(my_gen)
next(my_gen)
```

```Python
# python generators with a loop
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
   yield i

even_integers_generator_object = even_integers_generator()

next(even_integers_generator_object)
```

### Ways to consume a generator

1. `next(generator_object)` to step through the generator
2. `list(generator_object)` , `set(generator_object)` etc
3. comprehensions:
   1. list
   2. set
   3. generator
4. loops

### Pipelining generators

```Python
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))
```

```Python
# adding separate_names generator as another stage in pipeline

def separate_names(names):
	for full_name in names:
		for name in full_name.split(' '):
			yield name


full_names = (name.strip() for name in open('names.txt'))
names = separate_names(full_names)
lengths = ((name, len(name)) for name in names)
longest = max(lengths, key=lambda x:x[1])
```

### Why use generators

- Easy to implement
  - Generators can be implemented in a clear and concise way as compared to their iterator class counterpart.
- Memory efficient
  - A normal function to return a sequence will create the entire sequence in memory before returning the result. Generator implementation of such sequences is memory friendly as it only produces one item at a time.
- Represent Infinite Stream
  - Generators are excellent mediums to represent an infinite stream of data. Infinite streams cannot be stored in memory, and since generators produce only one item at a time, they can represent an infinite stream of data.
- Pipelining Generators
  - Multiple generators can be used to pipeline a series of operations.

## Context managers

### Basic context manager framework

```Python
from contextlib import contextmanager

@contextmanager
def simple_context_manager(obj):
    try:
        do_something
        yield
    finally:
        wrap_up
```

### More context manager examples

```Python
# this is a context manager

from contextlib import contextmanager
from logging import Logger, FileHandler

# a very simple example
#@contextmanager
def simple_context_manager(obj):
    try:
        obj.some_property += 1
        yield
    finally:
        obj.some_property -= 1

class Other_scm():
    def __init__(self, obj):
        self.obj = obj
    def __enter__(self):
        self.obj.some_property+=1
    def __exit__(self, *args):
        self.obj.some_property-=1

# a more complex example
@contextmanager
def error_logging(logger, level):
    oldlevel = logger.level
    try:
        logger.setLevel(level)
        yield
    finally:
        logger.setLevel(oldlevel)

if __name__ == "__main__":
    logger = Logger('name',20)
    handler = FileHandler('flog.log')
    logger.addHandler(handler)
    logger.info('this will get logged')
    with error_logging(logger, 30):
        logger.info('this will not get logged')
    logger.info('this will get logged because the level is {}'.format(logger.level))

class Simple_obj(object):
    def __init__(self, arg):
        self.some_property = arg

s = Simple_obj(5)
with simple_context_manager(s):
    print s.some_property
```

### with...as... context manager

```Python
from time import time
from contextlib import contextmanager

HEADER = "this is the header \n"
FOOTER = "\nthis is the footer \n"


@contextmanager
def new_log_file(name):
    try:
        logname = name
        f = open(logname, 'w')
        f.write(HEADER)
        yield f
    finally:
        f.write(FOOTER)
        print "logfile created"
        f.close()
```

## Coroutine

- Must always call next first on a raw coroutine before you can use it
- Use `.send` method to pass it a value e.g. `coroutine_object.send(a_value)`

### Simplest couroutine

```Python
def coroutine_example():
    while True:
        x = yield
        #do something with x
        print x
```

### Coroutine convenience decorator to automatically call next on the coroutine generated

```Python
def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return wrap
****

@coroutine_decorator
def coroutine_example():
    while True:
        x = yield
        #do something with x
        print x
```

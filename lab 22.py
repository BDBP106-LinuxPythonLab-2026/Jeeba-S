#q1
def greet_decorator(func):
    def wrapper():
        print("hello world")
        func()
        print("hello again")
    return wrapper

@greet_decorator
def message():
    print("This is my first attempt at using decorator.")
message()

#q2
def before_after(func):
    def wrapper():
        print ("start")
        func()
        print("finish")
    return wrapper
@before_after
def calculate():
    print("Calculating...")
calculate()

#q3
def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        func()
        print("count is", count)
    return wrapper
@count_calls
def say_hi():
    print("Hi!")
say_hi()
say_hi()

#q4
def check_positive(func):
    def wrap(x):

        if x > 0:
            func(x)
        else:
            print("num should be positive")

    return wrap
@check_positive
def is_pos(x):
    print("num is",x)
is_pos(2)
is_pos(0)
is_pos(-4)
is_pos(1)

#q5
import time
import math
def fac(func):
    def time_taken(x):
        start = time.perf_counter()
        func(x)
        end=time.perf_counter()
        print(end-start)
    return time_taken
@fac
def f(x):
    print(math.factorial(x))
f(50)

#q6
import math

def population_growth(i, r, t):
    def exponential_growth():
        a = r * t
        b = math.e ** a
        c = i * b
        return c

    result = exponential_growth()
    print(round(result))

population_growth(4, 2, 6)   

#q7
import math
import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def timed(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return timed

@measure_time
def population_growth(initial_population, rate, time_period):
    return round(initial_population * math.exp(rate * time_period))

print(population_growth(4, 2, 6))

#q8
def analyze_dna(x):
    def gc_content():

        count_gc = 0
        count_at = 0
        a=x.lower()
        for i in a:
            if i=="g" or i=="c":
                count_gc+=1
            else:
                count_at=count_at+1
        r=count_gc/(count_at+count_gc)*100
        print(r)
        return r
    a=gc_content()

    if a>50:
        print("gc rich")
    else:
        print("at rich")
analyze_dna("AtgcC")
analyze_dna("ATTgc")

#q9
def log_function_call(func):
    def wrapper():
        print("analyzing")
        s=func()
        print("done")
        return s
    return wrapper

def analyze_dna(x):
    @log_function_call
    def gc_content():

        count_gc = 0
        count_at = 0
        a=x.lower()
        for i in a:
            if i=="g" or i=="c":
                count_gc+=1
            else:
                count_at=count_at+1
        r=count_gc/(count_at+count_gc)*100
        print(r)
        return r
    a=gc_content()

    if a>50:
        print("gc rich")
    else:
        print("at rich")
analyze_dna("AtgcC")
analyze_dna("ATTgc")















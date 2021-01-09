
from concurrent.futures import ThreadPoolExecutor
import os

def func1():
    print("in func1")

def func2():
    print("in func2")

with ThreadPoolExecutor(max_workers=None) as pool:
    pool.submit(func1)
    pool.submit(func2)
    print(pool.values)


print(os.cpu_count())


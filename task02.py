""" Here's a not very efficient calculation function that calculates something important::
    
    import time
    import struct
    import random
    import hashlib

    def slow_calculate(value):
        ""Someweirdvoodoomagiccalculations""
        time.sleep(random.randint(1,3))
        data = hashlib.md5(str(value).encode()).digest()
        return sum(struct.unpack('<' + 'B' * len(data), data))

Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""

import time
import struct
import random
import hashlib
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def calculate_total_sum():
    pool = Pool()
    total_sum = sum(pool.map(slow_calculate, range(501)))
    pool.close()
    pool.join()
    return total_sum


start_time = time.time()
total_sum = calculate_total_sum()
end_time = time.time()

print('Total Sum:', total_sum)
print('Calculation Time:', end_time - start_time)

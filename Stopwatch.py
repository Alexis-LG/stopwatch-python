import sys
import timeit


def start_counter():
    start_time = timeit.default_timer()
    return start_time


def count_time():
    sys.stdout.write("\r")
    current_time = start_counter()
    sys.stdout.write(current_time.__str__())
    sys.stdout.flush()

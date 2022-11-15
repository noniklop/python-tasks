import multiprocessing
from functools import wraps
import time

N = 300000000


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {round(total_time, 3)}')
        return result

    return timeit_wrapper

@timeit
def simple_iteration():
    res = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            res += i

    return res

@timeit
def several_for_loops():
    res = 0
    for i in range(3, N, 3):
        res += i
    for i in range(5, N, 5):
        res += i
    for i in range(15, N, 15):
        res -= i
    return res

@timeit
def iterate_over_fifteen():
    range_diff = [0, 3, 5, 6, 9, 10, 12]
    res = 0
    for i in range(0, N, 15):
        for d in range_diff:
            v = i + d
            if v >= N:
                break
            res += v

    return res

@timeit
def math_formula():
    upper = N - 1
    threes = int(3 * (upper / 3) * ((upper / 3) + 1) / 2)
    fives = int(5 * (upper / 5) * ((upper / 5) + 1) / 2)
    fifteens = int(15 * (upper / 15) * ((upper / 15) + 1) / 2)
    res = threes + fives - fifteens

    return res


def run_all_calculations_in_parallel():
    proc1 = multiprocessing.Process(target=simple_iteration)
    proc2 = multiprocessing.Process(target=several_for_loops)
    proc3 = multiprocessing.Process(target=iterate_over_fifteen())
    proc4 = multiprocessing.Process(target=math_formula())

    process = (proc1, proc2, proc3, proc4)

    for proc in process:
        proc.start()
    for proc in process:
        proc.join()

    # Use multiprocessing library to run all above functions in parallel
    # Print execution time of each function


if __name__ == '__main__':
    run_all_calculations_in_parallel()

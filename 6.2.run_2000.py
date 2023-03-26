"""
Writer: Ranel Ben Simman Tov
"""
import time


def timer(f, *args, **kwargs):
    """
    Execute a function and return the time it took to run.
    :param f: the function to run
    :param args: the arguments to pass to the function
    :param kwargs: the keyword arguments to pass to the function
    :return: the time it took to run the function
    """
    start = time.perf_counter()
    # run the function with the given arguments
    f(*args, **kwargs)
    end = time.perf_counter()
    # return the time it took to run the function
    return end - start


if __name__ == '__main__':
    # some tests to check the timer function
    print("print execution time: {:.8f} seconds".format(timer(print, "Hello World!")))
    print("zip execution time: {:.8f} seconds".format(timer(zip, [1, 2, 3], [4, 5, 6])))
    print("format execution time: {:.8f} seconds".format(timer("Hi {name}".format, name="Bug")))
    print("sorted execution time: {:.8f} seconds".format(timer(sorted, [1, 3, 2, 5, 4])))

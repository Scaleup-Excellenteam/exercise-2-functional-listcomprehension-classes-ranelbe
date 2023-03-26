"""
Writer: Ranel Ben Simman Tov
"""


def group_by(func, iterable):
    """
    group the items in the iterable by the result of the given function
    :param func: the function to group by
    :param iterable: the iterable to group
    :return: a dictionary with the results of the function as keys and the items as values
    """
    grouped = {func(item): [] for item in iterable}
    for item in iterable:
        grouped[func(item)].append(item)
    return grouped


if __name__ == "__main__":
    # test to check the group_by function
    print(group_by(len, ["hi", "bye", "yo", "try"]))

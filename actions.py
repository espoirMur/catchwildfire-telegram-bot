def bisect(n, mapper, tester):
    """
    Runs a bisection.

    - `n` is the number of elements to be bisected
    - `mapper` is a callable that will transform an integer from "0" to "n"
      into a value that can be tested
    - `tester` returns true if the value is within the "right" range
    """

    if n < 1:
        raise ValueError('Cannot bissect an empty array')

    left = 0
    right = n - 1

    while left + 1 < right:
        mid = int((left + right) / 2)
        val = mapper(mid)
        tester_values = tester(val)
        if tester_values:
            right = mid
        else:
            left = mid

    return mapper(right)


def tester_function(index, responses=[]):
    """
    this function takes an array of user input and the index
    and return a message with the response at the given index
    response : array
    index : integer
    """
    response = responses[index].lower()
    return response.lower() == 'yes'

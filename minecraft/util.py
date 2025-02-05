import collections

def flatten(l):
    for e in l:
        if isinstance(e, collections.Iterable) and not isinstance(e, str):
            for ee in flatten(e): yield ee
        else: yield e

def flatten_parameters(l):
    return ",".join(map(str, flatten(l)))

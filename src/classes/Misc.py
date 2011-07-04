__author__ = 'prian'
import inspect
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

def enumKey(enum, index):
    for field in inspect.getmembers(enum):
        if field[1] == index:
            return field[0]
    return ''
import numpy as np
import random
import math
def get_state():
    n = random.choice([3,4,5,6])
    state = list(range(n**2))
    random.shuffle(state)
    print(np.array(state).reshape(n,n))
    return state
st = get_state()
print(st)

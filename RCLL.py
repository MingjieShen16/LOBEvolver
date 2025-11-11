import numpy as np

def piece_wise_constant_values(times,delta0,t_grid):
    idx = np.searchsorted(times, t_grid, side='right')-1
    idx = np.clip(idx, 0, len(times)-1)
    return delta0[idx]

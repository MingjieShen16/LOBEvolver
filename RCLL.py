import numpy as np

def piece_wise_constant_values(times,delta0,t_grid):
    idx = np.searchsorted(times, t_grid, side='right')-1
    idx = np.clip(idx, 0, len(times)-1)
    return delta0[idx]

def extract_windows_from_grid(values, window_size,stride):
    n_windows = (len(values) - window_size) // stride +1
    windows = np.zeros((n_windows, window_size, values.shape[1]))
    for i in range(n_windows):
        windows[i] = values[i*stride:i*stride + window_size]
        
    return windows


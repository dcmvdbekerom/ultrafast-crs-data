# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 11:00:16 2024

@author: bekeromdcmvd
"""

import numpy as np

fnames = [
    'nu_data.npy',
    'sigma_gRmin_data.npy',
    'E0_data.npy',
    'J_clip_data.npy',
    ]

fpath = '../data/CH4_v2'

for fname in fnames:
    print('Compressing '+fname+'... ', end='')
    arr = np.load(fpath + fname)
    np.savez_compressed(fpath+fname[:-1]+'z', arr)
    print('Done!')
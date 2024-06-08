# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 13:18:48 2024

@author: bekeromdcmvd
"""

import numpy as np
import os

data_path = './'

N_ext = 10

fnames = [
    'nu_data.npy',
    'J_clip_data.npy',
    'E0_data.npy',
    'sigma_gRmin_data.npy',    ]

new_path = data_path + '../data_ext/'
os.mkdir(new_path)

for fname in fnames:
    print(fname+'... ', end='')

    data = np.load(fname)
    
    # print(data.shape)
    data_ext = np.zeros((N_ext, *data.shape), dtype=data.dtype, order='F')
    for i in range(N_ext):
        data_ext[i] = data
    data2 = data_ext.reshape(*data.shape[:-1], (N_ext * data.shape[-1]), order='F')
    
    np.save(new_path +fname, data2)
    print('Done!')
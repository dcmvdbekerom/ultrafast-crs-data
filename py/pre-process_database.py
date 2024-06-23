# -*- coding: utf-8 -*-
"""
Created on Sun May 12 15:14:42 2024

@author: bekeromdcmvd
"""
import numpy as np

# print('Loading database... ', end='')
data_path = '../db/'
save_path = '../data/CH4_v2/'

branch_data = np.load(data_path + 'branch_data.npy')
nu_data = np.load(data_path + 'nu_data.npy')
sigma_data = np.load(data_path + 'sigma_data.npy')
J_data = np.load(data_path + 'J_data.npy')
E0_data = np.load(data_path + 'E0_data.npy')
gR_data = np.load(data_path + 'gR_data.npy')

J_Q = J_data[:,branch_data==b'Q']
J_min = np.min(J_Q[0]) #TODO: Shouldn't J start at 0?
J_max = np.max(J_Q[0])

# CH_4 v2 ro-vibrational constants from Olafson 1962 [cm-1]
B0 = 5.2412          # rotational constant, v=0 [cm-1]
D0 = 1.1e-4          # centrifugal constant, v=1 rot. sublevel alpha
B1_b = 5.379         # rot.constant, v=1 rot. sublevel beta (O & S branches)
D1_b = 1.7e-4 

calc_EvJ_1 = lambda J: ( (B1_b*J*(J+1)) - (D1_b*J**2 * (J+1)**2) ) # upper ro-vibrational state energy
calc_EvJ_0 = lambda J: ( (B0  *J*(J+1)) - (D0  *J**2 * (J+1)**2) ) # lower ro-vibrational state energy

sigma_gRmin_data = (sigma_data * np.min(gR_data, 0))

delta_J = branch_data.view(np.int8) - ord('Q')
J_min_k = J_min - np.clip(delta_J, None, 0)
J_max_k = J_max - np.clip(delta_J, 0, None)
J_clip = np.clip(J_data[1,:], J_min_k, J_max_k)
J_clip_data = ((delta_J+2)*(J_max+1) + J_clip).astype(np.int32)

J_arr = np.arange(J_min, J_max + 1)
EvJ_1, EvJ_0 = np.ones((2,J_max+1), dtype=np.float64)*np.nan
EvJ_1[J_min:J_max+1] = calc_EvJ_1(J_arr)
EvJ_0[J_min:J_max+1] = calc_EvJ_0(J_arr)


EvJ_data_arr = np.array([J_min, J_max,
                         EvJ_1, EvJ_0,
                         ], dtype=object)

np.save(save_path + 'nu_data.npy', nu_data)
np.save(save_path + 'sigma_gRmin_data.npy', sigma_gRmin_data)
np.save(save_path + 'E0_data.npy', E0_data)
np.save(save_path + 'J_clip_data.npy', J_clip_data)
np.save(save_path + 'EvJ_data.npy', EvJ_data_arr)




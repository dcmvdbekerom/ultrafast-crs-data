# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:29:21 2023

@author: bekeromdcmvd
"""
#https://stackoverflow.com/questions/19310808/how-to-read-a-v7-3-mat-file-via-h5py
#https://stackoverflow.com/questions/46044613/how-to-import-mat-v7-3-file-using-h5py
#https://stackoverflow.com/questions/17316880/reading-v-7-3-mat-file-in-python
import numpy as np
import matplotlib.pyplot as plt

def loadmat(*vargs, **kwargs):
    
    try:
        import mat73
        mat = mat73.loadmat(*vargs,**kwargs)
    except(TypeError):
        import scipy.io
        mat = scipy.io.loadmat(*vargs,**kwargs)
    
    return mat


fname = '../db/CH4_v1/{:s}_branch.mat'

branch_list = []
nu_list = []
sigma_list = []
J_list = [[],[]]
E0_list = []
gR_list = [[],[]]

N_tot = 0
for branch in ['O', 'P', 'Q', 'R', 'S']:
    mat = loadmat(fname.format(branch))
    N_lines = mat['E0_{:s}'.format(branch)].shape[0]
    N_tot += N_lines
    print('{:s} branch - {:d} lines'.format(branch,N_lines))
    
    branch_list += N_lines*[branch.encode()]
    nu_list += [*mat['omega_{:s}'.format(branch)][:,0]]
    sigma_list += [*mat['sigma_{:s}'.format(branch)][:,0]]
    J_list[0] += [*mat['J_{:s}'.format(branch)][:,0]]
    J_list[1] += [*mat['J_{:s}'.format(branch)][:,1]]
    E0_list   += [*mat['E0_{:s}'.format(branch)][:,0]]
    gR_list[0] += [*mat['gR_{:s}'.format(branch)][:,0]]
    gR_list[1] += [*mat['gR_{:s}'.format(branch)][:,1]]

print('Converting to arrays...')

nu_arr = np.array(nu_list, dtype='<f8')
idx = np.argsort(nu_arr)

nu_arr = nu_arr[idx]
branch_arr = np.array(branch_list, dtype='|S1')[idx]
sigma_arr = np.array(sigma_list, dtype='<f8')[idx]
J_arr = np.array(J_list, dtype='|u1')[:,idx]
E0_arr = np.array(E0_list, dtype='<f8')[idx]
gR_arr = np.array(gR_list, dtype='<u2')[:,idx]

spath = '../db/CH4_v1/'
np.save(spath + 'nu_data.npy', nu_arr)
np.save(spath + 'branch_data.npy', branch_arr)
np.save(spath + 'sigma_data.npy', sigma_arr)
np.save(spath + 'J_data.npy', J_arr)
np.save(spath + 'E0_data.npy', E0_arr)
np.save(spath + 'gR_data.npy', gR_arr)

print('Done!')
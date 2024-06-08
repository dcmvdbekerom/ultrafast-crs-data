# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 22:24:09 2024

@author: bekeromdcmvd
"""

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



# fname = 'CH4spectgram_T296K_4567301lines.mat'
# fname = 'minimalWorkingCode/probe.mat'
# fname = 'CH4spectgram_T296K_3244lines.mat'

fname = '../../DIT-CARS/local/DephasingQbranchCH4/DephasingQbranchCH4_1500K.mat'
mat = loadmat(fname)

np.save('omega.npy', mat['omega'])
np.save('tau.npy',   mat['tau'  ])
np.save('I_CRS_1500K.npy',mat['I_CARS'])

            
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 13:50:33 2016

@author: sheraz
"""

import utils
import matplotlib.pyplot as plt
import pyimpress
fname_mat = '/autofs/cluster/transcend/sheraz/scripts/realtimeMEG/weights.mat'

fig=plt.figure('mainfig',figsize=(25,15)) 
path='/autofs/space/megraid_research/MEG/tal/no_name/160901/'

matData=pyimpress.utils.readMatFile(fname_mat)
weights=matData['weightTop'].ravel()
weights=1.*(weights>.5)

fname_raw=path+'erm1.fif'
freqs,psds_erm=utils.plotPSD(fname_raw,tmax_crop=105,tmax_psd=100,
                             nperseg=4,noverlap=90,multitapper=False,NW=2,weights=weights)

#fname_raw=path+'plate.fif'
#plotPSD(fname_raw, color=(0,1,1), label='Copper Plate')
#
#
#fname_raw=path+'almuniumRing.fif'
#plotPSD(fname_raw,color=(1,0,1),label='Aluminium Ring',tmax_crop=120.85,tmax_psd=120)


fname_raw=path+'copperSulphateSphere.fif'
freqs,psds_ss=utils.plotPSD(fname_raw,tmax_crop=105,tmax_psd=100,
                            nperseg=4,noverlap=90,multitapper=False,NW=2,weights=weights)

plt.plot(freqs,psds_ss, color=(1,0,0), linewidth=3, label='Saline Sphere')
plt.plot(freqs,psds_erm, color=(0,0,1), linewidth=3, label='Empty Room')
plt.ylim(0,.9e-11)
plt.xlim(1,100)

#fname_raw=path+'andyOutofMachine.fif'
#freqs,psds_ao=utils.plotPSD(fname_raw)


#fname_raw=path+'andyINEyesClosed.fif'
#freqs,psds_ai=utils.plotPSD(fname_raw,tmax_crop=150.89,tmax_psd=150,
#                            nperseg=1,noverlap=90,multitapper=True,K=2)

plt.plot(freqs,psds_ss-psds_erm, color=(1,0,0), linewidth=3, label='Saline Sphere - Empty Room')
#plt.plot(freqs,psds_ai-psds_erm, color=(0,0,1), linewidth=3, label='Andy In - Empty Room')


#Setting plot Parameters

plt.xlim(1,1000)
plt.ylim(0,.9e-11)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.xlabel('Frequency (Hz)',fontsize=24)
plt.ylabel(r'$\mathrm{\mathsf{Amplitude (T) \,  \backslash \, \sqrt{Hz}}}$',fontsize=24)
plt.legend(fontsize=24)
plt.grid(b=True, which='minor', color='0.65',linestyle='-')
plt.minorticks_on()
plt.tight_layout()
plt.savefig('ALL_29_August_2016_zoom.png')



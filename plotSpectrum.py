# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 13:50:33 2016

@author: sheraz
"""

import utils
import matplotlib.pyplot as plt
fig=plt.figure('mainfig',figsize=(25,15)) 
path='/autofs/space/megraid_research/MEG/tal/no_name/160829/'


fname_raw=path+'erm.fif'
freqs,psds_erm=utils.plotPSD(fname_raw,tmax_crop=150.89,tmax_psd=150,
                             nperseg=1,noverlap=90,multitapper=True,K=2)

#fname_raw=path+'plate.fif'
#plotPSD(fname_raw, color=(0,1,1), label='Copper Plate')
#
#
#fname_raw=path+'almuniumRing.fif'
#plotPSD(fname_raw,color=(1,0,1),label='Aluminium Ring',tmax_crop=120.85,tmax_psd=120)


fname_raw=path+'salineSphere.fif'
freqs,psds_ss=utils.plotPSD(fname_raw,tmax_crop=150.89,tmax_psd=150,
                            nperseg=1,noverlap=90,multitapper=True,K=2)


#fname_raw=path+'andyOutofMachine.fif'
#freqs,psds_ao=utils.plotPSD(fname_raw)


fname_raw=path+'andyINEyesClosed.fif'
freqs,psds_ai=utils.plotPSD(fname_raw,tmax_crop=150.89,tmax_psd=150,
                            nperseg=1,noverlap=90,multitapper=True,K=2)

plt.plot(freqs,psds_ss-psds_erm, color=(1,0,0), linewidth=3, label='Saline Sphere - Empty Room')
plt.plot(freqs,psds_ai-psds_erm, color=(0,0,1), linewidth=3, label='Andy In - Empty Room')


#Setting plot Parameters

plt.xlim(10,500)
plt.ylim(0,.9e-12)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.xlabel('Frequency (Hz)',fontsize=24)
plt.ylabel(r'$\mathrm{\mathsf{Amplitude (T) \,  \backslash \, \sqrt{Hz}}}$',fontsize=24)
plt.legend(fontsize=24)
plt.grid(b=True, which='minor', color='0.65',linestyle='-')
plt.minorticks_on()
plt.tight_layout()
plt.savefig('ALL_29_August_2016_zoom.png')



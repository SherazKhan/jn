# -*- coding: utf-8 -*-

import utils
import matplotlib.pyplot as plt
import pyimpress
import time

fname_mat = '/autofs/cluster/transcend/sheraz/scripts/realtimeMEG/weights.mat'
matData=pyimpress.utils.readMatFile(fname_mat)
weights=matData['weightTop'].ravel()
weights=1.*(weights>.6)


fig=plt.figure('mainfig',figsize=(25,15)) 
path='/autofs/space/megraid_research/MEG/tal/no_name/160908/'


fname_raw=path+'erm.fif'
freqs,psds_erm=utils.plotPSD(fname_raw,tmax_crop=301,tmax_psd=300,picks ='all',
                             nperseg=1,noverlap=90,multitapper=False,NW=2,weights=weights)

fname_raw=path+'hot.fif'
freqs,psds_hot=utils.plotPSD(fname_raw,tmax_crop=301,tmax_psd=300,picks ='all',
                            nperseg=1,noverlap=90,multitapper=False,NW=2,weights=weights)

fname_raw=path+'erm1.fif'
freqs,psds_erm1=utils.plotPSD(fname_raw,tmax_crop=301,tmax_psd=300,picks ='all',
                             nperseg=1,noverlap=90,multitapper=False,NW=2,weights=weights)

fname_raw=path+'warm.fif'
freqs,psds_warm=utils.plotPSD(fname_raw,tmax_crop=301,tmax_psd=300,picks ='all',
                            nperseg=1,noverlap=90,multitapper=False,NW=2,weights=weights)

fname_raw=path+'erm2.fif'
freqs,psds_erm2=utils.plotPSD(fname_raw,tmax_crop=301,tmax_psd=300,picks ='all',
                             nperseg=1,noverlap=90,multitapper=False,NW=2,weights=weights)


plt.plot(freqs,psds_erm, color=(1,0,0), linewidth=3, label='Empty Room 1')
plt.plot(freqs,psds_erm1, color=(0,0,1), linewidth=3, label='Empty Room 2')
plt.plot(freqs,psds_erm2, color=(0,1,0), linewidth=3, label='Empty Room 3')
plt.plot(freqs,psds_hot, color=(0,0,0), linewidth=3, label='Hot Saline Sphere')
plt.plot(freqs,psds_warm, color=(1,0,1), linewidth=3, label='Warm Saline Sphere')

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
plt.show()
timestr = time.strftime("%Y%m%d-%H%M%S")
plt.savefig(timestr+'.png')



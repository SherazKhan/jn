# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 13:50:33 2016

@author: sheraz
"""
import mne
import utils
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(25,15)) 
ax = fig.add_subplot(111)
path='/autofs/space/megraid_research/MEG/tal/no_name/160829/'


fname_raw=path+'erm.fif'
raw=mne.io.read_raw_fif(fname_raw,preload=True)
raw.crop(0,135)
raw.notch_filter(np.arange(60, raw.info['sfreq']/2, 60), n_jobs=16)
picks = utils.get_Vertex_Channels(raw)
freqs,psds=utils.getPSD(raw,picks,tmin=10,tmax=130)
h1=ax.plot(freqs,psds, color=(1,0,0), linewidth=3, label='Empty Room')

fname_raw=path+'plate.fif'
raw=mne.io.read_raw_fif(fname_raw,preload=True)
raw.crop(0,135)
raw.notch_filter(np.arange(60, raw.info['sfreq']/2, 60), n_jobs=8)
freqs,psds=utils.getPSD(raw,picks,tmin=10,tmax=130)
h2=ax.plot(freqs,psds, color=(0,1,1), linewidth=2, label='Copper Plate')

fname_raw=path+'almuniumRing.fif'
raw=mne.io.read_raw_fif(fname_raw,preload=True)
raw.crop(0,120.85)
raw.notch_filter(np.arange(60, raw.info['sfreq']/2, 60), n_jobs=8)
freqs,psds=utils.getPSD(raw,picks,tmin=10,tmax=120)
h3=ax.plot(freqs,psds, color=(1,0,1), linewidth=2, label='Aluminium Ring')

fname_raw=path+'salineSphere.fif'
raw=mne.io.read_raw_fif(fname_raw,preload=True)
raw.crop(0,135)
raw.notch_filter(np.arange(60, raw.info['sfreq']/2, 60), n_jobs=16)
freqs,psds=utils.getPSD(raw,picks,tmin=10,tmax=130)
h4=ax.plot(freqs,psds, color=(0,1,0), linewidth=3, label='Saline Sphere')

fname_raw=path+'andyOutofMachine.fif'
raw=mne.io.read_raw_fif(fname_raw,preload=True)
raw.crop(0,135)
raw.notch_filter(np.arange(60, raw.info['sfreq']/2, 60), n_jobs=16)
freqs,psds=utils.getPSD(raw,picks,tmin=10,tmax=130)
h5=ax.plot(freqs,psds, color=(0,0,1), linewidth=3, label='Andy Out')

fname_raw=path+'andyINEyesClosed.fif'
raw=mne.io.read_raw_fif(fname_raw,preload=True)
raw.crop(0,135)
raw.notch_filter(np.arange(60, raw.info['sfreq']/2, 60), n_jobs=16)
freqs,psds=utils.getPSD(raw,picks,tmin=10,tmax=130)
h6=ax.plot(freqs,psds, color=(0,0,0), linewidth=3, label='Andy In')


#Setting plot Parameters
ax.set_xlim(100,2000)
ax.set_ylim(0,2e-28)
plt.yticks(fontsize=20, fontweight='bold')
plt.xticks(fontsize=20, fontweight='bold')
ax.set_xlabel('Frequency (Hz)',fontsize=24, fontweight='bold')
ax.set_ylabel('Amplitude',fontsize=24, fontweight='bold')
ax.legend(fontsize=24)
ax.grid(True)
plt.tight_layout()
fig.savefig('ALL_29_August_2016_zoom.png')



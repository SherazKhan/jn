# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 19:24:15 2016

@author: sheraz
"""
import mne
from scipy.signal import welch
import numpy as np

def get_Vertex_Channels(raw):
    selection=mne.read_selection('Vertex')
    selection=selection[2::3]
    selection+=['MEG 0421']
    selec=[item[0:3]+item[-4:] for item in selection]
    picks = mne.pick_types(raw.info, meg='mag', eeg=False, eog=False,
                           stim=False, exclude='bads', selection=selec)
    return picks


def getPSD(raw,picks,tmin=10,tmax=130):
    start, stop = raw.time_as_index([tmin, tmax])                     
    data, _ = raw[picks, start:(stop + 1)]
    freqs,psds_in =welch(np.mean(data,0),fs=raw.info['sfreq'],nperseg=2500,noverlap=2000)
    return freqs,psds_in
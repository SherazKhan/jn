# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 19:24:15 2016

@author: sheraz
"""
import mne
#from scipy.signal import welch
import numpy as np
from spectrum import pmtm as pspec
from numpy.lib import stride_tricks
import matplotlib.pyplot as plt

def subsequences(sig, frameSize, overlapFac=0.75):
    hopSize = int(frameSize - np.floor(overlapFac * frameSize))
    samples = np.append(np.zeros(int(np.floor(frameSize/2.0))), sig)
    cols = np.ceil( (len(samples) - frameSize) / float(hopSize)) + 1
    samples = np.append(samples, np.zeros(frameSize))
    frames = stride_tricks.as_strided(samples, shape=(cols, frameSize), strides=(samples.strides[0]*hopSize, samples.strides[0])).copy()
    return frames


    
def nextpow2(i):
    '''
    Find 2^n that is equal to or greater than.
    '''
    n = 2
    while n < i: n = n * 2
    return n
    
    
def pmtm(y,fs,K):
    '''
    Multi taper estiamtion of PSD with prolate-spheroidal tapers
    
    IN:
    t - time vector
    y - time series
    K - time-bandwidth product
    
    OUT:
    f - vector of frequencies
    Sh - One sided PSD
    '''
    N=y.shape[0]
    Nfft=nextpow2(N)
    z=np.zeros(Nfft-N)
    yz=np.r_[z,y]
    S=pspec(yz,NW=K,show=False)
    #Only keep one sided spectrum
    Sh=S[0:Nfft/2]
    Sh=Sh.flatten()
    return Sh

def get_Vertex_Channels(raw):
    selection=mne.read_selection('Vertex')
    selection=selection[2::3]
    selection+=['MEG 0421']
    selec=[item[0:3]+item[-4:] for item in selection]
    picks = mne.pick_types(raw.info, meg='mag', eeg=False, eog=False,
                           stim=False, exclude='bads', selection=selec)
    return picks


def stft(sig, frameSize, fs, overlapFac=0.75, window=np.hanning):
    frames=subsequences(sig, frameSize, overlapFac=overlapFac)
    win = window(frameSize)
    frames *= win
    freq = np.fft.rfftfreq(frameSize, d=1./fs)
    return freq, np.fft.rfft(frames)

def stmt(sig, frameSize, fs, K=4, overlapFac=0.75):
    frames=subsequences(sig, frameSize, overlapFac=overlapFac)
    psd=np.apply_along_axis(pmtm,1,frames,fs,K)
    dt=1./fs
    Nfft=nextpow2(frameSize)
    freq=np.linspace(0,1/(2*dt),Nfft/2)
    return freq,psd

def getPSD(raw,picks,tmin=10,tmax=130,nperseg=2500,noverlap=2000):
    start, stop = raw.time_as_index([tmin, tmax])                     
    data, _ = raw[picks, start:(stop + 1)]
    #freqs,psds_in =welch(np.mean(data,0),fs=raw.info['sfreq'],nperseg=nperseg,noverlap=noverlap)
    freqs,psds_in =stft(np.mean(data,0),nperseg, raw.info['sfreq'],
                        overlapFac=float(noverlap)/nperseg)
    psds_in=np.mean(abs(psds_in),axis=0)
    return freqs,psds_in
    

def getMTSD(raw,picks,tmin=10,tmax=130,nperseg=2500,noverlap=2000,K=4):
    start, stop = raw.time_as_index([tmin, tmax])                     
    data, _ = raw[picks, start:(stop + 1)]
    freqs,psds_in =stmt(np.mean(data,0),nperseg,raw.info['sfreq'],
                        overlapFac=float(noverlap)/nperseg,K=K)  
    psds_in=np.sqrt(np.mean(psds_in,axis=0))                          
    return freqs,psds_in

def plotPSD(fname_raw,tmin_crop=0,tmax_crop=135,n_jobs=16,tmin_psd=10,
            tmax_psd=130,color=(1,0,0),linewidth=3,label='',nperseg=0.5,noverlap=75,show_plot=False,multitapper=False,K=4):
                
    if  tmax_psd >  tmax_crop:
        tmax_psd = tmax_crop
    raw=mne.io.read_raw_fif(fname_raw,preload=False)
    raw.crop(tmin_crop,tmax_crop).load_data()
    raw.notch_filter(np.arange(60, raw.info['sfreq']/2, 60), n_jobs=n_jobs)
    nperseg=int(nperseg*raw.info['sfreq'])
    noverlap=int((noverlap/100.)*nperseg)
    picks = get_Vertex_Channels(raw)
    if multitapper:
        freqs,psds=getMTSD(raw, picks, tmin=tmin_psd, 
                                 tmax=tmax_psd, nperseg=nperseg, noverlap=noverlap,K=K)
    else:
        freqs,psds=getPSD(raw, picks, tmin=tmin_psd,
                                tmax=tmax_psd, nperseg=nperseg, noverlap=noverlap)
    if show_plot:
        handle=plt.plot(freqs,psds, color=color, linewidth=linewidth, label=label)
        return freqs,psds,handle
    return freqs,psds
    



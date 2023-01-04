# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:45:51 2023

@author: Maxime
"""

import numpy as np
import wave
from scipy.io.wavfile import read

# Lecture du fichier audio
signal, fs = read('022_echange.wav')

# Conversion du signal en tableau numpy
signal = np.array(signal, dtype=float)

# Nombre de points du signal
n_points = len(signal)

# Durée du signal (en secondes)
duration = n_points / fs

# Nombre de fichiers à créer
n_files = int(duration / 0.1)

# Extraction de chaque tranche de 0.1 seconde
for i in range(n_files):
    start = int(i * 0.1 * fs)
    end = int((i+1) * 0.1 * fs)
    chunk = signal[start:end]
    
    # Écriture du fichier audio
    wf = wave.open(f'output_{i+1}.wav', 'w')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(fs)
    wf.writeframes(chunk)
    wf.close()

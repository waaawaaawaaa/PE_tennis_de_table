# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 15:29:03 2023

@author: Maxime
"""

import numpy as np
from scipy.io.wavfile import read
from scipy.stats import pearsonr

# Lecture des fichiers audio
signal1, fs1 = read('reference.wav')
signal2, fs2 = read('022_echange.wav')

# Vérification que les deux fichiers ont la même fréquence d'échantillonnage
if fs1 != fs2:
    print("Les fichiers audio ont des fréquences d'échantillonnage différentes")
    exit()

# Conversion des signaux en tableaux numpy
signal1 = np.array(signal1, dtype=float)
signal2 = np.array(signal2, dtype=float)

# Calcul de la distance de Pearson
correlation, p_value = pearsonr(signal1, signal2)

print(f"Distance de Pearson : {correlation:.3f}")

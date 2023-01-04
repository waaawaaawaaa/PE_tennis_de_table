# PE_tennis_de_table
PE tennis de table 29a


Le fichier python "sequencage_audio.py" permet de découper un audio en sous-audio de durée souhaitée (ici 0.1 sec). Cela permet de réaliser les calculs de cross-corélation 
uniquement sur des durées faibles et de rejeter les parties où le rebond n'a pas lieu. 
Le calcul de cross-corélation permet de savoir, grâce au spectre du signal, si deux audios sont relativement similaires. Ce calcul est fait grâce à l'algorithme 
'crosscorrelation.py"


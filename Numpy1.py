import numpy as np
quilometragem = np.loadtxt('quilometragem.txt')
datafab = np.loadtxt('data-fab.txt')
km_media = quilometragem / (2022-datafab)
print(km_media,'\n')

preco_carros = np.array([88078.64, 106161.94, 72832.16, 124549.07, 92612.1, 97497.73, 56445.2, 112310.44, 120716.27, 76566.49])
media_preco = np.mean(preco_carros, axis=0, dtype=int)
print(media_preco,'R$\n')

preco_total = np.sum(preco_carros, dtype=int)
print(preco_total,'R$\n')

km_0 = np.array(['Jetta Variant', True, 'Passat', False, 'Crossfox', False, 'DS5', True, 'Aston Martin DB4', False, 'Palio Weekend', True, 'A5', False, 'Serie 3 Cabrio', False, 'Dodge Jorney', True, 'Carens', False])
km_0.resize((10,2), refcheck=False)
print(km_0)
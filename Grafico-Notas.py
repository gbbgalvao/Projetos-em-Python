from random import randrange
randrange (1,11)
listtt = []
for i in range (8):
  listtt.append(randrange(1,11))

print (f'As notas são {listtt}\n')

import matplotlib.pyplot as plt
x = list (range(1,9))
y = listtt
plt.plot(x, y, marker = 'o')
plt.title('Notas de matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()
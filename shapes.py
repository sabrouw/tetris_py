# chaque forme correspond à une lettre qui est 
# variable qui contient un tableau
#dans ce tableau il y a des tableau correspondant 
# à leur position debout et allongé

S = [['.00',
      '00.'],
     ['0.',
      '00',
      '.0']]

Z = [['00.',
      '.00'],
     ['..0',
      '.00',
      '.0.']]

I = [['0',
      '0',
      '0',
      '0'],
     ['0000']]

O = [['00',
      '00']]

J = [['0..',
      '000'],
     ['00',
      '0.',
      '0.'],
     ['000',
      '..0'],
     ['.0',
      '.0',
      '00',]]

L = [['..0',
      '000'],
     ['0.',
      '0.',
      '00'],
     ['000',
      '0..'],
     ['00',
      '.0',
      '.0']]

T = [['.0.',
      '000'],
     ['0.',
      '00',
      '0.'],
     ['000',
      '.0.'],
     ['.0',
      '00',
      '.0']]

#les formes (shapes) sont stokée dans un tableau
shapes = [S, Z, I, O, J, L, T]
# On créé un tableau de couleur la couleurs d'une forme est au meme indice
colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
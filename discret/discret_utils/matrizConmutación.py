from discret_utils.utils import binary


class conmutation_Matrix:
    def __init__(self, var=0):
        self.var = var
        self.matrix = []
        self.create()
        
    def print(self):
        [print(i) for i in self.matrix]

    def create(self):
        self.matrix = [[int(element) for element in binary(i).lstrip("0b")]
                                    for i in range(2 ** self.var-1, -1, -1)
                                 ]
        for i in self.matrix:
            while len(i) < self.var:
                i.insert(0,0)

    def __getitem__(self, index):
        return self.matrix[index]

    def reverse(self):
        self.matrix.reverse()
        return self

"""
matriz = Conmutation_Matrix(3)
for index,i in enumerate(matriz.reverse()):
    x, y, z = i 
    print(matriz[index], " = ", int( (not(y) and not(z)) or (x and y) or (not(x) and not(y))  ))
"""

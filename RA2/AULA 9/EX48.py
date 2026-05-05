import numpy as np
matriz = np.array(([1,2,3]
                    ,[4,5,6]
                    ,[7,8,9]
                    ))
diagonal = np.diag(matriz)
print("Elementos da diagonal principal da matriz:")
print(diagonal)
      
      #OU

print(matriz[0][0]
      ,matriz[1][1]
      ,matriz[2][2])
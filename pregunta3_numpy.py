import numpy as np
    b = np.array([[0, 1,  2], [3, 4, 5]])    # arreglo 2 x 3
     b
      array([[0, 1, 2],
       [3, 4, 5]])
     b.ndim
     2
     b.shape
     (2, 3)
     len(b)     # devuelve el tamaño de la primera dimension
     2
     c = np.array([[[1], [2]], [[3], [4]]])
     c
     array([[[1],
        [2]],

       [[3],
        [4]]])
      c.shape
      (2, 2, 1)
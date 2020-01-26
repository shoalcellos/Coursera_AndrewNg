# WARMUPEXERCISE Example function in python
#   eye is an example function that returns the 5x5 identity matrix

import numpy as np

def eye(l=5):

    # ============= YOUR CODE HERE ==============
    # Reading     : https://docs.python.org/3/tutorial/controlflow.html#defining-functions
    #               https://docs.scipy.org/doc/numpy/reference/generated/numpy.identity.html
    # Instructions: Return the 5x5 identity matrix 
    #               In python, we return values by using the return statement
    #               


    return np.identity(l) 
    # ===========================================

def warmUpExercise():
    A = eye()
    print(f"{A}\n")

if __name__ == "__main__":
    warmUpExercise()



    

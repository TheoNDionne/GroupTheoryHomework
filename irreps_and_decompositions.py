"""irreps_and_decomposition.py

A simple script that uses the character table for a group and the characters of one of its representations to determine
the rep's decomposition.

ADD OTHER STUFF
"""

# imports
import numpy as np

# functions
def get_irrep_multiplicity(representation_characters, character_table, elements_per_class):
    """A function that gets the multiplicity of each irrep 
       for real representations using the magic formula.
    """
    # multiply each character by the number of elements in its class
    representation_characters_adjusted = representation_characters*elements_per_class

    # perform a matrix multiplication between the character table and divide by group size
    multiplicity_vector = character_table @ representation_characters_adjusted / np.sum(elements_per_class)

    return multiplicity_vector


# main body of the script
if __name__ == "__main__":

############## AB4 (PG: C4v)

    # define the character table of the PG
    character_table_C4v = np.array([
        [1, 1, 1, 1, 1],
        [1, 1, 1,-1,-1],
        [1, 1,-1, 1,-1],
        [1, 1,-1,-1, 1],
        [2,-2, 0, 0, 0]
    ])  

    # define the number of elements per class
    elements_per_class_C4v = np.array([1,1,2,2,2])

    # the characters of the mechanical representation
    M_characters_C4v = np.array([15,-1,1,1,3])

    # Getting and printing the mutliplicities
    M_multiplicities_C4v = get_irrep_multiplicity(M_characters_C4v, character_table_C4v, elements_per_class_C4v)
    print(M_multiplicities_C4v)
    
    ### OUTPUT : [3. 1. 1. 2. 4.]

############## UF6 (PG: Oh)

    # define the character table of the PG
    character_table_Oh = np.array([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1,-1,-1,-1,-1,-1],
        [1, 1,-1,-1, 1, 1, 1,-1,-1, 1],
        [1, 1,-1,-1, 1,-1,-1, 1, 1,-1],
        [2, 2, 0, 0,-1, 2, 2, 0, 0,-1],
        [2, 2, 0, 0,-1,-2,-2, 0, 0, 1],
        [3,-1, 1,-1, 0, 3,-1, 1,-1, 0],
        [3,-1, 1,-1, 0,-3, 1,-1, 1, 0],
        [3,-1,-1, 1, 0, 3,-1,-1, 1, 0],
        [3,-1,-1, 1, 0,-3, 1, 1,-1, 0]
    ])  

    # define the number of elements per class
    elements_per_class_Oh = np.array([1, 3, 6, 6, 8, 1, 3, 6, 6, 8])

    # the characters of the mechanical representation
    M_characters_Oh = np.array([21,-3, 3,-1, 0,-3, 5,-1, 3, 0])

    # Getting and printing the mutliplicities
    M_multiplicities_Oh = get_irrep_multiplicity(M_characters_Oh, character_table_Oh, elements_per_class_Oh)
    print(M_multiplicities_Oh)
    
    ### OUTPUT : [1. 0. 0. 0. 1. 0. 1. 3. 1. 1.]
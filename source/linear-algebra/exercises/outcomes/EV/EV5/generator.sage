load("../../../source/common/sagemath/library.sage")
TBIL.config_matrix_typesetting()

class Generator(BaseGenerator):
    def data(self):
        A=CheckIt.simple_random_matrix_of_rank(choice([2,3]),rows=4,columns=choice([3,5]))
 
        tasks =  [{
            "basis": False,
            "vecset": TBIL.VectorSet(A.columns()),
            "matrix": A,
            "rref": A.rref(),
        }]

        basis = choice([True,False])
        if basis:
            rank = 4
        else:
            rank = choice([2,3])
        A=CheckIt.simple_random_matrix_of_rank(rank,rows=4,columns=4)
 
        tasks +=  [{
            "basis": basis,
            "vecset": TBIL.VectorSet(A.columns()),
            "matrix": A,
            "rref": A.rref(),
        }]

        basis = not basis
        if basis:
            rank = 4
        else:
            rank = choice([2,3])
        A=CheckIt.simple_random_matrix_of_rank(rank,rows=4,columns=4)
 
        tasks +=  [{
            "basis": basis,
            "vecset": TBIL.VectorSet(A.columns()),
            "matrix": A,
            "rref": A.rref(),
        }]

        shuffle(tasks)

        return {"tasks": tasks}

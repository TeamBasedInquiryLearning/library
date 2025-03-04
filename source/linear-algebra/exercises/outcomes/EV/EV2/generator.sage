load("../../../source/common/sagemath/library.sage")
TBIL.config_matrix_typesetting()

class Generator(BaseGenerator):
    def data(self):
        A=CheckIt.simple_random_matrix_of_rank(choice([2,3]),rows=4,columns=3)
 
        tasks =  [{
            "spans": False,
            "vecset": TBIL.VectorSet(A.columns()),
            "matrix": A,
            "rref": A.rref(),
        }]

        spans = choice([True,False])
        if spans:
            rank = 4
        else:
            rank = choice([2,3])
        A=CheckIt.simple_random_matrix_of_rank(rank,rows=4,columns=4)
 
        tasks +=  [{
            "spans": spans,
            "vecset": TBIL.VectorSet(A.columns()),
            "matrix": A,
            "rref": A.rref(),
        }]

        spans = not spans
        if spans:
            rank = 4
        else:
            rank = choice([2,3])
        A=CheckIt.simple_random_matrix_of_rank(rank,rows=4,columns=5)
 
        tasks +=  [{
            "spans": spans,
            "vecset": TBIL.VectorSet(A.columns()),
            "matrix": A,
            "rref": A.rref(),
        }]

        shuffle(tasks)

        return {"tasks": tasks}

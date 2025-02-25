load("../../../source/common/sagemath/library.sage")
TBIL.config_matrix_typesetting()

class Generator(BaseGenerator):
    def data(self):
        #Pick some  vectors in R4
        n=choice([4,5])
        dim=choice([2,3])
        A=CheckIt.simple_random_matrix_of_rank(dim,columns=n,rows=4)
        basis=[A.column(i) for i in A.pivots()]

        return {
            "vlist": TBIL.VectorSet(A.columns()),
            "basis": TBIL.VectorSet(basis),
            "dimension": dim,
            "matrix": A,
            "rref": A.rref(),
        }

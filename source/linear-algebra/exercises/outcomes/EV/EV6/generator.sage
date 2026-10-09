load("../../../source/common/sagemath/library.sage")
TBIL.config_matrix_typesetting()

class Generator(BaseGenerator):
    def data(self):
        #Choose R^4 or R^5, will use 5 or 4 vectors respectively
        base_dim = choice([4,5])
        vector_count = 9-base_dim
        #answer will be 2 or 3
        dim=choice([2,3])
        A=CheckIt.simple_random_matrix_of_rank(
            dim,
            columns=vector_count,
            rows=base_dim
        )
        basis=[A.column(i) for i in A.pivots()]

        return {
            "vlist": TBIL.VectorSet(A.columns()),
            "basis": TBIL.VectorSet(basis),
            "dimension": dim,
            "matrix": A,
            "rref": A.rref(),
        }

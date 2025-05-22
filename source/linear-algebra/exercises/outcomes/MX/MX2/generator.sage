load("../../../source/common/sagemath/library.sage")
TBIL.config_matrix_typesetting()

class Generator(BaseGenerator):
    def data(self):
        labels = list("ABCDLMNPQ")
        shuffle(labels)
        # invertible matrix
        A=CheckIt.simple_random_matrix_of_rank(4,rows=4,columns=4)
        solution = column_matrix(
            vector(QQ, [randrange(1,5)*choice([-1,1]) for _ in range(4)])
        )
        vars = column_matrix(var("x_1 x_2 x_3 x_4"))
        constants = A*solution
        m = A.augment(constants, subdivide=True)
        matrices = [{
            "matrix": A,
            "rref": A.rref(),
            "invertible": True,
            "inverse": A^(-1),
            "label": labels[0],
            "vars": vars,
            "solution": solution,
            "constant_vector": constants,
            "vector_eq": TBIL.VectorEquation(m),
        }]
        # non-invertible matrix
        A=CheckIt.simple_random_matrix_of_rank(choice([2,3]),rows=4,columns=4)
        constants = A*solution
        m = A.augment(constants, subdivide=True)
        matrices += [{
            "matrix": A,
            "rref": A.rref(),
            "invertible": False,
            "label": labels[1],
            "vector_eq": TBIL.VectorEquation(m),
        }]

        shuffle(matrices)

        return {
            "matrices": matrices,
        }


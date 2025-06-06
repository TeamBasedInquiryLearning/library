load("../../../source/common/sagemath/library.sage")
TBIL.config_matrix_typesetting()

class Generator(BaseGenerator):
    def data(self):
        # shuffle 2,3,4 to get dimensions
        dims = [2,3,4]
        shuffle(dims)

        # create matrices. only first two are multiply-able
        m = list(zip([
            random_matrix(QQ,dims[0],dims[1],algorithm='echelonizable',rank=min(dims[0],dims[1]),upper_bound=7),
            random_matrix(QQ,dims[1],dims[2],algorithm='echelonizable',rank=min(dims[1],dims[2]),upper_bound=7),
            random_matrix(QQ,dims[0],dims[2],algorithm='echelonizable',rank=min(dims[0],dims[2]),upper_bound=7),
        ],["L","R","N"]))
        shuffle(m)

        matrices, indices = zip(*m)

        letters = ["A","B","C"]

        productName = letters[indices.index("L")] + letters[indices.index("R")]
        product = matrices[indices.index("L")] * matrices[indices.index("R")]


        return {
            "A": matrices[0],
            "B": matrices[1],
            "C": matrices[2],
#            "leftMatrix": letters[indices.index("L")],
#            "rightMatrix": letters[indices.index("R")],
#            "leftDim": dims[0],
#            "middleDim": dims[1],
#            "rightDim": dims[2],
            "productName": productName,
            "product": product,
        }

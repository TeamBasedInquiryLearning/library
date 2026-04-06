load("../../../source/common/sagemath/library.sage")
TBIL.config_matrix_typesetting()

class Generator(BaseGenerator):
    def data(self):
        while True:
            # eigenvalues will be two distinct small integers with
            # different absolute values
            l1,l2 = sample(range(2,6),2)
            l1,l2 = l1*choice([-1,1]),l2*choice([-1,1])
            S=random_matrix(QQ, 2, 2, algorithm='echelonizable', rank=2, upper_bound=6)
            A=S.inverse()*matrix([[l1,1],[0,l2]])*S
            # to get roughly consistent difficulty
            if all(abs(a)>5 for a in A.list()):
                break

        # Get an eigenvector
        eigenvector = column_matrix((A-matrix([[l1,0],[0,l1]])).right_kernel(basis='pivot').basis()[0])
        # Scale to get whole numbers
        eigenvector = eigenvector[0].denominator()*eigenvector[1].denominator()*eigenvector

        return {
            "matrix": A,
            "e1": l1,
            "e2": l2,
            "charpoly": A.charpoly('lambda_'),
            "eigenvector": eigenvector,
            "scaled_eigenvector": l1*eigenvector,
        }

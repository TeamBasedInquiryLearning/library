load("../../../source/common/sagemath/library.sage")
TBIL.config_matrix_typesetting()

class Generator(BaseGenerator):
    def data(self):
        while True:
            ls = [choice([-1,1])*i for i in range(2,7)]
            l1,l2 = sample(ls,2)
            S=random_matrix(QQ, 2, 2, algorithm='echelonizable', rank=2, upper_bound=2)
            A=S.inverse()*matrix([[l1,1],[0,l2]])*S
            if all(a!=0 for a in A.list()):
                break

        return {
            "matrix": A,
            "e1": l1,
            "e2": l2,
            "charpoly": A.charpoly('lambda_'),
        }

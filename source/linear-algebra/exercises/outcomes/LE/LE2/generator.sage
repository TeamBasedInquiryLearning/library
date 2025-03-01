load("../../../source/common/sagemath/library.sage")
TBIL.config_matrix_typesetting()

class Generator(BaseGenerator):
    def data(self):
        scenarios = sample([
            {"rref": True},
            {"add": True},
            {"swap": True},
            {"scale": True},
        ], 4)
        # Create 3x4,3x5,4x4,5x3 RREF matrices
        dims = sample([
            (3, 4, choice([2,3])),
            (3, 5, choice([2,3])),
            (4, 4, choice([2,3])),
            (5, 3, 2)
        ], 4)
        for i in range(4):
            scenarios[i]["label"] = "ABCD"[i]
            scenarios[i]["matrix"] = CheckIt.simple_random_matrix_of_rank(
                dims[i][2], rows=dims[i][0], columns=dims[i][1]
            ).rref()
            if "add" in scenarios[i].keys():
                toprow = 0
                bottomrow = randrange(1, dims[i][2])
                scale = randrange(2,5)*choice([-1,1])
                E = elementary_matrix(dims[i][0], row1=toprow, row2=bottomrow, scale=scale)
                scenarios[i]["matrix"] = E*scenarios[i]["matrix"]
                scenarios[i]["rowop"] = f"R_{{ {toprow+1} }} + ({-scale}) R_{{ {bottomrow+1} }} \\to R_{{ {toprow+1} }}"
            elif "swap" in scenarios[i].keys():
                toprow = 0
                bottomrow = randrange(1, dims[i][2])
                E = elementary_matrix(dims[i][0], row1=toprow, row2=bottomrow)
                scenarios[i]["matrix"] = E*scenarios[i]["matrix"]
                scenarios[i]["rowop"] = f"R_{{ {toprow+1} }} \\leftrightarrow R_{{ {bottomrow+1} }}"
            elif "scale" in scenarios[i].keys():
                onlyrow = randrange(1, dims[i][2])
                scale = randrange(2,5)*choice([-1,1])
                E = elementary_matrix(dims[i][0], row1=onlyrow, scale=scale)
                scenarios[i]["matrix"] = E*scenarios[i]["matrix"]
                scenarios[i]["rowop"] = f"{latex(1/scale)} R_{{ {onlyrow+1} }} \\to R_{{ {onlyrow+1} }}"
            else:
                scenarios[i]["rowop"] = None

        A = CheckIt.simple_random_matrix_of_rank(2,rows=4,columns=4).rref()
        # add rows to other rows
        A = elementary_matrix(4, row1=2, row2=0, scale=randrange(1,4)*choice([-1,1]))*A
        A = elementary_matrix(4, row1=3, row2=0, scale=randrange(1,4)*choice([-1,1]))*A
        A = elementary_matrix(4, row1=2, row2=1, scale=randrange(1,4)*choice([-1,1]))*A
        A = elementary_matrix(4, row1=3, row2=1, scale=randrange(1,4)*choice([-1,1]))*A
        A = elementary_matrix(4, row1=0, row2=3, scale=randrange(1,4)*choice([-1,1]))*A
        A = elementary_matrix(4, row1=1, row2=2, scale=randrange(1,4)*choice([-1,1]))*A
        # swap two pairs of rows
        swaps = sample(range(4), 4)
        A = elementary_matrix(4, row1=swaps[0], row2=swaps[1])*A
        A = elementary_matrix(4, row1=swaps[2], row2=swaps[3])*A
        # scale a random row
        A = elementary_matrix(4, row1=randrange(4), scale=randrange(2,5)*choice([-1,1]))*A

        return {
            "A": A,
            "Arref": A.rref(),
            "scenarios": scenarios,
        }


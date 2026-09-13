load("../../../source/common/sagemath/library.sage")
TBIL.config_matrix_typesetting()

class Generator(BaseGenerator):
    def data(self):
        flip = choice([True,False])
        # surjection
        A=CheckIt.simple_random_matrix_of_rank(4,rows=4,columns=5)
        if flip:
            scenario = "columns"
        else:
            scenario = "kerimg"
        tasks = [{
            "surj": True,
            "value": True,
            scenario: True,
            "matrix": A,
            "rref": A.rref(),
        }]
        # non surjection
        A=CheckIt.simple_random_matrix_of_rank(choice([2,3]),rows=4,columns=5)
        if flip:
            scenario = "kerimg"
        else:
            scenario = "columns"
        tasks += [{
            "surj": True,
            "value": False,
            scenario: True,
            "matrix": A,
            "rref": A.rref(),
        }]


        flip = choice([True,False])
        # injection
        A=CheckIt.simple_random_matrix_of_rank(3,rows=4,columns=3)
        if flip:
            scenario = "columns"
        else:
            scenario = "kerimg"
        tasks += [{
            "inj": True,
            "value": True,
            scenario: True,
            "matrix": A,
            "rref": A.rref(),
        }]
        # non surjection
        A=CheckIt.simple_random_matrix_of_rank(2,rows=4,columns=3)
        if flip:
            scenario = "kerimg"
        else:
            scenario = "columns"
        tasks += [{
            "inj": True,
            "value": False,
            scenario: True,
            "matrix": A,
            "rref": A.rref(),
        }]

        shuffle(tasks)

        flip = choice([True, False])
        if flip:
            rank = 4
        else:
            rank = choice([2,3])
        A=CheckIt.simple_random_matrix_of_rank(rank,rows=4,columns=4)

        return {
            "tasks": tasks,
            "last_value": flip,
            "last_matrix": A,
            "last_rref": A.rref(),
        }

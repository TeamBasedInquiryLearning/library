class Generator(BaseGenerator):
    def data(self):        
        var1, var2 = sample([var('x'),var('y'),var('z')],2)

        a=choice([-1,1])*randrange(2,5)
        b=choice([-1,1])*randrange(2,5)
        c=choice([-1,1])*randrange(2,9)
        d=choice([-1,1])*randrange(2,6)
        f=choice([-1,1])*randrange(2,9)

        # ensure a*b-d != 0
        d = a*b + choice([-1,1])*randrange(2,6)

        LHS = b*var1+c
        RHS = d*var1+f

        solution = (f-a*c)/(a*b-d)

        aa=choice([-1,1])*randrange(2,5)
        bb=choice([-1,1])*randrange(2,5)
        cc=choice([-1,1])*randrange(2,9)
        ff=choice([-1,1])*randrange(2,9)

        # ensure aa*bb-dd != 0
        dd = aa*bb + choice([-1,1])*randrange(2,6)

        LHSineq = bb*var2+cc
        RHSineq = dd*var2+ff


        solution_ineq = (ff-aa*cc)/(aa*bb-dd)


        ineq=choice(['<','<=','>=','>'])
        if ineq=='<':
            if a*b-d>0:
                interval = f"(-\\infty, {solution_ineq})"
            if a*b-d<0:
                interval = f"({solution_ineq},\\infty)"
        if ineq=='<=':
            if a*b-d>0:
                interval = f"(-\\infty, {solution_ineq}]"
            if a*b-d<0:
                interval = f"[{solution_ineq},\\infty)"
        if ineq=='>':
            if a*b-d>0:
                interval = f"({solution_ineq},\\infty)"
            if a*b-d<0:
                interval = f"(-\\infty, {solution_ineq})"        
        if ineq=='>=':
            if a*b-d>0:
                interval = f"[{solution_ineq},\\infty)"
            if a*b-d<0:
                interval = f"(-\\infty, {solution_ineq}]"


        return {
            "a": a,
            "shuffle": choice([True,False]),
            "LHS": LHS,
            "RHS": RHS,
            "solution": solution,
            "variable": var1,
            "aa": a,
            "shuffleineq": choice([True,False]),
            "LHSineq": LHSineq,
            "RHSineq": RHSineq,
            "ineq": ineq,
            "solution2": solution_ineq,
            "interval": interval
        }

load("../sage/common.sage")

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

        ## ensure |ff-aa*cc| =< 15 (prevent big sols)
        ff = aa*cc + randrange(-15,16)

        # ensure |aa*bb-dd| >= 2 (prevent division by zero)
        dd = aa*bb + choice([-1,1])*randrange(2,6)

        LHSineq = bb*var2+cc
        RHSineq = dd*var2+ff


        solution_ineq = (ff-aa*cc)/(aa*bb-dd)


        ineq=choice(['<','<=','>=','>'])
        if ineq=='<':
            if aa*bb-dd>0:
                interval = f"(-\\infty, {solution_ineq})"
            if aa*bb-dd<0:
                interval = f"({solution_ineq},\\infty)"
        if ineq=='<=':
            if aa*bb-dd>0:
                interval = f"(-\\infty, {solution_ineq}]"
            if aa*bb-dd<0:
                interval = f"[{solution_ineq},\\infty)"
        if ineq=='>':
            if aa*bb-dd>0:
                interval = f"({solution_ineq},\\infty)"
            if aa*bb-dd<0:
                interval = f"(-\\infty, {solution_ineq})"        
        if ineq=='>=':
            if aa*bb-dd>0:
                interval = f"[{solution_ineq},\\infty)"
            if aa*bb-dd<0:
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
            "ineq": TBILPrecal.inequality_string(ineq),
            "solution2": solution_ineq,
            "interval": interval
        }

    @provide_data
    def graphics(data):
        P = arrow((0,0),(10,0),color="black", width=1, arrowsize=1, aspect_ratio=1)
        P += arrow((0,0),(-10,0),color="black", width=1, arrowsize=1)
        for i in range(-9,10):
            P += line([(i,-0.2),(i,0.2)],color="black")
            P += text(f"${i}$", (i,-0.6),color="black")
        if data["ineq"] in [">", ">="]:
            P += arrow((data["solution2"],0),(10,0),color="#0088ff", width=3, arrowsize=3)
        else:
            P += arrow((data["solution2"],0),(-10,0),color="#0088ff", width=3, arrowsize=3)
        P += text(f"${round(data['solution2'],ndigits=2)}$", (data["solution2"],0.6), color="black")
        if data["ineq"] == ">":
            P += text("(", (data['solution2'],0), color="#0088ff", fontsize=16)
        elif data["ineq"] == "<":
            P += text(")", (data['solution2'],0), color="#0088ff", fontsize=16)
        elif data["ineq"] == ">=":
            P += text("[", (data['solution2'],0), color="#0088ff", fontsize=16)
        elif data["ineq"] == "<=":
            P += text("]", (data['solution2'],0), color="#0088ff", fontsize=16)
        P.axes(False)
        return {
            "plot": plot(P)
        }

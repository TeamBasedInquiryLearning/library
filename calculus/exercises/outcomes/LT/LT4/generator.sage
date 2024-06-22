class Generator(BaseGenerator):
    def data(self):
    # Notes: This could definitely be improved! I (Reeve) coded this initially as 1 piecewise function for both parts, so some of the code if extremely convoluted in order to make that work. Things could definitely be improved to make numbers "nicer" for students.
        x = var('x')
        b = var('b')
        f="f"
        g="g"
        h="h"

        # Function Names
        functionnames=[f,g,h]
        shuffle(functionnames)

        # Parameterize Me!
        # Choose domain split for param piecewise function
        param_domainsplitlist = list(range(-3,0)) + list(range(1,6))
        param_x = choice(param_domainsplitlist)
        param_y = randint(-3,6)

        # Param Piece 1
        param_f1choice = choice(["linear","quadratic","rational"])
        # Force a choice by uncommenting the line below and defining f1choice
        #f1choice="rational"
        if param_f1choice == "linear":
            param_f1(x) = choice([b*x+choice([-1,1])*QQ(randint(1,12)/randint(1,5)),choice([-1,1])*QQ(randint(1,12)/randint(1,5))*x+b])
            parameter = solve(param_f1(x=param_x)-param_y,b)[0].rhs() # solve for b
        elif param_f1choice == "quadratic":
            quadcoeffs = [b,choice([-1,1])*randint(1,5),choice([-1,1])*QQ(randint(1,12)/randint(1,3))]
            shuffle(quadcoeffs)
            param_f1(x) = quadcoeffs[0]*x^2 + quadcoeffs[1]*x + quadcoeffs[2]
            parameter = solve(param_f1(x=param_x)-param_y,b)[0].rhs() # solve for b
        elif param_f1choice == "rational":
            # Determine 1 or 2 roots not equal to param_x for the denominator
            param_f1denrootlist = [n for n in range(param_x-5,param_x+6) if n!=param_x]
            param_f1denroot1 = choice(param_f1denrootlist)
            param_f1denroot2 = choice(param_f1denrootlist)
            param_f1den = x - param_f1denroot1
            dendegree = 1
            for i in range(0,randint(0,1)):
                param_f1den *= x - param_f1denroot2
                dendegree += 1
            # Determine 1 or 2 nonzero roots close to but not equal to param_x for the numerator (this might reduce to a linear function which you can avoid if you like...)
            # Note: param_x can't be zero or a root of the numerator if you want to be able to reliably solve for b
            param_f1numrootlist = [n for n in range(param_x-5,param_x+6) if n!=0 and n!=param_x]
            # If you want a rational function for sure, uncomment the the 2 lines below
            #param_f1numrootlist = [n for n in range(param_x-5,param_x+5) if n!=0 and n!=param_x and n!=param_f1denroot1 and n!=param_f1denroot2]
            #shuffle(param_f1numrootlist)
            param_f1numroot1 = choice(param_f1numrootlist)
            param_f1numroot2 = choice(param_f1numrootlist)
            param_f1num = choice([b*x - param_f1numroot1,x - param_f1numroot1*b])
            if dendegree < 2:
                param_f1num *= x - param_f1numroot2
            param_f1(x) = param_f1num.expand()/param_f1den.expand()
            parameter = solve(param_f1(x=param_x)-param_y,b)[0].rhs() # solve for b

        # Param piece 2 will connect to (param_x,param_y)
        # choose f2 based on complexity of f1
        if param_f1choice == "linear":
            param_f2choice = "quadratic"
        elif param_f1choice == "rational":
            param_f2choice = "linear"
        else:
            param_f2choice = choice(["linear","quadratic"])
        # Force a choice by uncommenting the line below and defining f2choice
        #param_f2choice = "quadratic"
        param_slope = choice([-1,1])*QQ(randint(1,5)/randint(1,2))
        param_line = param_slope*(x-param_x) + param_y
        if param_f2choice == "linear":
            param_f2 = param_line.full_simplify()
        elif param_f2choice == "quadratic":
            param_x2 = param_x + randint(-5,6)
            param_f2 = (choice([-1,1])*(x-param_x)*(x-param_x2) + param_line).full_simplify()

        # Choose inequalities for where param_f1 meets param_f2.
        param_f1ineq = choice(["<","\\leq"])
        if param_f1ineq == "<":
            param_f2ineq = "\\geq"
        else:
            param_f2ineq = ">"

        parametervars = [
            {
                "fn":functionnames[0],
                "x":param_x,
                # Note: because f1 contains 2 variables (x and b), we need to explicitly state f1 is a function of x, otherwise this will be displayed in a strange way
                "f1":param_f1(x),
                "f2":param_f2,
                "f1ineq":param_f1ineq,
                "f2ineq":param_f2ineq,
                "parameter":parameter,
            }
        ]

        nums = list(range(2,10))+list(range(-9,-1))
        shuffle(nums)
        m1,m3,a,match,diff = nums[:5]
        distype = choice(["jump","removable"])
        if distype == "jump":
            if choice([True,False]):
                #value matches left limit
                f1 = m1*(x-a)+match
                f2 = match
                f3 = m3*(x-a)+diff
            else:
                #value matches right limit
                f1 = m1*(x-a)+diff
                f2 = match
                f3 = m3*(x-a)+match
        else:
            #limits match each other but not value
            f1 = m1*(x-a)+match
            f2 = diff
            f3 = m3*(x-a)+match

        discontinuityvars = [
            {
                "discontinuity": True,
                "fn":functionnames[1],
                "a":a,
                "f1":f1,
                "f2":f2,
                "f3":f3,
                distype: True,
            }
        ]

        tasks = parametervars+discontinuityvars
        shuffle(tasks)

        return {
            "tasks": tasks,
        }
#Functions to display powers of trig functions
def print_cosp(self,*args): return f"\\cos ^{args[1]}({latex(args[0])})"
cosp = function("cosp",nargs=2,print_latex_func=print_cosp)
def print_sinp(self,*args): return f"\\sin ^{args[1]}({latex(args[0])})"
sinp = function("sinp",nargs=2,print_latex_func=print_sinp)

class Generator(BaseGenerator):

    def data(self):
        # integral with odd power
        x=var("x")
        
        even=2*randint(1,6)
        
        odd=choice([5,7])

        z = var("z")
        if odd==5:
            hint = "hint_2"
        else:
            hint = "hint_3"
        
        trigs=[sin, cos]
        shuffle(trigs)
        
        f=randint(1,5)*(trigs[0](x))^even*(trigs[1](x))^odd
        
        F=f.integral(x)

        # integral with even powers

        a = randrange(2,6)
        m = randrange(2,5)
        n = randrange(2,5)
        k = 2^randrange(2,5)
        g = k*cosp(a*x,2*m)*sinp(a*x,2*n)
        also_g = k/2^(m+n)*(1+cos(2*a*x))^m*(1-cos(2*a*x))^n
        

        return {
            "f": f,
            "F": F,
            "g": g,
            "also_g": also_g,
            hint: True,
        }

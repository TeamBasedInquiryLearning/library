#Functions to display powers of trig functions
def print_cosp(self,*args): return f"\\cos ^{{{args[1]}}}({latex(args[0])})"
def deriv_cosp(self,*args,**kwds): 
    if args[1]==1:
        return -1*sinp(args[0],1)*args[0].derivative(args[kwds['diff_param']])
    else:
        return args[1]*-1*cosp(args[0],args[1]-1)*sinp(args[0],1)*args[0].derivative(args[kwds['diff_param']])

cosp = function("cosp",nargs=2,print_latex_func=print_cosp,derivative_func=deriv_cosp)
def print_sinp(self,*args): return f"\\sin ^{{{args[1]}}}({latex(args[0])})"
def deriv_sinp(self,*args,**kwds): 
    if args[1]==1:
        return cosp(args[0],1)*args[0].derivative(args[kwds['diff_param']])
    else:
        return args[1]*sinp(args[0],args[1]-1)*cosp(args[0],1)*args[0].derivative(args[kwds['diff_param']])

sinp = function("sinp",nargs=2,print_latex_func=print_sinp, derivative_func=deriv_sinp)

class Generator(BaseGenerator):

    def data(self):
        # Task 1, integral with odd power
        x=var("x")
        
        n=randint(1,6)
        m=randint(2,3)

        k=var('k')
        z=var('z')
        hint=f"(1-z)^{m}={latex(sum(binomial(m,k)*(-z)^k,k,0,m))}"
        
        
        trigs=[sinp, cosp]
        shuffle(trigs)
        
        a = randint(1,6)
        f = a*trigs[0](x,2*n)*trigs[1](x,2*m+1)
        F = sum(a*binomial(m,k)*(-1)^k*1/(2*n+2*k+1)*trigs[0](x,2*n+2*k+1)*trigs[0](x,1).derivative(x)/trigs[1](x,1),k,0,m)


        # Task 2, integral with even powers

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
            "hint": hint,
        }

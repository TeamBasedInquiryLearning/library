load("../../../source/common/sagemath/library.sage")

class Generator(BaseGenerator):

    def data(self):
        # Task 1, integral with odd power
        x=var("x")
        
        n=randint(1,6)
        m=randint(2,3)

        k=var('k')
        z=var('z')
        hint=f"(1-z)^{m}={latex(sum(binomial(m,k)*(-z)^k,k,0,m))}"
        
        
        trigs=[TBIL.sinp, TBIL.cosp]
        shuffle(trigs)
        
        a = randint(1,6)
        f = a*trigs[0](x,2*n)*trigs[1](x,2*m+1)
        F = sum(a*binomial(m,k)*(-1)^k*1/(2*n+2*k+1)*trigs[0](x,2*n+2*k+1)*trigs[0](x,1).derivative(x)/trigs[1](x,1),k,0,m)


        # Task 2, integral with even powers

        a = randrange(2,6)
        m = randrange(2,5)
        n = randrange(2,5)
        k = 2^randrange(2,5)
        g = k*TBIL.cosp(a*x,2*m)*TBIL.sinp(a*x,2*n)
        also_g = k/2^(m+n)*(1+cos(2*a*x))^m*(1-cos(2*a*x))^n
        

        return {
            "f": f,
            "F": F,
            "g": g,
            "also_g": also_g,
            "hint": hint,
        }

class Generator(BaseGenerator):
    def data(self):
        
        x=var("x")
        n=var("n")
        
        funct=choice(['sin', 'cos', 'exp', 'oneover'])
        
        a=Integer(randint(1,5)*choice([-1,1]))
        k=Integer(randint(2,5))
        m=Integer(randint(1,5))
        c=Integer(randint(1,5)*choice([-1,1]))
        
        if funct=='sin':
            # base power series
            f=sin(x)
            seq=(-1)^n*x^(2*n+1)/factorial(2*n+1)
            # composition with ax^k
            f_comp = sin(a*x^k)
            seq_comp =(-1)^n*(a*x^k)^(2*n+1)/factorial(2*n+1)
            if a > 0:
                seq_comp_simp = ((-1)^n).mul(abs(a)^(2*n+1),hold=True)*x^(2*n*k+k)/factorial(2*n+1)
            else:
                seq_comp_simp = ((-1)^(n+1)).mul(abs(a)^(2*n+1),hold=True)*x^(2*n*k+k)/factorial(2*n+1)
            # product with x^m
            f_prod=x^m*sin(x)
            seq_prod=(-1)^n*x^(2*n+1+m)/factorial(2*n+1)
            # derivative
            seq_diff=((-1)^n)*(2*n+1)*x^(2*n)/factorial(2*n+1)
            seq_diff_simp=(-1)^n*x^(2*n)/factorial(2*n)
            # anti-derivative
            seq_int=(-1)^(n)*x^(2*n+2)/factorial(2*n+1)/(2*n+2)
            seq_int_simp=(-1)^(n+1)*x^(2*n)/factorial(2*n)
            
        if funct=='cos':
            # base power series
            f=cos(x)
            seq=(-1)^n*x^(2*n)/factorial(2*n)
            # composition with ax^k
            f_comp = cos(a*x^k)
            seq_comp =(-1)^n*(a*x^k)^(2*n)/factorial(2*n)
            seq_comp_simp = (-a^2)^n*x^(2*n*k)/factorial(2*n)
            # product with x^m
            f_prod=x^m*cos(x)
            seq_prod=(-1)^n*x^(2*n+m)/factorial(2*n)
            # derivative
            seq_diff=((-1)^n)*(2*n)*x^(2*n-1)/factorial(2*n)
            seq_diff_simp=(-1)^(n+1)*x^(2*n+1)/factorial(2*n+1)
            # anti-derivative
            seq_int=(-1)^(n)*x^(2*n+1)/factorial(2*n)/(2*n+1)
            seq_int_simp=(-1)^(n)*x^(2*n+1)/factorial(2*n+1)
        
        if funct=='exp':
            # base power series
            f=exp(x)
            seq=x^(n)/factorial(n)
            # composition with ax^k
            f_comp = exp(a*x^k)
            seq_comp =(a*x^k)^(n)/factorial(n)
            seq_comp_simp = a^(n)*x^(n*k)/factorial(n)
            # product with x^m
            f_prod=x^m*exp(x)
            seq_prod=x^(n+m)/factorial(n)
            # derivative
            seq_diff=n*x^(n-1)/factorial(n)
            seq_diff_simp=x^(n)/factorial(n)
            # anti-derivative
            seq_int=x^(n+1)/factorial(n)/(n+1)
            seq_int_simp=x^n/factorial(n)
            
        if funct=='oneover':
            # base power series
            f=(1-x).power(-1,hold=True)
            seq=x^(n)
            # composition with ax^k
            f_comp = (1-a*x^k).power(-1,hold=True)
            seq_comp =(a*x^k)^(n)
            seq_comp_simp =(a)^n*x^(n*k)
            # product with x^m
            f_prod=x^m*f
            seq_prod=x^(n+m)
            # derivative
            seq_diff=n*x^(n-1)
            seq_diff_simp=(n+1)*x^(n)
            # anti-derivative
            seq_int=x^(n+1)/(n+1)
            seq_int_simp=x^n/n
            
        
        
        
        prob=choice(['int', 'diff'])
        
        
        
        
        

        return {
            "f": f,
            "f_comp": f_comp,
            "f_prod": f_prod,
            "seq": seq,
            "seq_comp": seq_comp,
            "seq_comp_simp": seq_comp_simp,
            "seq_prod": seq_prod,
            "seq_diff": seq_diff,
            "seq_diff_simp": seq_diff_simp,
            "seq_int": seq_int,
            "seq_int_simp": seq_int_simp,
            "c":c,  
            prob:True,  
        }

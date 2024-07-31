import random
class Generator(BaseGenerator):
    def data(self):
        x=var("x")
        y=var("y")
        from sage.symbolic.integration.integral import definite_integral

        
        
        
        scenario=randint(0,3)
        
        if scenario==0:
            m=randint(1,6)/2
            c=randint(0,3)
            f(x)=m*x+c
            g(y)=1/m*(y-c)
            
        if scenario==1:
            m=randint(1,6)/2
            c=randint(0,3)
            f(x)=m*x^2+c
            g(y)=sqrt(1/m*(y-c))
            
        if scenario==2:
            m=randint(1,6)
            c=randint(0,3)
            f(x)=m*e^x+c
            g(y)=log(1/m*(y-c))
            
        #This may effectively duplicate scenario 1 after this refactor, but with uglier endpoints sometimes
        if scenario==3:
            m=randint(1,6)
            c=randint(0,3)
            f(x)=sqrt(m*x+c)
            g(y)=1/m*(y^2-c)
        
        fp(x)=diff(f(x),x)
        gp(y)=diff(g(y),y)
        
        givenfx=choice([True,False])
        givengy= not givenfx

        if givenfx:
            a=randint(0,3)
            b=a+randint(1,4)
            aa=f(a)
            bb=f(b)
        
        if givengy:
            aa=randint(0,3)
            bb=aa+randint(1,4)
            a=g(aa)
            b=g(bb)


        return {
            "f": f(x),
            "fp": fp(x),
            "a": a,
            "b": b,  
            "g": g(y),
            "gp": gp(y),
            "aa": aa,
            "bb": bb,
            "givenfx": givenfx,
            "givengy": givengy,
        }


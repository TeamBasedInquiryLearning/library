class Generator(BaseGenerator):
    def data(self):
        x=var("x")
        from sage.symbolic.integration.integral import definite_integral

        f(x)=0
        
        while f(x)==0:
            functions=[
                sqrt(randint(1,5)*x+randint(1,5)),
                randint(1,5)*e^(randint(1,5)*choice([-1,1])*x)+randint(-5,5),
                randint(1,5)*choice([-1,1])*x^randint(1,5)+randint(1,5)*choice([-1,1])*x^randint(1,5)
            ]
            f(x)=choice(functions)
        
        fp(x)=diff(f(x),x)
        
        n=randint(4,5)
        a=randint(0,3)
        b=a+randint(1,4)
        DX=(b-a)/n
        

        xi=a
        estlength=0
        
        XIlist=[]
        XIp1list=[]
        FXIlist=[]
        FXIp1list=[]
        
        Lengthlist=[]
        
        for i in range(n):
            XIlist.append(xi)
            XIp1list.append(round(xi+DX,4))
            FXIlist.append(round(f(xi), 4))
            FXIp1list.append(round(f(xi+DX), 4))
            Lengthlist.append(round(sqrt(DX^2+(f(xi+DX)-f(xi))^2), 4))
            estlength=estlength+round(sqrt(DX^2+(f(xi+DX)-f(xi))^2),4)
            xi=round(xi+DX,4)
        
                            
        Datalist=[]
            
        for i in range(n):
            entry={
                'xi':XIlist[i],
                'xip1':XIp1list[i],
                'fxi':FXIlist[i],
                'fxip1':FXIp1list[i],
                'length':Lengthlist[i],        
            }
            Datalist.append(entry)                     
        
                            
                            
        

        return {
            "f": f(x),
            "fp": fp(x),
            "a": a,
            "b": b,  
            "DX": DX,
            "estlength": estlength,
            "n": n,
            "Datalist": Datalist,          
        }

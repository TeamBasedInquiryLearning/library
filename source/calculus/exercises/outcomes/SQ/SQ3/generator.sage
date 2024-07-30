class Generator(BaseGenerator):
    def data(self):
        n=var("n")
        i=var("i")

        #Geometric
        rtemp=1
        while rtemp==1:
            rtemp=1/randint(1,6)*randint(1,6)
        
        r=rtemp*choice([-1,1])
        k=randint(1,3)*choice([-1,1])
        Geo(n)=k*r^n
        GeoPS(n)=k*(1-r^(n+1))/(1-r)
        
        if abs(r)>1:
            Converge1=False
            Limit1=False
        if abs(r)<1:
            Converge1=True
            Limit1=k*(1)/(1-r)
            
        
        
        #telescope
        a=randint(2,5)
        b=randint(2,5)
        f(n)=1/(a*n+b)
        #Tele(n)=f(n)-f(n+1)
        #TelePS(n)=f(1)-f(n+1)
        
        Converge2=True
        Limit2=f(1)
        
        Problem1={
            "Limit":Limit1,
            "Converge":Converge1,
        }
        
        Problem2={
            "Limit":Limit2,
            "Converge":Converge2,
        }

        return {
            
            "s0": k,
            "s1": k*r,
            "s2": k*r^2,
            "k": k,
            "r": r,
            "fi": f(i),
            "fi1": f(i+1),
            "f1": f(1),
            "fn1": f(n+1),
            "geo_closed": GeoPS(n),
            "Problem1": Problem1,
            "Problem2": Problem2,
        }

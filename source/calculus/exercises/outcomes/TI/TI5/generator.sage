class Generator(BaseGenerator):
    def data(self):
        x = var("x")

        # define possible factors
        
        scenario=randint(0,10)
        
        pm = choice([-1,1])
        primes = [2,3,5,7]
        a,k = sample(primes,2)
        du=k
        u=k*x
        
        if scenario==0:
            f=du/(a^2+u^2)
            F=arctan(u/a)
        if scenario==1:
            f=du/sqrt(u^2+pm*a^2)
            F=ln(abs(u+sqrt(u^2+pm*a^2)))
        if scenario==2:
            f=du*sqrt(u^2+pm*a^2)     
            F=u/2*sqrt(u^2+pm*a^2)+pm*a^2/2*ln(abs(u+sqrt(u^2+pm*a^2)))
        if scenario==3:
            f=du*u^2/sqrt(u^2+pm*a^2)
            F=u/2*sqrt(u^2+pm*a^2)-pm*a^2/2*ln(abs(u+sqrt(u^2+pm*a^2)))     
        if scenario==4:
            f=du/(u*sqrt(u^2+a^2))
            F=-1/a*ln(abs((a+sqrt(u^2+a^2))/u))     
        if scenario==5:
            f=du/(u*sqrt(u^2-a^2))
            F=1/a*arcsec(u/a)    
        if scenario==6:
            f=du/sqrt(a^2-u^2)
            F=arcsin(u/a)     
        if scenario==7:
            f=du*sqrt(a^2-u^2)
            F=u/2*sqrt(a^2-u^2)+a^2/2*arcsin(u/a)
        if scenario==8:
            f=du*u^2/sqrt(a^2-u^2)
            F=-u/2*sqrt(a^2-u^2)+a^2/2*arcsin(u/a)    
        if scenario==9:
            f=du/(u*sqrt(a^2-u^2))
            F=-1/a*ln(abs((a+sqrt(a^2-u^2))/u))    
        if scenario==10:
            f=du/(u^2*sqrt(a^2-u^2))
            F=-sqrt(a^2-u^2)/(a^2*u)
        
        # bit more randomness...
        c=randint(2,5)*choice([-1,1])
        
        return {
            "f": c*f,
            "F": c*F,
            "stuff": [u,du,a,k,pm,c],
        }

class Generator(BaseGenerator):
    def data(self):
        n=var("n")
        
        #Converge
        
        power=randint(1,3)
        num=randint(1,5)*n^power
        for i in range(power):
            num=num+choice([0,0,randint(0,5)])*n^i
        powerd=randint(power+2, power+4)
        denomp=randint(1,5)*n^powerd
        for i in range(powerd):
            denomp=denomp+choice([0,0,randint(0,5)])*n^i
        denom=choice([randint(1,5)*randint(2,5)^n, denomp])    
        Sequence1=num/denom*(-1)^(n+randint(0,1))
        Converge1=True
        
        
        
        Series1={
            "Sequence":Sequence1,
            "Converge":Converge1,
        }
        
        power=randint(1,3)
        num=randint(1,5)*n^power
        for i in range(power):
            num=num+choice([0,0,randint(0,5)])*n^i
        powerd=power+1
        denomp=randint(1,5)*n^powerd
        for i in range(powerd):
            denomp=denomp+choice([0,0,randint(0,5)])*n^i
        denom=denomp   
        Sequence2=num/denom*(-1)^(n+randint(0,1))
        Converge2=False
        
        
        
        Series2={
            "Sequence":Sequence2,
            "Converge":Converge2,
        }
        
        
        
        
        
        
        
        Problems=[Series1, Series2]
        shuffle(Problems)

        return {
            "Problems": Problems,
        }

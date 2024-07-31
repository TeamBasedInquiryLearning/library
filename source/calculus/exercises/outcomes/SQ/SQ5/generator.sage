class Generator(BaseGenerator):
    def data(self):
        n=var("n")
        
        
        power=randint(2,5)
        num=randint(1,5)*n^power
        denom=randint(1,5)*n^power
        for i in range(power):
            num=num+choice([0,0,randint(0,5)])*n^i
            denom=denom+choice([0,0,randint(0,5)])*n^i
        Sequence1=num/denom
        Converge1=False
        Test1="Divergence"
        
        
        
        Series1={
            "Sequence":Sequence1,
            "Converge":Converge1,
            "Test":Test1,
        }
        
        power=randint(1,5)
        case=randint(0,1)
        
        if case==0:
            power=1/power
        Converge2=False
        Test2="Integral"
        if power > 1:
            Converge2=True
        Sequence2=1/n^power    
        
        
        
        Series2={
            "Sequence":Sequence2,
            "Converge":Converge2,
            "Test":Test2,
        }
        
        
        power=randint(2,4)
        num=randint(1,5)*n^power
        for i in range(power):
            num=num+choice([0,0,randint(0,5)])*n^i
        denom=randint(1,5)*n^(power+1)
        for i in range(power+1):
            denom=denom+choice([0,0,randint(0,5)])*n^i
        Sequence3=(-1)^(n+randint(0,1))*num/denom
        Converge3=True
        Test3="Alternating Summation"
        
        
        Series3={
            "Sequence":Sequence3,
            "Converge":Converge3,
            "Test":Test3,
        }
        
        
        
        
        
        
        
        
        Problems=[Series1, Series2, Series3]
        shuffle(Problems)

        return {
            "Problems": Problems,
        }

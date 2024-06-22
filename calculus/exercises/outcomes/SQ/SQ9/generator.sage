class Generator(BaseGenerator):
    def data(self):
        n=var("n")
        
        #Converge1
        power=randint(1,3)
        num=randint(1,5)*n^power
        for i in range(power):
            num=num+choice([0,0,randint(0,5)])*n^i
        powerd=randint(power+2, power+4)
        denomp=randint(1,5)*n^powerd
        for i in range(powerd):
            denomp=denomp+choice([0,0,randint(0,5)])*n^i
        denom=choice([randint(1,5)*randint(2,5)^n, denomp])    
        Sequence1=num/denom*(-1)^(n*randint(0,1))
        Converge1=True
        
        
        
        Converge1={
            "Sequence":Sequence1,
            "Converge":Converge1,
        }
        
        
        #Converge2
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
        Converge2=True
        
        
        
        Converge2={
            "Sequence":Sequence2,
            "Converge":Converge2,
        }
        
        
        #Converge3
        num=Integer(randint(1,5))
        denom=Integer(randint(num+1, num+5))
        coeff=randint(1,5)
        ratio=num/denom    
        Sequence3=coeff*ratio^n
        Converge3=True
        
        
        
        Converge3={
            "Sequence":Sequence3,
            "Converge":Converge3,
        }
        
        
        
        #Converge4
        power=randint(1,3)
        num=randint(1,5)*n^power
        for i in range(power):
            num=num+choice([0,0,randint(0,5)])*n^i
        
        Sequence4=num/randint(2,5)^n*(-1)^(n*randint(0,1))
        Converge4=True
        
        
        
        Converge4={
            "Sequence":Sequence4,
            "Converge":Converge4,
        }
        
        
        #Converge5
        
        num=choice([n^randint(1,5)+randint(0,5), randint(1,5)*randint(2,5)^n+randint(0,5), randint(1,5)*randint(2,5)^n*n^randint(1,5)])
        Sequence5=num/factorial(n)
        
        Converge5={
            "Sequence":Sequence5,
            "Converge":True,
        }
        
        #Converge 6
        
        num=choice([n^randint(1,5)+randint(0,5), randint(1,5)*randint(2,5)^n+randint(0,5), randint(1,5)*randint(2,5)^n*n^randint(1,5), randint(2,5)^n*factorial(n), n^randint(2,5)*factorial(n)])
        Sequence6=num/(n^n)
        
        Converge6={
            "Sequence":Sequence6,
            "Converge":True,
        }
        
        
        
        #Diverge1
        power=randint(1,3)
        num=randint(1,5)*n^power
        for i in range(power):
            num=num+choice([0,0,randint(0,5)])*n^i
        powerd=power+1
        denomp=randint(1,5)*n^powerd
        for i in range(powerd):
            denomp=denomp+choice([0,0,randint(0,5)])*n^i
        denom=denomp  
        Sequence7=num/denom
        Converge7=False
        
        
        
        Diverge1={
            "Sequence":Sequence7,
            "Converge":Converge7,
        }
        
        
        
        #Diverge2
        power=randint(1,3)
        num=randint(1,5)*n^power
        for i in range(power):
            num=num+choice([0,0,randint(0,5)])*n^i
        
        Sequence8=randint(2,5)^n*(-1)^(n*randint(0,1))/num
        Converge8=False
        
        
        
        Diverge2={
            "Sequence":Sequence8,
            "Converge":Converge8,
        }
        
        
        #Diverge3
        
        num=choice([n^randint(1,5)+randint(0,5), randint(1,5)*randint(2,5)^n+randint(0,5), randint(1,5)*randint(2,5)^n*n^randint(1,5)])
        Sequence9=factorial(n)/num
        
        Diverge3={
            "Sequence":Sequence9,
            "Converge":False,
        }
        
        #Diverge4
        
        num=choice([n^randint(1,5)+randint(0,5), randint(1,5)*randint(2,5)^n+randint(0,5), randint(1,5)*randint(2,5)^n*n^randint(1,5), randint(2,5)^n*factorial(n), n^randint(2,5)*factorial(n)])
        Sequence10=(n^n)/n
        
        Diverge4={
            "Sequence":Sequence10,
            "Converge":False,
        }
        
        
        
        
        
        
        Convergent=choice([Converge1, Converge2, Converge3, Converge4, Converge5, Converge6])
        
        Divergent=choice([Diverge1, Diverge2, Diverge3, Diverge4])
        
        
        
        Problems=[Convergent, Divergent]
        shuffle(Problems)

        return {
            "Problems": Problems,
        }

class Generator(BaseGenerator):
    def data(self):
        # FIXME very slow!
        n=var("n")
        
        RL=1
        
        
        PossibleSequences=[
            (n^randint(1,2)+randint(1,5))/randint(2,5)^n,
            (n^randint(1,2)+randint(1,5))/factorial(n),
            (n^randint(1,2)+randint(1,5))/n^n,
            (randint(2,5)^n)/factorial(n),
            (randint(2,5)^n)/n^n,
            randint(1,5)*factorial(n)/n^n,
            factorial(n)/(randint(2,5)^n),
            n^n/(randint(2,5)^n),
            n^n/(randint(1,5)*factorial(n)),
            randint(2,5)^n/(n^randint(1,2)+randint(1,5)),
            factorial(n)/(n^randint(1,2)+randint(1,5)),
            n^n/(n^randint(1,2)+randint(1,5)),
            
        ]
        
        
        #Nterms=[randint(1,5)*n^2, randint(1,5)*randint(2,5)^n, randint(1,5)*(randint(2,5)^n)*(n^(randint(1,3))), randint(1,5)*factorial(n), randint(1,5)*factorial(n)*randint(2,5)^n, randint(1,5)*factorial(n)*n^(randint(1,3)) , randint(1,5)*(n^n), randint(1,5)*(n^n)*factorial(n), randint(1,5)*(n^n)*randint(2,5)^n, randint(1,5)*(n^n)*n^(randint(1,3))]
        
        #Dterms=[randint(1,5)*(randint(2,5)^n)*(n^(randint(1,3))), randint(1,5)*factorial(n), randint(1,5)*factorial(n)*randint(2,5)^n, randint(1,5)*factorial(n)*n^(randint(1,3)) , randint(1,5)*(n^n), randint(1,5)*(n^n)*factorial(n), randint(1,5)*(n^n)*randint(2,5)^n, randint(1,5)*(n^n)*n^(randint(1,3))]
        
        lim=1
        
        while (RL==1):
            #shuffle(Nterms)
            #shuffle(Dterms)
            #num=Nterms[0]
            #denom=Dterms[0]
            #Sequence(n)=num/denom
            shuffle(PossibleSequences)
            Sequence(n)=PossibleSequences[0]
            Ratio=Sequence(n+1)/Sequence(n)
            Seq=Sequence(n)
            lim=Seq.limit(n=oo)
            RL=Ratio.limit(n=oo)
        
        Converge=False
        
        if abs(Ratio.limit(n=oo))<1:
            Converge=True
        
        return {
            "Sequence":Seq,
            "Converge":Converge,
        }

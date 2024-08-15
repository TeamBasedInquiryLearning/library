class Generator(BaseGenerator):
    def data(self):
        n=var("n")
    
        sequences=[
            [randint(1,3)/(log(n)+randint(0,4)), False, randint(2,5)],
            [randint(1,3)/(randint(1,3)*n+randint(0,4)), False, randint(2,5)],
            [randint(1,3)/(randint(1,3)*n^2+randint(0,4)*n+randint(0,4)), True, randint(2,5)],
            [randint(1,3)/(randint(2,5)^n+randint(0,4)), True, randint(2,5)],
        ]
        
        shuffle(sequences)
        
        Thing1=sequences[0]
        Thing2=sequences[1]
        
        Problem1={
            "Seq":Thing1[0],
            "Converge":Thing1[1],
            "k":Thing1[2],
        }
        
        Problem2={
            "Seq":Thing2[0],
            "Converge":Thing2[1],
            "k":Thing2[2],
        }

        return {
            "Problem1": Problem1,
            "Problem2": Problem2,  
        }

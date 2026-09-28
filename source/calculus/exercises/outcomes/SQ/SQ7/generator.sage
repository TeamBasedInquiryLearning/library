class Generator(BaseGenerator):
    def data(self):
        n = var("n")
        i,j = sample(range(4),2)
        terms = [
            n^choice([1,2])+randrange(1,6),  # polynomial
            randrange(2,6)^n,  # exponential
            factorial(n),  # factorial
            n^n  # tetration
        ]
        
        return {
            "sequence": terms[i]/terms[j],
            "converge": i < j,
        }

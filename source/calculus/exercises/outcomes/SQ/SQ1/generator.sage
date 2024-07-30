class Generator(BaseGenerator):
    def data(self):
        n=var("n")
        a_n = var("a_n")
        
        def random_arithmetic():
            a_0 = randrange(1,6)*choice([-1,1])
            k = randrange(2,6)*choice([-1,1])
            closed = a_0 + k*n
            recursive = a_n + k
            return {
                "closed": closed,
                "recursive": recursive,
            }
        
        def random_geometric():
            a_0 = randrange(1,6)*choice([-1,1])
            k = randrange(2,5)*choice([-1,1])
            closed = a_0*k^n
            recursive = a_n*k
            return {
                "closed": closed,
                "recursive": recursive,
            }
        
        closed_start,recursive_start = sample(range(2),2)
        closed,recursive = sample([random_arithmetic(),random_geometric()],2)

        find_terms = {
            "closed": closed["closed"],
            "closed_start": closed_start,
            "closed_terms": [{"term": closed["closed"](n=k)} for k in range(closed_start,closed_start+5)],
            "recursive": recursive["recursive"],
            "recursive_start": recursive_start,
            "recursive_first": recursive["closed"](n=recursive_start),
            "recursive_terms": [{"term": recursive["closed"](n=k)} for k in range(recursive_start,recursive_start+5)],
        }
        
        closed_start,recursive_start = sample(range(2),2)
        closed,recursive = sample([random_arithmetic(),random_geometric()],2)

        find_formulas = {
            "closed": closed["closed"],
            "closed_start": closed_start,
            "closed_terms": [{"term": closed["closed"](n=k)} for k in range(closed_start,closed_start+5)],
            "recursive": recursive["recursive"],
            "recursive_start": recursive_start,
            "recursive_first": recursive["closed"](n=recursive_start),
            "recursive_terms": [{"term": recursive["closed"](n=k)} for k in range(recursive_start,recursive_start+5)],
        }

        return {
            "terms": find_terms,
            "formulas": find_formulas,
        }
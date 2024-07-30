class Generator(BaseGenerator):
    
    def data(self):
        
        
        def poly_with_zeros(zeros, x=var("x"), mults=None, vrange=None):
            """
            Returns a polynomial with the specified zeros and mulitiplicies
            (defaults to multiplicity 1 for all zeros).
            If a vrange is provided, points on the polynomial between the given zeros
            are within this distance of zero (for a prettier graph, but a messier
            polynomial).
            """
            if mults is None:
                mults = [1 for _ in zeros]
            poly = prod((x-zero)^mults[i] for i,zero in enumerate(zeros))
            if vrange is None:
                return poly
            auto_vrange = 0
            sorted_zeros = list(zeros)
            sorted_zeros.sort()
            for i in range(len(sorted_zeros)-1):
                if abs(poly.find_local_minimum(sorted_zeros[i],sorted_zeros[i+1])[0]) > auto_vrange:
                    auto_vrange = abs(poly.find_local_minimum(sorted_zeros[i],sorted_zeros[i+1])[0])
                if abs(poly.find_local_maximum(sorted_zeros[i],sorted_zeros[i+1])[0]) > auto_vrange:
                    auto_vrange = abs(poly.find_local_maximum(sorted_zeros[i],sorted_zeros[i+1])[0])
            return poly/auto_vrange*vrange
        
        var('x y')
        
        
        scenario = "precal" #choice(["precal", "CA"])
        
        if scenario == "precal":
            name1 = choice(["zeroes", "roots"])
            name2 = choice(["zeroes", "roots"])
            a = randrange(0,2)*choice([-1,1])
            b = randrange(1,3)*choice([-1,1])
            R = [-3,-2,-1,0,1,2,3]
            shuffle(R)
            r1 = R[0]
            r2 = R[1]
            r3 = a+b*I
            r4 = a-b*I
            f(x)= expand((x-r1)*(x-r2)*(x-r3)*(x-r4))
            
            s1 = randrange(1,6)
            s2 = randrange(1,6)*(-1)
            k = randrange(2,6)
            s3 = ((randrange(1,6)*k+randrange(1,k))*choice([-1,1]))/k
            m1 = randrange(1,6)
            m2 = randrange(1,6)
            m3 = randrange(1,6)
            g(x) = k^m3*(x-s1)^m1*(x-s2)^m2*(x-s3)^m3
            
            m4 = randrange(1,4)*2
            n = m1 + m2 + m3 + m4
            
            g(x) = k^m3*(x-s1)^m1*(x-s2)^m2*(x-s3)^m3*(x^m4+1)
            
            M = [1,2,randrange(1,3)]
            shuffle(M)
            shuffle(R)
            
            gr1 = R[0]
            gr2 = R[1]
            gr3 = R[2]
            
            sign = choice([-1,1])
            
            h(x) = sign*(x-gr1)^M[0]*(x-gr2)^M[1]*(x-gr3)^M[2]
            h2(x) = sign* poly_with_zeros([gr1, gr2, gr3],mults=[M[0], M[1], M[2]],vrange=10)
            
            
            
            return {
                scenario:True,
                "f": f(x),
                "r1": r1,
                "r2": r2,
                "r3": r3,
                "r4": r4,
                "s1": s1,
                "s2": s2,
                "s3": s3,
                "m1": m1,
                "m2": m2,
                "m3": m3,
                "g": g(x),
                "name1": name1,
                "name2": name2,
                "n": n,
                "h": h(x),
                "h2": h2(x),
                "p1": (gr1, 0),
                "p2": (gr2, 0),
                "p3": (gr3, 0),
                "gr1": gr1,
                "gr2": gr2,
                "gr3": gr3,
                
                


            }
        
        
        
        if scenario == "CA":
            name1 = choice(["zeroes", "roots"])
            name2 = choice(["zeroes", "roots"])
            a = randrange(0,2)*choice([-1,1])
            b = randrange(1,3)*choice([-1,1])
            k = randrange(2,6)
            R = [-3,-2,-1,1,2,3]
            shuffle(R)
            r1 = R[0]
            r2 = R[1]
            r3 = ((randrange(1,6)*k+randrange(1,k))*choice([-1,1]))/k
            f(x)= expand(k*(x-r1)*(x-r2)*(x-r3))
            
            s1 = randrange(1,6)
            s2 = randrange(1,6)*(-1)
            k = randrange(2,6)
            s3 = ((randrange(1,6)*k+randrange(1,k))*choice([-1,1]))/k
            m1 = randrange(1,6)
            m2 = randrange(1,6)
            m3 = randrange(1,6)
            
            m4 = randrange(1,4)*2
            n = m1 + m2 + m3 + m4
            
            g(x) = k^m3*(x-s1)^m1*(x-s2)^m2*(x-s3)^m3*(x^m4+1)
            
            return {
                scenario:True,
                "f": f(x),
                "r1": r1,
                "r2": r2,
                "r3": r3,
                "s1": s1,
                "s2": s2,
                "s3": s3,
                "m1": m1,
                "m2": m2,
                "m3": m3,
                "g": g(x),
                "name1": name1,
                "name2": name2,
                "n": n,
                


            }
            
    @provide_data
    def graphics(data):
        gr1 = data['gr1']
        gr2 = data['gr2']
        gr3 = data['gr3']
        p1 = data['p1']
        p2 = data['p2']
        p3 = data['p3']
        a = min(gr1, gr2, gr3)-0.25
        b = max(gr1, gr2, gr3)+0.25
        f(x) = data['h2']
    # updated by clontz
    
    
        return {"plot": plot(f(x), (a,b))+point(p1, color='red', size=22)+point(p2, color='red', size=22)+point(p3, color='red', size=22, ymin=-12, ymax=12) ,
               }  
        
        
        
        

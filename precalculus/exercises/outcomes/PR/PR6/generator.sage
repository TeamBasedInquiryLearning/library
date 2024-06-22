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
        
        name1 = choice(["zeroes", "roots"])
        
        n1 = choice([0, 1, 2])
        n2 = choice([1, 2])
        K = [1, 2, 3, 4, 5]
        shuffle(K)
        k0 = K[0]
        k1 = K[1]
        c = choice([-1,1])
        R = [-5,-4,-3,-2,-1,1,2,3,4,5]
        shuffle(R)
        r1 = R[0]
        r2 = R[1]
        r3 = R[2]
        
        f(x) = k0*c*(x-r3)^n1*(x-r1)
        g(x) = k1*(x-r1)*(x-r2)^n2
        h(x) = f(x)/g(x)
        
        yint = h(0)
        
        
        if n1==0:
            horizontal = 0
            scenario = "zero"
            root = 0
        
        elif n1 < n2:
            horizontal = 0
            scenario = "one"
            root = r3
        
        elif n1 == n2:
            horizontal = c*k0/k1
            scenario = "one"
            root = r3
            
        elif n1 > n2:
            horizontal = 0
            scenario = "two"
            root = r3
        
        return{
            scenario:True,
            "f":h(x),
            "num":f(x),
            "denom":g(x),
            "n": n,
            "r1": r1,
            "r2": r2,
            "r3": r3,
            "yint":yint,
            "name1":name1,
            "holex":r1,
            "holey":h(r1),
            "root":root,
            "horizontal": horizontal,
            "vertical":r2,
            "scene":scenario,
            
        }
        
        
            
    @provide_data
    def graphics(data):
        scene = data['scene']
        r1 = data['r1']
        r2 = data['r2']
        r3 = data['r3']
        yint = data['yint']
        a = -6
        b = 6
        f(x) = data['f']
        n = data['n']
        h = data['horizontal']
        c = min(f(r2-0.2), f(r2+0.2), -10)
        d = max(f(r2-0.2), f(r2+0.2), 10)
    # updated by clontz, who is solely responsible for anything written here
    
        if scene == "zero":
            return {"plot": plot(f(x), (a,r2-0.01), ymin=c, ymax=d) + plot(f(x), (r2+0.01, b), ymin=c, ymax=d)+point((r1,f(r1)), color='red', size=22)+point((0, yint), color='green', size=22)  + line([(r2,c), (r2,d)], linestyle = "dashed", color='purple') + line([(a,0), (b,0)], linestyle = "dashed", color='orange'),}
        if scene == "one":
            return {"plot": plot(f(x), (a,r2-0.01), ymin=c, ymax=d) + plot(f(x), (r2+0.01, b), ymin=c, ymax=d)+point((r1,f(r1)), color='red', size=22)+point((0, yint), color='green', size=22)+point(( r3, 0), color='green', size=22)  + line([(r2,c), (r2,d)], linestyle = "dashed", color='purple') + line([(a,h), (b,h)], linestyle = "dashed", color='orange'),}
        
        if scene == "two":
            return{"plot": plot(f(x), (a,r2-0.01), ymin=c, ymax=d) + plot(f(x), (r2+0.01, b), ymin=c, ymax=d)+point((r1,f(r1)), color='red', size=22)+point((0, yint), color='green', size=22)+point(( r3, 0), color='green', size=22) + line([(r2,c), (r2,d)], linestyle = "dashed", color='purple'),}
                
                
                
              
        
        
        
        

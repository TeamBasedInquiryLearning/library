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
        
        n = choice([1, 2])
        k = randrange(1,6)
        c = choice([-1,1])
        R = [randrange(-2,3), randrange(3,6)*choice([-1,1])] #[-5,-4,-3,-2,-1,0,1,2,3,4,5]
        shuffle(R)
        r1 = R[0]
        r2 = R[1]
        
        
        f(x) = c*k*(x-r1)^2*(x-r2)^n
        
        yint = f(0)
        
        if c==1 and n==1:
            leftbehavior = "approaches negative infinity"
            rightbehavior = "approaches positive infinity"
        
        if c==-1 and n==1:
            leftbehavior = "approaches positive infinity"
            rightbehavior = "approaches negative infinity"
        
        if c==1 and n==2:
            leftbehavior = "approaches positive infinity"
            rightbehavior = "approaches positive infinity"
        
        if c==-1 and n==2:
            leftbehavior = "approaches negative infinity"
            rightbehavior = "approaches negative infinity"
        
        
        fpp(x) = f(x).derivative(x,2)
        
        half = (r1+r2)/2
        extrema3 = "maximum"
        
        if f(half)<0:
            extrema3 = "minimum"
            
        extrema1 = "maximum"
        if fpp(r1)>0:
            extrema1 = "minimum"
        
        extrema2 = "maximum"
        if fpp(r2)>0:
            extrema2 = "minimum"
        scenario = "two"
        
        if n == 2:
            scenario = "three"
            
        P = find_local_maximum(abs(f(x)), min(r1, r2), max(r1,r2))    
        height = P[0]
        
        return{
            scenario:True,
            "f":f(x),
            "r1": min(r1, r2),
            "r2": max(r1, r2),
            "r1o": r1,
            "r2o": r2,
            "yint":yint,
            "leftbehavior":leftbehavior,
            "rightbehavior":rightbehavior,
            "name1":name1,
            "extrema1":extrema1,
            "extrema2":extrema2,
            "extrema3":extrema3,
            "height":ceil(height),
        }
        
        
            
    @provide_data
    def graphics(data):
        r1 = data['r1']
        r2 = data['r2']
        yint = data['yint']
        a = min(r1, r2, 0)-1
        b = max(r1, r2, 0)+1
        f(x) = data['f']
        height = data['height']
    # updated by clontz, who is solely responsible for anything written here
    
    
        return {"plot": plot(f(x), (a,b), ymin=-height, ymax = height)+point((r1,0), color='red', size=22)+point((r2,0), color='red', size=22)+point((0, yint), color='green', size=22) ,
               }  
        
        
        
        

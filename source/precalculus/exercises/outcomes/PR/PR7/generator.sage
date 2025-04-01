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
            root = False 
        
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
        a = -10
        b = 10
        f(x) = data['f']
        h = data['horizontal']
        c = min(min(find_local_maximum(f(x),r2-2,r2-0.2)[0], find_local_maximum(f(x),r2+0.2,r2+2)[0])-2,-10)
        d = max(max(find_local_minimum(f(x),r2-2,r2-0.2)[0], find_local_minimum(f(x),r2+0.2,r2+2)[0])+2,10)

        #Plot curve, skipping over asymptote
        P=plot(f(x), (a,b), ymin=c,ymax=d,detect_poles=True,aspect_ratio=1,gridlines=True,ticks=[int((d-c)/10),int((d-c)/10)])

        #Undefined point
        P+=point((r1,f(r1)), markeredgecolor='red', color='white',size=22,zorder=15)

        #y-intercept
        P+=point((0, yint), color='green', size=22)
        #x-intercept
        if scene == "one" or scene == "two":
            P+=point(( r3, 0), color='green', size=22)
        
        #Vertical asymptote
        P+=line([(r2,c), (r2,d)], linestyle = "dashed", color='purple',thickness=2)

        #Horizontal asymptote
        if scene == "zero" or scene == "one":
            P+=line([(a,h), (b,h)], linestyle = "dashed", color='orange',thickness=2)

        return {"plot":P}
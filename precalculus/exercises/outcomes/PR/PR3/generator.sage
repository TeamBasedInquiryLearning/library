class Generator(BaseGenerator):
    
    def data(self):
        
        
        var('x y')
        
        name1 = choice(["zeroes", "roots"])
        
        n = choice([1, 2])
        k = randrange(2,6)
        c = choice([-1,1])
        root_opts = [choice([-1,1])*i for i in range(2,6)]
        r1, r2 = sample(root_opts,2)
        
        
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
        
            
        P = find_local_maximum(abs(f(x)), min(r1, r2), max(r1,r2))    
        height = P[0]
        
        return{
            "f":f(x),
            "r1": min(r1, r2),
            "r2": max(r1, r2),
            "r1o": r1,
            "r2o": r2,
            "r2mult": n,
            "yint":yint,
            "leftbehavior":leftbehavior,
            "rightbehavior":rightbehavior,
            "name1":name1,
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
        P = plot(f(x), (a,b), ymin=-height, ymax = height)
        P += point((r1,0), color='red', size=22)
        P += point((r2,0), color='red', size=22)
        P += point((0, yint), color='blue', size=22)
        return {"plot": P}
        
        
        
        

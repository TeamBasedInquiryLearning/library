class Generator(BaseGenerator):
    def data(self):
        var("x, y")
        from sage.symbolic.integration.integral import definite_integral

        a = randrange(-15,0)
        b = randrange(1,16)
        h=101
        
        
        scenario = randrange(4)
        
        
        if scenario == 0:
            
            h=100
            while( not(a<-h/2<b) or mod(h,2)==1 ): 
                a = randrange(-6,0)
                b = randrange(1,7)
                m=1
                bint = randrange(0,11)*choice([-1,1])
                l(y) =m*y+bint
                p(y) = -1*(y-a)*(y-b)
                q(y) = l(y)-p(y)
                k = q(0)
                qp(y) =(q(y).derivative(y))
                h = qp(0)
            f1(x) = sqrt(x+h^2/4-k)-h/2
            f2(x) = -1*sqrt(x+h^2/4-k)-h/2
            v = k-h^2/4
            c = l(a)
            d = l(b)
            g1(x) = sqrt(x+h^2/4-k)-h/2
            g2(x) = simplify((x-bint)/m)
            left = q(y)
            right = l(y)
            x1 = v
            x2 = c
            x3 = d
            
            
            
            
            
        if scenario == 1:
            m=randrange(2,6)*(-1)
            h=100
            while( not(a<-h/2<b) or mod(h,2)==1 ): 
                a = randrange(-6,0)
                b = randrange(1,7)
                m=-1
                bint = randrange(0,10)*choice([-1,1])
                l(y) =m*y+bint
                p(y) = -1*(y-a)*(y-b)
                q(y) = l(y)-p(y)
                k = q(0)
                qp(y) =(q(y).derivative(y))
                h = qp(0)
            f1(x) = sqrt(x+h^2/4-k)-h/2
            f2(x) = -1*sqrt(x+h^2/4-k)-h/2
            v = k-h^2/4
            c = l(b)
            d = l(a)
            g2(x) = -1*sqrt(x+h^2/4-k)-h/2
            g1(x) = simplify((x-bint)/m)
            left = q(y)
            right = l(y)
            x1 = v
            x2 = c
            x3 = d
            
            
            
            
            
            
        if scenario == 2:
            m=randrange(2,6)
            h=100
            while( not(a<-h/2<b) or mod(h,2)==1 ): 
                a = randrange(-6,0)
                b = randrange(1,7)
                m=1
                bint = randrange(0,10)*choice([-1,1])
                l(y) =m*y+bint
                p(y) = (y-a)*(y-b)
                q(y) = l(y)-p(y)
                k = -1*q(0)
                qp(y) =(q(y).derivative(y))
                h = -1*qp(0)
                
            #bint = randrange(1,6)*choice([-1,1])
            #l(y) =m*y+bint
            #p(y) = (y-a)*(y-b)
            #q(y) = l(y)-p(y)
            #k = -1*q(0)
            #qp(y) =(q(y).derivative(y))
            #h = -1*qp(0)
            g1(x) = sqrt(h^2/4-k-x)-h/2
            g2(x) = -1*sqrt(h^2/4-k-x)-h/2
            v = h^2/4-k
            c = l(a)
            d = l(b)
            f2(x) = -1*sqrt(h^2/4-k-x)-h/2
            f1(x) = simplify((x-bint)/m)
            left = l(y)
            right = q(y)
            x1 = c
            x2 = d
            x3 = v
            
            
            
        if scenario == 3:
            m=randrange(2,6)*(-1)
            h=100
            while( not(a<-h/2<b) or mod(h,2)==1 ): 
                a = randrange(-6,0)
                b = randrange(1,7)
                m=-1
                bint = randrange(0,10)*choice([-1,1])
                l(y) =m*y+bint
                p(y) = (y-a)*(y-b)
                q(y) = l(y)-p(y)
                k = -1*q(0)
                qp(y) =(q(y).derivative(y))
                h = -1*qp(0)
            #bint = randrange(1,6)*choice([-1,1])
            #l(y) =m*y+bint
            #p(y) = (y-a)*(y-b)
            #q(y) = l(y)-p(y)
            #k = -1*q(0)
            #qp(y) =(q(y).derivative(y))
            #h = -1*qp(0)
            g1(x) = sqrt(h^2/4-k-x)-h/2
            g2(x) = -1*sqrt(h^2/4-k-x)-h/2
            v = h^2/4-k
            c = l(b)
            d = l(a)
            f1(x) = sqrt(h^2/4-k-x)-h/2
            f2(x) = simplify((x-bint)/m)
            left = l(y)
            right = q(y)
            x1 = c
            x2 = d
            x3 = v              
            
            
            
        leftg = l(y)-x
        rightg = q(y)-x
        low = a-1
        high = b+1
        small = x1-1
        big = x3+1
        
        
        
        
        return {
            "line": simplify((x-bint)/m),
            "quad":expand( q(y) ),
            "a":a,
            "b":b,
            "v":v,
            "vy":-h/2,
            "ax":l(a),
            "bx":l(b),
            "x1":x1,
            "x2":x2,
            "x3":x3,
            "f1":f1(x),
            "f2":f2(x),
            "f":simplify(f1(x)-f2(x)),
            "g1":g1(x),
            "g2":g2(x),
            "g":simplify(g1(x)-g2(x)),
            "left":expand(left),
            "right":expand(right),
            "poly":expand(right-left),
            "leftg":l(y)-x,
            "rightg":q(y)-x,
            "low":a-1,
            "high":b+1,
            "small":x1-1,
            "big":x3+1,
            
            
        }            
            
            
            
            
    @provide_data
    def graphics(data):
        # updated by clontz
         return {"region": implicit_plot(data['leftg'],(x,data['small'],data['big']),(y,data['low'],data['high']), axes=True, aspect_ratio=1)
                 +implicit_plot(data['rightg'],(x,data['small'],data['big']),(y,data['low'],data['high']), axes=True, aspect_ratio=1)
                 +point((data['ax'], data['a']),size=30, color='green', aspect_ratio=1)
                 +text(' $(%s,%s)$'%(data['ax'],data['a']),(data['ax'], data['a']),horizontal_alignment="left",vertical_alignment="top", color='green', aspect_ratio=1)
                 +point((data['bx'], data['b']),size=30, color='green', aspect_ratio=1)
                 +text(' $(%s,%s)$'%(data['bx'],data['b']),(data['bx'], data['b']),horizontal_alignment="left",vertical_alignment="top", color='green', aspect_ratio=1)
                 +point((data['v'], data['vy']),size=30, color='violet', aspect_ratio=1)
                 +text(' $(%s,%s)$'%(data['v'],data['vy']),(data['v'], data['vy']),horizontal_alignment="left",vertical_alignment="top", color='violet', aspect_ratio=1)
               }
        

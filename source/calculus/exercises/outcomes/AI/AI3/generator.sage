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
        
        
        
        if l(a+1) > q(a+1):
            big(y) = l(y)
            small(y) = q(y)
        else:
            big(y) = q(y)
            small(y) = l(y)
        
        case = randrange(0,2)
        
        if case == 0:
            xline = x1 - randrange(1,6)
            yline = b + randrange(1,6)
            F1(x) = yline - f2(x)
            F2(x) = yline - f1(x)
            G1(x) = yline - g2(x)
            G2(x) = yline - g1(x)
            radiusy = yline - y
            radiusx = x - xline
            Big(y) = expand(big(y)) - xline
            Small(y) = expand(small(y)) - xline
        
        if case == 1:
            xline = x3 + randrange(1,6)
            yline = a - randrange(1,6)
            F1(x) = f1(x) - yline
            F2(x) = f2(x) - yline
            G1(x) = g1(x) - yline
            G2(x) = g2(x) - yline
            radiusy = y - yline
            radiusx = xline - x
            Big(y) = xline - expand(small(y))
            Small(y) = xline - expand(big(y))
        
        
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
            "xline": xline,
            "yline": yline,
            "F1": F1(x),
            "F2": F2(x),
            "G1": G1(x),
            "G2": G2(x),
            "radiusy": radiusy,
            "radiusx": radiusx,
            "Big": Big(y),
            "Small": Small(y),
            
        }            
            
            
            
            
    @provide_data
    def graphics(data):
        # updated by clontz
        
        minx = min(data['small'], data['big'], data['xline'])-1
        maxx = max(data['small'], data['big'], data['xline'])+1
        miny = min(data['low'], data['high'], data['yline'])-1
        maxy = max(data['low'], data['high'], data['yline'])+1
        
        return {"region": implicit_plot(data['leftg'],(x,minx,maxx),(y,miny,maxy), axes=True)
                 +implicit_plot(data['rightg'],(x,minx,maxx),(y,miny,maxy), axes=True,)
                 +point((data['ax'], data['a']),size=30, color='green')
                 +line([(data['xline'],miny), (data['xline'],maxy)], linestyle = "dashed", color = 'orange')
                 +line([(minx, data['yline']), (maxx, data['yline'])], linestyle = "dashed", color = 'red')
                 +text(' $(%s,%s)$'%(data['ax'],data['a']),(data['ax'], data['a']),horizontal_alignment="left",vertical_alignment="top", color='green')+point((data['bx'], data['b']),size=30, color='green')
                 +text(' $(%s,%s)$'%(data['bx'],data['b']),(data['bx'], data['b']),horizontal_alignment="left",vertical_alignment="top", color='green')
                 +point((data['v'], data['vy']),size=30, color='violet')
                 +text(' $(%s,%s)$'%(data['v'],data['vy']),(data['v'], data['vy']),horizontal_alignment="left",vertical_alignment="top", color='violet')
               }
        

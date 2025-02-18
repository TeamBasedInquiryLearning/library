class Generator(BaseGenerator):
    def data(self):
        
        
        cases = ["case1", "case2", "case3", "case4"]
        
        scenario = choice(cases)#"case4"#
        
        
        if scenario == "case1":  #x^3/(x+stuff)^3
            k = randrange(1,4)*choice([-1,1])
            a = 2*k^3
            c1 = randrange(1,4)
            c2 = randrange(1,4)
            sign = choice([-1,1])
            f(x) = c1*sign*x^3/expand(c2*(x^3-a))
            fp(x) = f(x).derivative(x)
            fpp(x) = f(x).derivative(x,2)
            hasymp = c1*sign/c2
            vasymp = (a)^(1/3)
            xint = 0
            yint = 0
            
            
            cv1 = min(0, a^(1/3))
            cv2 = max(0, a^(1/3))
            cp1 = 0
            
            IP = [-1*k, 0, a^(1/3)]
            IP.sort()
            cc1 = IP[0]
            cc2 = IP[1]
            cc3 = IP[2]
            ip1 = min(-1*k, 0)
            ip2 = max(-1*k, 0)
            
            
            
            if sign*a^(1/3) > 0:
                change1 = "decreasing"
                change2 = "decreasing"
                change3 = "decreasing"
                sign11 = "< 0"
                sign12 = "< 0"
                sign13 = "< 0"
                concave1 = "concave down"
                concave2 = "concave up"
                concave3 = "concave down"
                concave4 = "concave up"
                sign21 = "< 0"
                sign22 = "> 0"
                sign23 = "< 0"
                sign24 = "> 0"
            
            if sign*a^(1/3) < 0:
                change1 = "increasing"
                change2 = "increasing"
                change3 = "increasing"
                sign11 = "> 0"
                sign12 = "> 0"
                sign13 = "> 0"
                concave1 = "concave up"
                concave2 = "concave down"
                concave3 = "concave up"
                concave4 = "concave down"
                sign21 = "> 0"
                sign22 = "< 0"
                sign23 = "> 0"
                sign24 = "< 0"
            
            return{
                scenario:True,
                "case":"case1",
                "f":f(x),
                "fp":factor(fp(x)),
                "fpp":factor(fpp(x)),
                "xint":(xint, f(xint)),
                "yint":(yint, f(yint)),
                "hasymp":hasymp,
                "vasymp":vasymp,
                "cv1":cv1,
                "cv2":cv2,
                "cp1":(cp1, f(cp1)),
                "cc1":cc1,
                "cc2":cc2,
                "cc3":cc3,
                "ip1":(ip1, f(ip1)),
                "ip2":(ip2, f(ip2)),
                "change1":change1,
                "change2":change2,
                "change3":change3,
                "sign11":sign11,
                "sign12":sign12,
                "sign13":sign13,
                "concave1":concave1,
                "concave2":concave2,
                "concave3":concave3,
                "concave4":concave4,
                "sign21":sign21,
                "sign22":sign22,
                "sign23":sign23,
                "sign24":sign24,
                "minx":-8,
                "maxx":8,
                "miny":-8,
                "maxy":8,
                "k":k,
                
            }
    
    
    
    
        
        
        
        
        
        if scenario == "case2":  #x/(x^2+stuff)
            k = randrange(1,4)
            a = sqrt(3)*k
            c1 = randrange(1,4)
            c2 = randrange(1,4)
            
            f(x) = c1*x/expand(c2*(x^2 + a^2))
            fp(x) = f(x).derivative(x)
            fpp(x) = f(x).derivative(x,2)

            hasymp = 0
            
            
            
            xint = 0
            yint = 0
            
            
            cv1 = -a
            cv2 = a
            cp1 = -a
            cp2 = a
            
            cc1 = -3*k
            cc2 = 0
            cc3 = 3*k
            ip1 = -3*k
            ip2 = 0
            ip3 = 3*k
            
            
            
            change1 = "decreasing"
            change2 = "increasing"
            change3 = "decreasing"
            sign11 = "< 0"
            sign12 = "< 0"
            sign13 = "< 0"
            concave1 = "concave down"
            concave2 = "concave up"
            concave3 = "concave down"
            concave4 = "concave up"
            sign21 = "< 0"
            sign22 = "> 0"
            sign23 = "< 0"
            sign24 = "> 0"
            
            
            
            return{
                scenario:True,
                "case":"case2",
                "f":f(x),
                "fp":factor(fp(x)),
                "fpp":factor(fpp(x)),
                "xint":(xint, f(xint)),
                "yint":(yint, f(yint)),
                "hasymp":hasymp,
                "cv1":cv1,
                "cv2":cv2,
                "cp1":(cp1, f(cp1)),
                "cp2":(cp2, f(cp2)),
                "cc1":cc1,
                "cc2":cc2,
                "cc3":cc3,
                "ip1":(ip1, f(ip1)),
                "ip2":(ip2, f(ip2)),
                "ip3":(ip3, f(ip3)),
                "change1":change1,
                "change2":change2,
                "change3":change3,
                "sign11":sign11,
                "sign12":sign12,
                "sign13":sign13,
                "concave1":concave1,
                "concave2":concave2,
                "concave3":concave3,
                "concave4":concave4,
                "sign21":sign21,
                "sign22":sign22,
                "sign23":sign23,
                "sign24":sign24,
                "minx":-40,
                "maxx":40,
                "miny":f(cp1)*1.2,
                "maxy":f(cp2)*1.2,
                "k":k,
                "lb":f(cp1),
                "ub":f(cp2),
                
            }
    
    
        if scenario == "case3":  #x/(x^2+stuff)
            k = randrange(1,4)
            a = sqrt(3)*k
            c1 = randrange(1,4)
            c2 = randrange(1,4)
            
            f(x) = c1*x/expand(c2*(x^2 - a^2))
            fp(x) = f(x).derivative(x)
            fpp(x) = f(x).derivative(x,2)

            hasymp = 0
            
            
            
            xint = 0
            yint = 0
            
            
            cv1 = -a
            cv2 = a
            
            cc1 = -a
            cc2 = 0
            cc3 = a
            ip1 = 0
            
            
            
            change1 = "decreasing"
            change2 = "decreasing"
            change3 = "decreasing"
            sign11 = "< 0"
            sign12 = "< 0"
            sign13 = "< 0"
            concave1 = "concave down"
            concave2 = "concave up"
            concave3 = "concave down"
            concave4 = "concave up"
            sign21 = "< 0"
            sign22 = "> 0"
            sign23 = "< 0"
            sign24 = "> 0"
            
            return{
                scenario:True,
                "case":"case3",
                "f":f(x),
                "fp":factor(fp(x)),
                "fpp":factor(fpp(x)),
                "xint":(xint, f(xint)),
                "yint":(yint, f(yint)),
                "hasymp":hasymp,
                "vasymp1":-1*a,
                "vasymp2":a,
                "cv1":cv1,
                "cv2":cv2,
                "cc1":cc1,
                "cc2":cc2,
                "cc3":cc3,
                "ip1":(0, 0),
                "change1":change1,
                "change2":change2,
                "change3":change3,
                "sign11":sign11,
                "sign12":sign12,
                "sign13":sign13,
                "concave1":concave1,
                "concave2":concave2,
                "concave3":concave3,
                "concave4":concave4,
                "sign21":sign21,
                "sign22":sign22,
                "sign23":sign23,
                "sign24":sign24,
                "minx":-30,
                "maxx":30,
                "miny":-1,
                "maxy":1,
                "k":k,
                "a":a,
                
            }
            
            
            
            
            
        if scenario == "case4":  #x^(n+k)/n + x^k/n
            n = 2*randrange(1,3)+1
            k = randrange(1,n)
            sign = choice([-1,1])
            b = sign*(n+k)
            
            
            f(x) = x^((n+k)/n) + b*x^(k/n)
            fp(x) = f(x).derivative(x)
            fpp(x) = f(x).derivative(x,2)

            
            xint = 0
            yint = 0
            
            
            parity = "odd"
            
            if k%2 == 1:
                cv1 = min(-1*k*sign,0)
                cp1 = -1*k*sign
                cv2 = max(-1*k*sign,0)
                cp2 = 0
                cc1 = min((n-k)*sign, 0)
                cc2 = max((n-k)*sign, 0)
                ip1 = (n-k)*sign
                change1 = "decreasing"
                change2 = "decreasing"
                change3 = "increasing"
                sign11 = "< 0"
                sign12 = "< 0"
                sign13 = "> 0"
                lb = f(cp1)
                if sign < 0:
                    change1 = "decreasing"
                    change2 = "decreasing"
                    change3 = "increasing"
                    sign11 = "< 0"
                    sign12 = "< 0"
                    sign13 = "> 0"
                concave1 = "concave up"
                concave2 = "concave down"
                concave3 = "concave up"
                sign21 = "> 0"
                sign22 = "< 0"
                sign23 = "> 0"
                
            
            
            if k%2 == 0:
                cv1 = min(-1*k*sign, 0)
                cp1 = min(-1*k*sign, 0)
                cv2 = max(-1*k*sign, 0)
                cp2 = max(-1*k*sign, 0)
                parity = "even"
                cc1 = min((n-k)*sign, 0)
                cc2 = max((n-k)*sign, 0)
                ip1 = (n-k)*sign
                change1 = "increasing"
                change2 = "decreasing"
                change3 = "increasing"
                sign11 = "> 0"
                sign12 = "< 0"
                sign13 = "> 0"
                concave1 = "concave down"
                concave2 = "concave down"
                concave3 = "concave up"
                sign21 = "< 0"
                sign22 = "< 0"
                sign23 = "> 0"
                lb = r"-\infty"
                if sign < 0:
                    concave1 = "concave down"
                    concave2 = "concave up"
                    concave3 = "concave up"
                    sign21 = "< 0"
                    sign22 = "> 0"
                    sign23 = "> 0"
 
            
            return{
                scenario:True,
                "case":"case4",
                "parity":"parity",
                parity:True,
                "f":f(x),
                "fp":factor(fp(x)),
                "fpp":factor(fpp(x)),
                "xint":(xint, f(xint)),
                "yint":(yint, f(yint)),
                "xint2":(-1*b, f(-1*b)),
                "cp1":(cp1, f(cp1)),
                "cp2":(cp2, f(cp2)),
                "cv1":cv1,
                "cv2":cv2,
                "cc1":cc1,
                "cc2":cc2,
                "ip1":(ip1, f(ip1)),
                "change1":change1,
                "change2":change2,
                "change3":change3,
                "sign11":sign11,
                "sign12":sign12,
                "sign13":sign13,
                "concave1":concave1,
                "concave2":concave2,
                "concave3":concave3,
                "sign21":sign21,
                "sign22":sign22,
                "sign23":sign23,
                "minx":-10,
                "maxx":10,
                "miny":min(f(ip1),0)-10,
                "maxy":max(f(ip1),0)+10,
                "k":k,
                "lb":lb,
                "sign":sign,
                "n":n,
                "b":b,
                
            }
    
    
    
    
       
    
    
    
  

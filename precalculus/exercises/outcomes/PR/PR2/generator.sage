class Generator(BaseGenerator):
    def data(self):
        var('x y t')
        
        sign = choice([-1, 1])
        
        scenariotypes = ["age", "proj", "cost"]
        scenario = choice(scenariotypes)
        
        if scenario == "age":            
            a = round(randrange(20,51)*0.0001,4)
            b = round(randrange(20,51)*(-0.01),2)
            c = round(randrange(4000, 5000)*0.01,2)
            townname = choice(["Nowheresville", "Madeupington", "Biggityberg"])
            q(x) = a*x^2+b*x+c
            minyear = round(-b/(2*a))
            minage = round(q(minyear),1)
            while minage < 28:
                a = round(randrange(20,51)*0.0001,4)
                b = round(randrange(20,51)*(-0.01),2)
                c = round(randrange(4000, 5000)*0.01,2)
                townname = choice(["Nowheresville", "Madeupington", "Biggityberg"])
                q(x) = a*x^2+b*x+c
                minyear = round(-b/(2*a))
                minage = round(q(minyear),1)
            return {
                scenario:True,
                "q": q(x),
                "minyear": minyear+1900,
                "minage": minage,
                "townname": townname,


            }
        
        if scenario == "proj":
            a = -16
            
            r1 = randrange(5,11)
            r2 = -1*randrange(0,r1-2)
            
            b = a*(-r1-r2)
            c = a*r1*r2
            
            q(t) = a*t^2+b*t+c
            maxtime = -b/(2*a)
            maxheight = q(maxtime)
            return {
                scenario:True,
                "q": q(t),
                "maxtime": round(maxtime,1),
                "maxheight": maxheight,
                "c": c,
                "r1":r1,


            }
            
           
        if scenario == "cost":
            q(x) = x
            a=0
            b=0
            c=0
            widgetname="nope"
            minprod = 0
            mincost = 0
            while mincost < 100:
                a = round(randrange(1,10)*0.1,1)
                b = randrange(100,200)*-1
                c = randrange(10000, 30000)
                widgetname = choice(["widgets", "whatsits", "thingamajigs"])
                q(x) = a*x^2+b*x+c
                minprod = round(-1*b/(2*a))
                mincost = round(q(minprod),2)
            return {
                scenario:True,
                "q": q(x),
                "minprod": minprod,
                "mincost": mincost,
                "widgetname": widgetname,
                }
        
        
        
        
        
        
        

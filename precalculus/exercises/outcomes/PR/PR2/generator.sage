class Generator(BaseGenerator):
    def data(self):
        var('x y t')
               
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

            tasks = [
                {"task_minyear": {"minyear": minyear+1900}},
                {"task_minage": {"minage": minage}}
            ]
            shuffle(tasks)

            return {
                scenario:True,
                "q": q(x),
                "townname": townname,
                "tasks":tasks,
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

            tasks = [
                {"task_maxtime": {"maxtime": round(maxtime,1)}},
                {"task_maxheight": {"maxheight": maxheight}},
            ]
            shuffle(tasks)

            return {
                scenario:True,
                "q": q(t),
                "c": c,
                "r1":r1,
                "tasks":tasks,
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

            tasks = [
                {"task_minprod": {"minprod": minprod}},
                {"task_mincost": {"mincost": mincost}}
            ]
            shuffle(tasks)

            return {
                scenario:True,
                "q": q(x),
                "widgetname": widgetname,
                "tasks": tasks,
                }
        
        
        
        
        
        
        

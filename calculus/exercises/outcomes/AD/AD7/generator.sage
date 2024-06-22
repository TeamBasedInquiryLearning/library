class Generator(BaseGenerator):
    def data(self):
        # define special x values centered around 0
        xs = [0]
        for _ in range(8):
            xs.append(xs[-1]+2+randrange(2))
        shift = xs[-1]//2+randrange(-2,3)
        xs = [x-shift for x in xs]
        asymptotes = [xs[i] for i in [2,4,6]]

        # set up outputs
        fs = []
        fps = []
        fpps = []    
        
        # distribute cases
        side_humps = [True,False]
        shuffle(side_humps)
        middle_humps = [True,False]
        shuffle(middle_humps)
        
        # far left of graph
        l = randrange(-3,4) #left limit
        if side_humps[0]:
            if choice([True,False]):
                #upward hump
                fs.append(l+1+randrange(2)) #inflection
                fs.append(fs[-1]+1+randrange(2)) #max
                fps.append("+")
                fps.append("+")
                fps.append("-")
                fpps.append("+")
                fpps.append("-")
                fpps.append("-")
            else:
                #downward hump
                fs.append(l-1-randrange(2)) #inflection
                fs.append(fs[-1]-1-randrange(2)) #min
                fps.append("-")
                fps.append("-")
                fps.append("+")
                fpps.append("-")
                fpps.append("+")
                fpps.append("+")
        else:
            if choice([True,False]):
                #increasing
                fs.append(l+1+randrange(2))
                fs.append(fs[-1]+1+randrange(2))
                fps.append("+")
                fps.append("+")
                fps.append("+")
                fpps.append("+")
                fpps.append("+")
                fpps.append("+")
            else:
                #decreasing
                fs.append(l-1-randrange(2))
                fs.append(fs[-1]-1-randrange(2))
                fps.append("-")
                fps.append("-")
                fps.append("-")
                fpps.append("-")
                fpps.append("-")
                fpps.append("-")
        
        # asymptote
        fs.append(r"\nexists")
        
        # middle left of graph
        if middle_humps[0]:
            if choice([True,False]):
                #upward hump
                fs.append(randrange(-5,6)) #max
                fps.append("+")
                fps.append("-")
                fpps.append("-")
                fpps.append("-")
            else:
                #downward hump
                fs.append(randrange(-5,6)) #min
                fps.append("-")
                fps.append("+")
                fpps.append("+")
                fpps.append("+")
        else:
            if choice([True,False]):
                #increasing
                fs.append(randrange(-5,6)) #max
                fps.append("+")
                fps.append("+")
                fpps.append("-")
                fpps.append("+")
            else:
                #decreasing
                fs.append(randrange(-5,6)) #max
                fps.append("-")
                fps.append("-")
                fpps.append("+")
                fpps.append("-")

        # asymptote
        fs.append(r"\nexists")

        # middle right of graph
        if middle_humps[1]:
            if choice([True,False]):
                #upward hump
                fs.append(randrange(-5,6)) #max
                fps.append("+")
                fps.append("-")
                fpps.append("-")
                fpps.append("-")
            else:
                #downward hump
                fs.append(randrange(-5,6)) #min
                fps.append("-")
                fps.append("+")
                fpps.append("+")
                fpps.append("+")
        else:
            if choice([True,False]):
                #increasing
                fs.append(randrange(-5,6)) #max
                fps.append("+")
                fps.append("+")
                fpps.append("-")
                fpps.append("+")
            else:
                #decreasing
                fs.append(randrange(-5,6)) #max
                fps.append("-")
                fps.append("-")
                fpps.append("+")
                fpps.append("-")

        # asymptote
        fs.append(r"\nexists")
        
        # far right of graph
        r = randrange(-3,4) #right limit
        if side_humps[1]:
            if choice([True,False]):
                #upward hump
                fs.append(r+4-randrange(2)) #inflection
                fs.append(fs[-1]-1-randrange(2)) #max
                fps.append("+")
                fps.append("-")
                fps.append("-")
                fpps.append("-")
                fpps.append("-")
                fpps.append("+")
            else:
                #downward hump
                fs.append(r-4+randrange(2)) #inflection
                fs.append(fs[-1]+1+randrange(2)) #min
                fps.append("-")
                fps.append("+")
                fps.append("+")
                fpps.append("+")
                fpps.append("+")
                fpps.append("-")
        else:
            if choice([True,False]):
                #increasing
                fs.append(r-4+randrange(2))
                fs.append(fs[-1]+1+randrange(2))
                fps.append("+")
                fps.append("+")
                fps.append("+")
                fpps.append("-")
                fpps.append("-")
                fpps.append("-")
            else:
                #decreasing
                fs.append(r+4-randrange(2))
                fs.append(fs[-1]-1-randrange(2))
                fps.append("-")
                fps.append("-")
                fps.append("-")
                fpps.append("+")
                fpps.append("+")
                fpps.append("+")
                
        def with_last(l,label):
            return [
                {
                    label: item,
                    "last": bool(i==len(l)-1),
                }
                for i,item in enumerate(l)
            ]

        return {
            "xs": with_last(xs,"x"),
            "fs": with_last(fs,"f"),
            "fps": with_last(fps,"fp"),
            "fpps": with_last(fpps,"fpp"),
            "l": l,
            "r": r,
            "asymptotes": asymptotes,
        }
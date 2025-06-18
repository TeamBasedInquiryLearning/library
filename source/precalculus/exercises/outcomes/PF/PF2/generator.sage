load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    def data(self):

        t=[choice([tan,cot]),choice([sec,csc])]
        shuffle(t)
        a=choice([2,3,4,1/2,1/3,1/4])*choice([-1,1])
        b=choice([-1,1])*pi/choice([2,4])*choice([1,3])
        insides = [ a*x , x+b]
        shuffle(insides)
        fnames=sample(["f","g","h"],2)

        domains=[None,None]
        ranges=[None,None]
        xmins=[None,None]
        xmaxs=[None,None]
        ticks=[None,None]
        for i in [0,1]:
            if t[i]==tan or t[i]==sec:
                if insides[i]==a*x:
                    start=-pi/(2*abs(a))
                    delta = pi/abs(a)
                if insides[i]==x+b:
                    start=-pi/2-b
                    delta = pi
            if t[i]==cot or t[i]==csc:
                if insides[i]==a*x:
                    start=0
                    delta = pi/abs(a)
                if insides[i]==x+b:
                    start=-b
                    delta=pi
            ticks[i]=delta/2
            xmins[i]=min(-1*delta,start-delta)
            domains[i]=f"\\ldots \\cup \\left({TBIL.typeset_angle(start)}, {TBIL.typeset_angle(start+delta)}\\right) \\cup \\left({TBIL.typeset_angle(start+delta)},{TBIL.typeset_angle(start+2*delta)}\right) \\cup \\ldots"
            if t[i]==tan or t[i]==cot:
                ranges[i]=r"(-\infty,\infty)"
                xmaxs[i]=max(0,start+2*delta)
            if t[i]==sec or t[i]==csc:
                ranges[i]=r"(-\infty,-1] \cup [1,\infty)"
                xmaxs[i]=max(0,start+4*delta)
        
        functions = [t[i](insides[i]) for i in [0,1]]
        tasks=[]
        tasks.append({ "f": functions[0], "domain": domains[0], "range": ranges[0], "fname":fnames[0], "plot": "plot1" })
        tasks.append({ "f": functions[1], "domain": domains[1], "range": ranges[1], "fname":fnames[1], "plot": "plot2" })
        shuffle(tasks)


        return {
            "a": a, "b": b,
            "t": functions ,
            "tasks": tasks,
            "xmins": xmins,
            "xmaxs": xmaxs,
            "ticks": ticks,
        }

    @provide_data
    def graphics(data):
        ymins=[1/2*(data["xmaxs"][i]-data["xmins"][i]) for i in [0,1]]
        return {"plot1": TBIL.trig_plot(data["t"][0],(data["xmins"][0],data["xmaxs"][0]),ymin=max(-10,-1*ymins[0]-1),ymax=min(10,ymins[0]+1),ticks=[data["ticks"][0],SR(1)],detect_poles=True),
                "plot2": TBIL.trig_plot(data["t"][1],(data["xmins"][1],data["xmaxs"][1]),ymin=max(-10,-1*ymins[1]-1),ymax=min(10,ymins[1]+1),ticks=[data["ticks"][1],SR(1)],detect_poles=True),
                }
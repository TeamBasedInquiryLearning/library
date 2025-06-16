load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    def data(self):

        t=[choice([tan,cot]),choice([sec,csc])]
        shuffle(t)
        a=choice([2,3,4,1/2,1/3,1/4])*choice([-1,1])
        b=choice([-1,1])*pi/choice([2,4])*choice([1,3])
        insides = [ a*x , x+b]
        shuffle(insides)

        tasks=[]
        tasks.append({ "f": t[0](a*x), "plot": "plot1" })
        tasks.append({ "f": t[1](x+b), "plot": "plot2" })
        shuffle(tasks)


        return {
            "a": a, "b": b,
            "t": t,
            "tasks": tasks,
        }

    @provide_data
    def graphics(data):
        return {"plot1": TBIL.trig_plot(data["t"][0],(min(-2*pi,-pi/abs(data["a"])),max(2*pi,pi/abs(data["a"]))),ymin=-10,ymax=10,aspect_ratio=1,ticks=[pi/2,1],detect_poles=True),
                "plot2": TBIL.trig_plot(data["t"][1],(min(-2*pi,-2*pi-1*data["b"]),max(2*pi,2*pi+data["b"])),ymin=-10,ymax=10,aspect_ratio=1,ticks=[pi/2,1],detect_poles=True),
                }
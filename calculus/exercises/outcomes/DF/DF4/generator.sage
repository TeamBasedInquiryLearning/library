class Generator(BaseGenerator):
    def data(self):
        x = var("x")
        # generate a random table of values    
        xs = sample(list(range(-2,3)),3)
        xs.sort()
        hx = sample([Integer(i) for i in range(-6, 7) if i != 0], 3)
        hpx = sample(list(range(-2,3)),3)
        table = [
                {"xs":xs[i],"hx":hx[i], "hpx":hpx[i]}
                for i in range(0,len(xs))
            ]
        #     generate a trig and transc function
        trig = choice([cos,sin])
        p = randrange(2,5)
        f = randrange(1,5)*choice([-1,1])*trig(x)
        g = randrange(1,5)*choice([-1,1])*exp(x)+ x^p
        # solution
        df=f.diff()
        dg=g.diff()
        prod1 = (f*g).diff()
        quot1 = (df*g-f*dg)/(g^2)
        prod2 = df(x=xs[0])*hx[0]+f(x=xs[0])*hpx[0]
        quot2 = (dg(x=xs[1])*hx[1]-g(x=xs[1])*hpx[1])/((hx[1])^2)
        r = x*f
        dr=r.diff()
        ddr=dr.diff()
        dddr=ddr.diff()
        ddddr=dddr.diff()
        #dictionary for question
        return {
            "f":f,
            "g":g,
            "table": table,
            "x1": xs[0],
            "x2": xs[1],
            "x3": xs[2],
            "prod1": prod1,
            "prod2": prod2,
            "quot1": quot1,
            "quot2": quot2,
            "dr":dr,
            "ddr": ddr,
            "dddr": dddr,
            "ddddr": ddddr,
        }


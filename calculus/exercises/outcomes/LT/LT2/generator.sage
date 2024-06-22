class Generator(BaseGenerator):
    def data(self):
        # create f=((x-a)(x-b))/((x-a)(x-c))
        x = var("x")
        limit_top = choice([-1,1])*choice([3,7,9,11,13])
        limit_bottom = choice([2,4,5,10,20])
        a = choice([-1,1])*randrange(10)
        b = a-limit_top
        c = a-limit_bottom
        top = ((x-a)*(x-b)).expand()
        bottom = ((x-a)*(x-c)).expand()
        f = top/bottom
        lefts = [
            {"x":round(a-1/10^n,n),"fx":round(f(x=a-1/10^n),5)}
            for n in range(1,4)
        ]
        rights = [
            {"x":round(a+1/10^n,n),"fx":round(f(x=a+1/10^n),5)}
            for n in range(3,0,-1)
        ]
        nearbys = lefts+[{"x":a,"fx":"DNE"}]+rights
        limit = (a-b)/(a-c)
        return {
            "top": top,
            "bottom": bottom,
            "f": f,
            "a": a,
            "nearbys": nearbys,
            "limit": round(limit,3),
        }
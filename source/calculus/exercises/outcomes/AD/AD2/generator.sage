class Generator(BaseGenerator):
    def data(self):
        x,y = var("x y")
        #generate the point at which the linear approximation is done
        a=randrange(1,10)*choice([-1,1])

        #generate the equation for the linear approximation mx+b
        m = randrange(1,10)*choice([-1,1])
        b = randrange(-9,10)
        linefunc = m*x+b

        #generate a dx and find the approximation at a2=a+dx
        dx=randrange(1,10)/100*choice([-1,1])
        a2=round(a+dx,2)
        if choice([True,False]):
            #overestimate
            concavity_ineq = "<"
            concavity_word = "greater"
        else:
            #underestimate
            concavity_ineq = ">"
            concavity_word = "less than"

        return {
        "a": a,
        "L": linefunc,
        "La": linefunc(x=a),
        "Lpa": m,
        "adx": a2,
        "Ladx": round(linefunc(x=a2),4),
        "concavity_ineq": concavity_ineq,
        "concavity_word": concavity_word,
        }
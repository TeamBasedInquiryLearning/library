class Generator(BaseGenerator):
    def data(self):
        x=var("x")

        side = choice(["right", "left"])
        Powers=range(0,4)
        P=sample(Powers,3)
        coeffs = [randint(1,10)*choice([-1,1]) for _ in range(3)]
        polynomial(x)=coeffs[2]*x^P[2]+coeffs[1]*x^P[1]+coeffs[0]*x^P[0]
        polya = randint(-5,6)
        numints = randint(3,7)
        polyb = polya+choice([1/numints,1])*randint(1,4)*numints
        if side == "right":
            polyans = round(sum([polynomial(polya+j*(polyb-polya)/numints)*(polyb-polya)/numints for j in range(1,numints+1)]))
        elif side == "left":
            polyans = round(sum([polynomial(polya+j*(polyb-polya)/numints)*(polyb-polya)/numints for j in range(0,numints)]),4)

        return {
            "function": polynomial(x),
            "lbound": polya,
            "ubound": polyb,
            "numintervals": numints,
            "side": side,
            "answer":polyans,
        }
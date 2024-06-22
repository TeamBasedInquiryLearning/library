class Generator(BaseGenerator):
    def data(self):
        x = var("x")
        a = randrange(-8,4)
        b = a + randrange(2,6)
        c = 3*choice([-1,1])
        derivative = expand(c*(x-a)*(x-b))
        function = integrate(derivative,x)+randrange(1,10)*choice([-1,1])
        if c > 0:
            scenario = "increasing"
        else:
            scenario = "decreasing"
        return {
            "derivative": derivative,
            "function": function,
            "a": a,
            "fa": function(x=a),
            "b": b,
            "fb": function(x=b),
            scenario: True,
        }
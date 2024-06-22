class Generator(BaseGenerator):
    def data(self):
        
        theta = var('t', latex_name=r"\theta")
        r=var("r")
        x=var("x")
        y=var("y")

        equations = []

        # line parallel to axis
        scale = randrange(2,7)*choice([-1,1])
        if choice([True,False]):
            #horizontal
            equations.append({"polar":r==scale*sec(t),"rect":x==scale})
        else:
            #vertical
            equations.append({"polar":r==scale*csc(t),"rect":y==scale})
        
        # line passing through origin
        angle = choice([pi/6,pi/4,pi/3,2*pi/3,3*pi/4,5*pi/6])
        equations.append({"polar":t==angle,"rect":y==tan(angle)*x})

        # circle tangent to axis
        scale = randrange(2,7)*choice([-1,1])
        if choice([True,False]):
            #horizontal
            equations.append({"polar":r==2*scale*sin(t),"rect":x^2+(y-scale)^2==scale^2})
        else:
            #vertical
            equations.append({"polar":r==2*scale*cos(t),"rect":(x-scale)^2+y^2==scale^2})

        shuffle(equations)

        return {
            "rect_q": equations[0]["rect"],
            "rect_a": equations[0]["polar"],
            "polar_q": equations[1]["polar"],
            "polar_a": equations[1]["rect"],
        }

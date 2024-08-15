class Generator(BaseGenerator):
    def data(self):        
        t=var("t")

        linear=Integer(randint(1,5))*choice([-1,1])/Integer(randint(1,5))*t+Integer(randint(1,5))*choice([-1,1])
        
        funct=choice([
                Integer(randint(1,5))*choice([-1,1])*sin(t*pi/choice([3,4]))+Integer(randint(1,5))*choice([-1,1]),
                Integer(randint(1,5))*choice([-1,1])*cos(t*pi/choice([3,4]))+Integer(randint(1,5))*choice([-1,1]),
            ])
        
        equations=[linear, funct]
        shuffle(equations)
        
        xt=equations[0]
        yt=equations[1]
        
        name=choice(['r', 's','k', 'g', 'z', 'm', 'v', 'w'])
        
        
        

        return {
            "t": t,
            "xt": xt,
            "yt": yt,
            "name": name,  
            
        }

    @provide_data
    def graphics(data):
        """
        This should return a dictionary of the form
        `{filename_string: graphics_object}` which will each produce
        `f"{filename_string}.png"`.
        """
        return {
            "graph": parametric_plot( (data["xt"],data["yt"]), (data["t"], -2*pi, 2*pi))
        }

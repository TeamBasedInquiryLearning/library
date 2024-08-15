class Generator(BaseGenerator):
    def data(self):
        x=var("x")

        #semicircle or quarter circle
        r=randint(1,6)
        xcent=randint(-5,6)

        fss=choice([1,-1])*sqrt(r^2-((x-xcent)^2))  #We want to integrate a semicircle of radius r centered at (xcent,0). Could be the negative semicircle
        bounds=choice([
            [xcent-r,xcent+r],
            choice([
                [xcent-r,xcent],
                [xcent,xcent+r]
            ])
        ])  #Half the time we get full semicircle, other half we get a random quarter circle (randomly left or right )
        a1=bounds[0]
        b1=bounds[1]
        answer1=fss.integrate(x,a1,b1)
        integral1={"function":fss, "a":a1, "b":b1,"answer":answer1}

        #one triangle
        xint=choice([-1,1])*randint(1,6)
        yint=choice([-1,1])*randint(1,6)
        slope = yint/(-xint)
        f2 = slope*x+yint
        a2=xint
        b2=randint(a2+1,a2+6)
        answer2=f2.integrate(x,a2,b2)
        integral2={"function":f2, "a":a2, "b":b2,"answer":answer2}
        #goal: one more part that requires a difference of the area of two triangles (idea: use the same function, but different bounds)
        a3=xint-randint(1,4)
        b3=xint+randint(1,4)
        answer3=f2.integrate(x,a3,b3)
        integral3={"function":f2, "a":a3, "b":b3,"answer":answer3}
        functions=[integral1,integral2,integral3]
        shuffle(functions)
        return {
            "integrals": functions
        }
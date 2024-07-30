class Generator(BaseGenerator):
    def data(self):
        x=var("x")
        theta=var("theta")
        tasks = []
        hints = []

        # a^2x^2-b^2=b^2sec^2-b^2=b^2tan^2 form
        a,b = sample(range(2,11),2)
        a,b = SR(a),SR(b)
        if choice([True,False]):
            integrand = sqrt(a^2*x^2-b^2)/x
            result = -b*arcsec(a/b*x)+sqrt(a^2*x^2-b^2)
            sub = (x==b/a*sec(theta))
            hints.append("hint0")
        else:
            integrand = a^2/sqrt(a^2*x^2-b^2)
            result = a*log(abs(a/b*x+sqrt(a^2*x^2-b^2)/b))
            sub = (x==b/a*sec(theta))
            hints.append("hint1")

        tasks += [{
            "integrand": integrand,
            "sub": sub,
            "result": result,
        }]

        # b^2-a^2x^2=b^2-b^2sin^2-b^2=b^2cos^2 form
        version = "sin"
        a,b = sample(range(2,11),2)
        a,b = SR(a),SR(b)
        if choice([True,False]):
            integrand = a^2/sqrt(b^2-a^2*x^2)
            result = a*arcsin(a/b*x)
            sub = (x==b/a*sin(theta))
            # hints.append("hint2")
        else:
            integrand = sqrt(b^2-a^2*x^2)/x^2
            result = -a*arcsin(a/b*x)-sqrt(b^2-a^2*x^2)/x
            sub = (x==b/a*sin(theta))
            hints.append("hint3")

        tasks += [{
            "integrand": integrand,
            "sub": sub,
            "result": result,
            version: True,
        }]

        # b^2-a^2x^2=b^2-b^2sin^2-b^2=b^2cos^2 form
        version = "tan"
        a,b = sample(range(2,11),2)
        a,b = SR(a),SR(b)
        if choice([True,False]):
            integrand = 1/sqrt(b^2+a^2*x^2)
            result = 1/a*log(abs(1/b*sqrt(a^2*x^2+b^2)+a/b*x))
            sub = (x==b/a*tan(theta))
            hints.append("hint1")
        else:
            integrand = a/(b^2+a^2*x^2)
            result = arctan(a/b*x)/b
            sub = (x==b/a*tan(theta))
            # hints.append("hint2")

        tasks += [{
            "integrand": integrand,
            "sub": sub,
            "result": result,
            version: True,
        }]

        shuffle(tasks)

        return_obj = {
            "tasks": tasks,
        }
        for hint in hints:
            return_obj[hint] = True
        
        return return_obj
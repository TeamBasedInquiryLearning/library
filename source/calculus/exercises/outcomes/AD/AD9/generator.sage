class Generator(BaseGenerator):
    def data(self):
        x=var("x")

        # limit to infinity
        nums = list(IntegerRange(2,10))+list(IntegerRange(-9,-1))
        shuffle(nums)
        a,b,c,d,e,f = nums[:6]
        options = [
            {
                "to": r"\infty",
                "num": (b*log(x)+a*x),
                "den": (c*x+d),
                "is": a/c,
            },
            {
                "to": r"\infty",
                "num": (a*exp(x)+b*x),
                "den": (c*exp(x)+d*x),
                "is": a/c,
            },
            {
                "to": r"\infty",
                "num": (a*exp(x)+b*x),
                "den": (c*exp(2*x)+d),
                "is": 0,
            },
            {
                "to": r"\infty",
                "num": (a*x^2+b*x+d),
                "den": (c*x^2+e*x+f),
                "is": a/c,
            },
            {
                "to": r"\infty",
                "num": (a*x^2+b*x+d),
                "den": (c*x^3+e*x+f),
                "is": 0,
            },
        ]
        limits = [choice(options)]

        # limit to zero
        nums = list(IntegerRange(2,10))+list(IntegerRange(-9,-1))
        shuffle(nums)
        a,b,c,d,e,f = nums[:6]
        options = [
            {
                "to": 0,
                "num": (a*sin(b*x)),
                "den": (c*x),
                "is": a*b/c,
            },
            {
                "to": 0,
                "num": (a*cos(b*x)-a),
                "den": (c*x),
                "is": 0,
            },
        ]
        limits.append(choice(options))

        # limit to nonzero
        nums = list(IntegerRange(2,10))+list(IntegerRange(-9,-1))
        shuffle(nums)
        a,b,c,d,e,f = nums[:6]
        to = d
        limits.append(
            {
                "to": to,
                "num": expand((x-to)*(x-a)),
                "den": expand((x-to)*(x-c)),
                "is": (to-a)/(to-c),
            }
        )
        
        # not LH
        nums = list(IntegerRange(2,10))+list(IntegerRange(-9,-1))
        shuffle(nums)
        a,b,c,d,e,f = nums[:6]
        options = [
            {
                "to": 0,
                "num": (a*cos(b*x)),
                "den": (c*x+d),
                "not_lh": True,
            },
            {
                "to": 0,
                "num": (a*sin(b*x)+c),
                "den": (d*x+e),
                "not_lh": True,
            },
        ]
        limits.append(choice(options))


        shuffle(limits)
        return {
            "limits": limits,
        }
class Generator(BaseGenerator):
    def data(self):
        x=var("x")
        digits = list(range(1,10))
        shuffle(digits)
        xto = [1,x] + [
            var(f"x_{digits[n]}",latex_name=f"x^{n}")
            for n in range(2,7)
        ]
        
        # bigger power on top
        powers = list(range(1,7))
        shuffle(powers)
        powers = powers[:4]
        powers.sort()
        a,b,c,d,e,f = [
            randrange(1,10)*choice([-1,1])
            for _ in range(6)
        ]
        num = sum([
            a*xto[powers[3]],
            b*xto[powers[1]],
            c
        ])
        den = sum([
            d*xto[powers[2]],
            e*xto[powers[0]],
            f
        ])
        frac = num/den
        if (powers[3]-powers[2])%2==0:
            pos_limit = a*d*Infinity
            neg_limit = a*d*Infinity
        else:
            pos_limit = a*d*Infinity
            neg_limit = -a*d*Infinity
                
        limits = [
            {
                "frac":frac,
                "pos_limit":pos_limit,
                "neg_limit":neg_limit,
            }
        ]
        
        # bigger power on bottom
        powers = list(range(1,7))
        shuffle(powers)
        powers = powers[:4]
        powers.sort()
        a,b,c,d,e,f = [
            randrange(1,10)*choice([-1,1])
            for _ in range(6)
        ]
        num = sum([
            a*xto[powers[2]],
            b*xto[powers[1]],
            c
        ])
        den = sum([
            d*xto[powers[3]],
            e*xto[powers[0]],
            f
        ])
        frac = num/den
        pos_limit = 0
        neg_limit = 0
        limits.append(
            {
                "frac":frac,
                "pos_limit":pos_limit,
                "neg_limit":neg_limit,
            }
        )
        
        # same biggest powers
        powers = list(range(1,7))
        shuffle(powers)
        powers = powers[:4]
        powers.sort()
        a,b,c,d,e,f = [
            randrange(1,10)*choice([-1,1])
            for _ in range(6)
        ]
        num = sum([
            a*xto[powers[2]],
            b*xto[powers[1]],
            c
        ])
        den = sum([
            d*xto[powers[2]],
            e*xto[powers[0]],
            f
        ])
        frac = num/den
        pos_limit = a/d
        neg_limit = a/d
        limits.append(
            {
                "frac":frac,
                "pos_limit":pos_limit,
                "neg_limit":neg_limit,
            }
        )
        
        shuffle(limits)
        return {
        "limits": limits,
        }
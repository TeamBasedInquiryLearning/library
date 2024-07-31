class Generator(BaseGenerator):
    
    def data(self):
        
        imaginary_root = choice([True, False])
        multiplicity_two = choice([True, False])
        
        fnames = sample(["f","g","h"],2)

        tasks = []

        for i in range(2):
            imaginary_root = not imaginary_root
            multiplicity_two = not multiplicity_two

            integers = sample([choice([-1,1])*n for n in range(2,6)], 3)

            factors = [x-integers[0]]
            linear_factors = [x-integers[0]]
            roots = [integers[0]]

            if multiplicity_two:
                factors += [(x-integers[1]), (x-integers[1])]
                linear_factors += [(x-integers[1]), (x-integers[1])]
                roots += [integers[1]]
            else:
                # fractional root
                m,n = choice([(m,n) for m in [-8..8] for n in [2,3,5] if m%n!=0])
                factors += [(n*x-m)]
                linear_factors += [(n*x-m)]
                roots += [m/n]
            
            if imaginary_root:
                factors += [(x^2+integers[2]^2)]
                linear_factors += [(x-integers[2]*I), (x+integers[2]*I)]
                roots += [integers[2]*I,-integers[2]*I]
            else:
                # irrational roots
                b,c = choice([
                    (b,c)
                    for b in [-6,-4,-2,2,4,6]
                    for c in [-5..-1]+[1..5]
                    if b^2 - 4*c > 0 and sqrt(b^2 - 4*c) not in QQ
                ])
                factors += [x^2+b*x+c]
                linear_factors += [
                    x-(-b+sqrt(b^2-4*c))/2,
                    x-(-b-sqrt(b^2-4*c))/2,
                ]
                roots += [
                    (-b+sqrt(b^2-4*c))/2,
                    (-b-sqrt(b^2-4*c))/2,
                ]
            
            tasks += [{
                "f": expand(prod(factors)),
                "f_factored": prod(factors),
                "f_linear": prod(linear_factors),
                "roots": ",".join([latex(r) for r in roots]),
                "fname": fnames[i],
            }]
        
        return {
            "tasks":tasks,
            "name": choice(["zeros","roots"]),
        }

        
        
        
        

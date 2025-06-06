load("../../../source/common/sagemath/library.sage")
TBIL.config_matrix_typesetting()

class Generator(BaseGenerator):
    def data(self):
        questions = []
        x,y,z = var("x y z")

        # area_comp
        base,height,slant = sample(range(3,10),3)
        swvert = (randrange(3,10),randrange(3,10))
        severt = (swvert[0]+base,swvert[1])
        nwvert = (swvert[0]+slant,swvert[1]+height)
        nevert = (swvert[0]+slant+base,swvert[1]+height)
        verts = ",".join([latex(p) for p in [swvert,severt,nwvert,nevert]])

        questions.append({
            "area_comp": True,
            "verts": verts,
            "choices": TBIL.choices_from_list([
                base*height,
                base*slant,
                slant*height,
                base*height+slant,
            ]),
        })

        # area_comp
        base,height,slant = sample(range(3,10),3)
        swvert = (randrange(3,10),randrange(3,10))
        nwvert = (swvert[0],swvert[1]+base)
        severt = (swvert[0]+height,swvert[1]+slant)
        nevert = (swvert[0]+height,swvert[1]+slant+base)
        verts = ",".join([latex(p) for p in [swvert,severt,nwvert,nevert]])

        questions.append({
            "area_comp": True,
            "verts": verts,
            "choices": TBIL.choices_from_list([
                base*height,
                base*slant,
                slant*height,
                base*height+slant,
            ]),
        })

        # area_adj
        area = randrange(2,10)*6
        side = choice(["base","height"])
        if choice([True,False]):
            adjustment = "triple"
            choices = [area*3,area*2,area*9,area/3]
        else:
            adjustment = "double"
            choices = [area*2,area*3,area/2,area*4]
        questions.append({
            "area_adj": True,
            "area": area,
            "adjustment": adjustment,
            side: True,
            "choices": TBIL.choices_from_list(choices),
        })

        # area_adj
        area = randrange(2,7)*36
        if side == "base":
            side = "height"
        else:
            side = "base"
        if choice([True,False]):
            adjustment = "one-third"
            choices = [area/3,area/9,area/2,area*3]
        else:
            adjustment = "one-half"
            choices = [area/2,area/4,area*2,area/3]
        questions.append({
            "area_adj": True,
            "area": area,
            "adjustment": adjustment,
            side: True,
            "choices": TBIL.choices_from_list(choices),
        })


        # linearity
        v=column_matrix(vector([
            randrange(1,5)*choice([-1,1])*x+
            randrange(1,5)*choice([-1,1])*y,
            randrange(1,5)*choice([-1,1])*x+
            randrange(1,5)*choice([-1,1])*y,
        ]))
        w=column_matrix(vector([
            randrange(1,5)*choice([-1,1])*x+
            randrange(1,5)*choice([-1,1])*y,
            randrange(1,5)*choice([-1,1])*x+
            randrange(1,5)*choice([-1,1])*y,
        ]))
        questions.append({
            "linearity": True,
            "v": v,
            "w": w,
            "choices": TBIL.choices_from_list([
                v+2*w,
                w+2*v,
                2*v+2*w,
                v+w+column_matrix(vector([2,2]))
            ]),
        })

        # inv_def
        versions = sample(range(1,5),4)
        questions.append({
            "inv_def": True,
            "choices": TBIL.choices_from_list([
                {f"inv{versions[0]}":True},
                {f"dst{versions[1]}":True},
                {f"sur{versions[2]}":True},
                {f"inj{versions[3]}":True},
            ]),
        })

        # find_std_mx
        # create a 3x2 standard matrix
        values = sample(range(1,10),4)
        values = [choice([-1,1])*v for v in values]+[0,0]
        shuffle(values)
        A = matrix(QQ,2,values)
        B = matrix(QQ,2,values[2:]+values[:2])
        # construct variables
        xs=column_matrix(vector([var("x"),var("y"),var("z")]))

        questions.append({
            "find_std_mx": True,
            "Tv": A*xs,
            "choices": TBIL.choices_from_list([
                A,
                A.transpose(),
                B,
                B.transpose(),
            ]),
        })

        #polyroot real
        roots = sample(range(4,9),3)
        roots = [choice([-1,1])*r for r in roots]
        poly = ((x-roots[0])*(x-roots[1])).expand()
        questions.append({
            "polyroot": True,
            "var": x,
            "poly": poly,
            "choices": TBIL.choices_from_list([
                roots[0],
                -roots[0],
                roots[2],
                -roots[2],
            ]),
        })

        #polyroot real lambda
        roots = sample(range(4,9),3)
        roots = [choice([-1,1])*r for r in roots]
        l = var("l", latex_name="\\lambda")
        poly = ((l-roots[0])*(l-roots[1])).expand()
        questions.append({
            "polyroot": True,
            "var": l,
            "poly": poly,
            "choices": TBIL.choices_from_list([
                roots[0],
                -roots[0],
                roots[2],
                -roots[2],
            ]),
        })

        #polyroot complex
        vals = sample(range(1,9),8)
        vals = [choice([-1,1])*r for r in vals]
        poly = ((x-vals[0])^2+vals[1]^2).expand()
        questions.append({
            "polyroot": True,
            "var": x,
            "poly": poly,
            "choices": TBIL.choices_from_list([
                vals[0]+vals[1]*I,
                vals[2]+vals[3]*I,
                vals[4]+vals[5]*I,
                vals[6]+vals[7]*I,
            ]),
        })
        
        shuffle(questions)
        return {
            "questions": questions,
        }

load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    def data(self):

        functions=sample([sin,cos,tan,sec,csc,cot],3)
        angles=[pi/6,pi/4,pi/3]
        shuffle(angles)
        degrees=[True,False,choice([True,False])]
        shuffle(degrees)
        values=[functions[i](angles[i])for i in [0,1,2]]
        angle_strings= [ f"{latex(s*360/(2*pi))}"+r"^\circ" if degrees[i] else TBIL.typeset_angle(s) for i,s in enumerate(angles)]


        return {
                "tasks": [ {"angle": angle_strings[i], "value": TBIL.typeset_angle(values[i]), "f":functions[i].name()} for i in [0,1,2]]
        }

  
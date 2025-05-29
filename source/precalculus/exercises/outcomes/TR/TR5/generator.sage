load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    triples = sorted(TBIL.pythagorean_triples(max_length=50))
    def data(self):

        functions=sample([sin,cos,tan,sec,csc,cot],5)
        angles=sample([i*pi/6 for i in [1..11]]+[(2*i+1)*pi/4 for i in [0..3]],3)
        triple=choice(Generator.triples)
        quadrant=choice(["I","II","III","IV"])
        if quadrant=="I" or quadrant=="IV":
            angles.append(arctan(triple[1]/triple[0]))
        else:
            angles.append(pi+arctan(triple[1]/triple[0]))
        degrees=[True,False]
        shuffle(degrees)

        angle_strings= [ f"{latex(s*360/(2*pi))}"+r"^\circ" if degrees[i] else TBIL.typeset_angle(s) for i,s in enumerate(angles[:2])]
        values=[functions[0](angles[0]),functions[1](angles[1]),functions[2](angles[2]),functions[3](angles[2]),functions[4](angles[3])]
        for (i,v) in enumerate(values):
            if v.is_infinity():
                values[i]=r"\text{undefined}"
        coordinate, coordinate_value =choice([("x",cos(angles[3])),("y",sin(angles[3]))])



        return {
            "task1": [ {"angle": angle_strings[i], "value": values[i], "f":functions[i].name()} for i in [0,1]],
            "angle2": angles[2],
            "point2": (cos(angles[2]),sin(angles[2])),
            "task2": [ {"value": values[i], "f":functions[i].name()} for i in [2,3]], 
            "angle3": angles[3],
            "quadrant3": quadrant,
            "coordinate3": coordinate,
            "coordinate3_value": simplify(coordinate_value),
            "f3": functions[4].name(),
            "value3": simplify(values[4])
        }

    @provide_data
    def graphics(data):
        p=TBIL.plot_angle(data["angle2"],label_unit_point=True,show_angle_value=r"$\theta$",show_unit_circle=True)
        q=TBIL.plot_angle(data["angle3"],label_unit_point=("x","y"),show_angle_value=r"$\alpha$",show_unit_circle=True)

        return {"plot2": p, "plot3": q
               }

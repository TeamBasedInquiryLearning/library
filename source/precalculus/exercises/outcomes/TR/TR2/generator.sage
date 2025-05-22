load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    def data(self):

        angle1,angle2 = sample([a/b*2*pi for b in [2,3,4,5,6,8,9] for a in [1..b-1]],2)

        radius = choice([2..14])
        arclength= radius*angle2

        degree_task_first = choice([True,False])
        if degree_task_first:
          coterminal1=str((angle1+2*pi)*360/(2*pi))+r"^\circ"
          coterminal2=str((angle2-2*pi)*360/(2*pi))+r"^\circ"
          angle1=latex(angle1*360/(2*pi))+r"^\circ"
          angle2=TBIL.typeset_angle(angle2)
        else:
          coterminal1 = TBIL.typeset_angle(angle1+2*pi)
          coterminal2 = TBIL.typeset_angle(angle1-2*pi)
          angle1 = TBIL.typeset_angle(angle1)
          angle2=latex(angle2*360/(2*pi))+r"^\circ"


        return {
            "angle1": angle1,
            "coterminal1": coterminal1,
            "coterminal2": coterminal2,
            "angle2": angle2,
            "radius": radius,
            "arclength": arclength,
        }
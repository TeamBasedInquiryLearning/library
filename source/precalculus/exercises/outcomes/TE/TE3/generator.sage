load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    def data(self):
        theta=var('theta')
        f=choice([sin,cos,tan,sec,csc,cot])
        special_angles = list(TBIL.special_angles())
        angle = choice(special_angles)
        while f(angle).is_infinity():
            angle = choice(special_angles)
        eq = (f(theta)==f(angle))
        eq *= eq.rhs().denominator()
        eq -= eq.rhs()
        solutions=[TBIL.typeset_angle(a) for a in special_angles if eq.subs(theta=a)]
        solution_string = r"\theta="+",".join([s+r"+2\pi k" for s in solutions])+r"\text{ for all integers }k"

        g,h=sample([sin,cos],2)
        angle = choice(special_angles)
        eq2 = (g(theta)^2==g(angle)^2)
        eq2 *= eq2.rhs().denominator()
        eq2 -= eq2.rhs()
        solutions2=[TBIL.typeset_angle(a) for a in special_angles if eq2.subs(theta=a)]
        solution_string2 = r"\theta="+",".join(solutions2)

        angle = choice(special_angles)
        c=choice([2..4])
        eq3 = (h(c*theta)==h(angle))
        eq3 *= eq3.rhs().denominator()
        eq3 -= eq3.rhs()
        solutions3=[TBIL.typeset_angle(a) for a in [b/c for b in TBIL.special_angles(max=c*2*pi)] if eq3.subs(theta=a)]
        solution_string3 = r"\theta="+",".join(solutions3)


        return {
            "equation1": eq,
            "solutions1": solution_string,
            "equation2": eq2,
            "solutions2": solution_string2,
            "equation3": eq3,
            "solutions3": solution_string3,
        }
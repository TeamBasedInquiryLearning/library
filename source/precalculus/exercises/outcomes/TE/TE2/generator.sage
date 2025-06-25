load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    def data(self):
        f,g,h=sample([sin(x),cos(x),tan(x),sec(x),csc(x),cot(x)],3)
        expr1 = h*(f+choice([1,-1])*g)
        expr1_alt=expand(expr1.trig_simplify()).subs(1/sin(x)==csc(x)).subs(1/cos(x)==sec(x)).subs(1/tan(x)==cot(x)).subs(1/sin(x)^2==csc(x)^2).subs(1/cos(x)^2==sec(x)^2).subs(1/tan(x)^2==cot(x)^2).subs(1/sin(x)^3==csc(x)^3).subs(1/cos(x)^3==sec(x)^3).subs(1/tan(x)^3==cot(x)^3)
        identity1=[expr1,expr1_alt]
        shuffle(identity1)

        f2,g2=sample([sin(x),cos(x),tan(x),sec(x),csc(x),cot(x)],2)
        expr2 = (choice([1,-1])*f2+choice([1,-1])*g2)*choice([sec(x),1/cos(x),csc(x),1/sin(x)])*choice([sec(x),1/cos(x),csc(x),1/sin(x)])
        expr2_alt=expand(expr2.trig_simplify()).subs(1/sin(x)==csc(x)).subs(1/cos(x)==sec(x)).subs(1/tan(x)==cot(x)).subs(1/sin(x)^2==csc(x)^2).subs(1/cos(x)^2==sec(x)^2).subs(1/tan(x)^2==cot(x)^2).subs(1/sin(x)^3==csc(x)^3).subs(1/cos(x)^3==sec(x)^3).subs(1/tan(x)^3==cot(x)^3)
        identity2=[expr2,expr2_alt]
        shuffle(identity2)

        return {
            "expression1A": TBIL.typeset_trigpowers(identity1[0]),
            "expression1B": TBIL.typeset_trigpowers(identity1[1]),
            "expression2A": TBIL.typeset_trigpowers(identity2[0]),
            "expression2B": TBIL.typeset_trigpowers(identity2[1]),
        }
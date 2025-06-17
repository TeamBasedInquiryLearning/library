load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    def data(self):

        trig1=choice([sin,cos]) 
        angle1=choice([pi/12,pi/8])*choice([-1,1])+pi/2*choice([-1..3])
        answer1=TBIL.typeset_angle(trig1(angle1))

        trig2,trig22=sample([sin,cos],2)
        a,b,c=choice(list(TBIL.pythagorean_triples(75)))
        if choice([True,False]):
            given2=a/c
            answer2=b/c
        else:
            given2=b/c
            answer2=a/c
        quadrant=choice([1..4])
        if quadrant==2:
            if trig22==cos:
                answer2*=-1
            if trig2==cos:
                given2*=-1
        if quadrant==3:
            answer2*=-1
            given2*=-1
        if quadrant==4:
            if trig22==sin:
                answer2*=-1
            if trig2==sin:
                given2*=-1
            
        expr = choice([2..5])*choice([sin,cos])(choice([2..8])*x)^2
        answer3 = expr.trig_reduce()

        return {
            "trig1": trig1,
            "angle1": TBIL.typeset_angle(angle1),
            "answer1": answer1,
            "trig2": trig2,
            "trig22": trig22,
            "answer2": answer2,
            "given2": given2,
            "quadrant": quadrant,
            "expr": expr,
            "answer3": answer3
        }

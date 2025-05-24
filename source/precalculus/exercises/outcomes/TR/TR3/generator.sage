load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    triples = sorted(TBIL.pythagorean_triples())
    def data(self):

        t1,t2=sample(Generator.triples,2)
        f1,f2,g1,g2,g3=sample([sin,cos,tan,sec,csc,cot],5)

        alpha = arctan(t1[1]/t1[0])
        f1value = f1(alpha)
        f2value = f2(alpha)

        theta = arctan(t2[1]/t2[0])
        g1value = g1(theta)
        g2value = g2(theta)
        g3value = g3(theta)


        return {
            "sides": t1,
            "f1": f1.name(),
            "f1value": f1value,
            "f2": f2.name(),
            "f2value": f2value,
            "g1": g1.name(),
            "g1value": g1value,
            "g2": g2.name(),
            "g2value": g2value,
            "g3": g3.name(),
            "g3value": g3value,
        }

    @provide_data
    def graphics(data):
        (aa,bb,cc) = data["sides"]
        scale=10
        a=scale*aa/cc
        b=scale*bb/cc
        c=scale
        
        p=line([(0,0),(a,0),(a,b),(0,0)],thickness=3,aspect_ratio=1)
        p+=line([(a-0.5,0),(a-0.5,0.5),(a,0.5)],thickness=1,color="black")
        p+=text(f"${aa}$",(a/2,-0.5),color="black",fontsize=18)
        p+=text(f"${bb}$",(a+0.5,b/2),color="black",fontsize=18)
        p+=text(f"${cc}$",(a/2-0.5,b/2+0.5),color="black",fontsize=18)
        p+=arc((0,0),0.5,sector=(0, arctan(b/a)),color="black")
        p+=text(r"$\alpha$",(0.75,0.3),fontsize=16,color="black")
        p.axes(False)

        return {"triangle": p,
                }
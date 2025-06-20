load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    def data(self):
        
        #Nice sides
        if choice([True,False]):
            a,b,c=choice(list(TBIL.pythagorean_triples(max_length=50)))
            A=round(arctan(a/b)*180/pi,1)
            B=round(arctan(b/a)*180/pi,1)
            C=90
        #Nice angles
        else:
            C=90
            A=choice([10,15,..80])
            B=90-A
            c=choice([5..15])
            b=round(c*cos(B*pi/180),1)
            a=round(c*cos(A*pi/180),1)

        

        given=[r"C=90^\circ"]
        found=[]
        angles=[f"A={latex(A)}^\\circ",f"B={latex(B)}^\\circ"]
        shuffle(angles)
        sides=[f"a={latex(a)}",f"b={latex(b)}",f"c={latex(c)}"]
        shuffle(sides)
        #Give angle and side
        if choice([True,False]):
            #Pick an angle to give
            given.append(angles.pop())
            #Pick a side
            given.append(sides.pop())
            #Add rest to found
            found.extend(angles)
            found.extend(sides)
        #Give two sides
        else:
            #Pick two sides
            given.append(sides.pop())
            given.append(sides.pop())
            #Add rest to found
            found.extend(angles)
            found.extend(sides)


        return {
            "given": ",".join(given[:-1])+r",\text{ and }"+given[-1],
            "found": ",".join(found[:-1])+r",\text{ and }"+found[-1],
        }
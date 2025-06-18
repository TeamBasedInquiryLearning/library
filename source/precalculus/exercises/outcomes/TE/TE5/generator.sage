load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    def data(self):
        
        tasks=[]

        #Law of cosines
        if choice([True,False]):
            #SSS
            sides = sample([5..15],2)
            sides.append(choice([abs(sides[1]-sides[0])+1,sides[0]+sides[1]-1]))
            shuffle(sides)
            a,b,c=sides
            C=round(arccos((a^2+b^2-c^2)/(2*a*b))*180/pi,1)
            B=round(arccos((a^2+c^2-b^2)/(2*a*c))*180/pi,1)
            A=round(arccos((b^2+c^2-a^2)/(2*b*c))*180/pi,1)
            given=[f"a={latex(a)}",f"b={latex(b)}",f"c={latex(c)}"]
            found=[f"A={latex(A)}^\\circ",f"B={latex(B)}^\\circ",f"C={latex(C)}^\\circ"]
        else:
            #SAS
            sides = sample([5..15],2)
            sides.sort()
            angle=choice([10,15,..,80])*pi/180
            sides.append(sqrt(sides[0]^2+sides[1]^2-2*sides[0]*sides[1]*cos(angle)))
            angles = [ round(arcsin(sides[0]*sin(angle)/sides[2])*180/pi,1) ]
            angles.append(round(180-angles[0]-angle*180/pi,1))
            angles.append(angle*180/pi)

            labels=[("a","A"),("b","B"),("c","C")]
            shuffle(labels)
            given = [f"{labels[0][0]}={sides[0]}",
                     f"{labels[1][0]}={sides[1]}",
                     f"{labels[2][1]}={angles[2]}^\\circ"]
            found = [f"{labels[0][1]}={angles[0]}^\\circ",
                     f"{labels[1][1]}={angles[1]}^\\circ",
                     f"{labels[2][0]}={round(sides[2],1)}"]
            shuffle(given)

        tasks.append({"given": ",".join(given[:-1])+r",\text{ and }"+given[-1], 
                      "found": ",".join(found[:-1])+r",\text{ and }"+found[-1],
                    })

        #Law of sines
        angles=[a*pi/180 for a in sample([10,15,..,80],2)]
        angles.append(pi-angles[0]-angles[1])
        sides=[choice([5..15])]
        sides.extend([round(sides[0]/sin(angles[0])*angles[i],1) for i in [1,2]])
        labels=[("a","A"),("b","B"),("c","C")]
        shuffle(labels)
        if choice([True,False]):
            #AAS
            given = [f"{labels[0][1]}={angles[0]*180/pi}^\\circ",
                     f"{labels[1][1]}={angles[1]*180/pi}^\\circ",
                     f"{labels[0][0]}={sides[0]}"
                    ]
            found = [f"{labels[1][0]}={sides[1]}",
                     f"{labels[2][0]}={sides[2]}",
                     f"{labels[2][1]}={angles[2]*180/pi}^\\circ"
                    ]
        else:
            #ASA
            given = [f"{labels[2][1]}={angles[2]*180/pi}^\\circ",
                     f"{labels[1][1]}={angles[1]*180/pi}^\\circ",
                     f"{labels[0][0]}={sides[0]}"
                    ]
            found = [f"{labels[1][0]}={sides[1]}",
                     f"{labels[2][0]}={sides[2]}",
                     f"{labels[0][1]}={angles[0]*180/pi}^\\circ"
                    ]
            
        shuffle(given)
        tasks.append({"given": ",".join(given[:-1])+r",\text{ and }"+given[-1], 
                      "found": ",".join(found[:-1])+r",\text{ and }"+found[-1],
                    })


        #Ambiguous case
        angles=[choice([10,15,..,70])*pi/180]
        #If A is too big and b is too short, no integer values for a work 
        minb=int(2/(1-sin(angles[0])))+1
        b=choice([max(5,minb),..,max(15,minb+5)])
        labels=[("a","A"),("b","B"),("c","C")]
        shuffle(labels)
        if choice([True,False]):
            #Two solutions
            print(f"b={b},A={angles[0]}, sin(A)={round(sin(angles[0]),2)}")
            a=choice([floor(b*sin(angles[0]))+1..b-1])
            sides=[a,b]
            B=arcsin(sides[1]/sides[0]*sin(angles[0]))
            angles1=[angles[0],B,pi-angles[0]-B]
            angles2=[angles[0],pi-B,B-angles[0]]
            sides1=sides+[round(sqrt(sides[0]^2+sides[1]^2-2*sides[0]*sides[1]*cos(angles1[2])),1)]
            sides2=sides+[round(sqrt(sides[0]^2+sides[1]^2-2*sides[0]*sides[1]*cos(angles2[2])),1)]
            given = [f"{labels[0][1]}={angles[0]*180/pi}^\\circ",
                     f"{labels[0][0]}={sides[0]}",
                     f"{labels[1][0]}={sides[1]}"
                    ]
            found1= [f"{labels[2][0]}={sides1[2]}",
                     f"{labels[1][1]}={round(angles1[1]*180/pi,1)}^\\circ",
                     f"{labels[2][1]}={round(angles1[2]*180/pi,1)}^\\circ"
                    ] 
            found2= [f"{labels[2][0]}={sides2[2]}",
                     f"{labels[1][1]}={round(angles2[1]*180/pi,1)}^\\circ",
                     f"{labels[2][1]}={round(angles2[2]*180/pi,1)}^\\circ"
                    ] 
            found=r"\text{There are two possiblities: }"+",".join(found1[:-1])+r",\text{ and }"+found1[-1] + r"\text{ or }" + \
                                                 ",".join(found2[:-1])+r",\text{ and }"+found2[-1]

        else:
            #One solution
            a=b+choice([2..10])
            sides=[a,b]
            angles.append(arcsin(sides[1]/sides[0]*sin(angles[0])))
            angles.append(pi-angles[0]-angles[1])
            sides.append(round(sqrt(sides[0]^2+sides[1]^2-2*sides[0]*sides[1]*cos(angles[2])),1))
            given = [f"{labels[0][1]}={angles[0]*180/pi}^\\circ",
                     f"{labels[0][0]}={sides[0]}",
                     f"{labels[1][0]}={sides[1]}"
                    ]
            found = [f"{labels[2][0]}={sides[2]}",
                     f"{labels[1][1]}={round(angles[1]*180/pi,1)}^\\circ",
                     f"{labels[2][1]}={round(angles[2]*180/pi,1)}^\\circ"
                    ]
            found=",".join(found[:-1])+r",\text{ and }"+found[-1]
            
        shuffle(given)
        tasks.append({"given": ",".join(given[:-1])+r",\text{ and }"+given[-1], 
                      "found": found 
                    })

        
        shuffle(tasks)
        return { "tasks": tasks,
        }
load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    def data(self):

        names=["Mateo", "Nina", "Ophelia", "Pierre", "Quinn", "Rosa", "Serena", "Thad", "Ursula","Victor"]

        scenario1=choice(["ladder","elevation","angleofclimb"])
        #Ladder against a building
        if scenario1=="ladder":
            ladder_length=choice([12,16,..,48])
            #Keep it 60-80 degrees ish
            height = choice([int(sin(pi/3)*ladder_length),..,int(sin(80/180*pi)*ladder_length)])
            angle = round(arcsin(height/ladder_length)*180/pi,1)
            variables1 = { "height": height,
                           "ladder": ladder_length,
                           "angle": angle
                         }
        #Angle of elevation/depression
        elif scenario1=="elevation":
            scenario=choice(["scenarioA","scenarioB"])
            units=choice(["ft","m"])
            if units=="ft":
                height=choice([500,600,..,4000])
            else:
                height=choice([100,150,..,1000])
            angle = choice([10..35])
            distance=round(height/sin(angle*pi/180),0)
            variables1={ scenario: {
                          "name": choice(names),
                          "units": units,
                          "height": height,
                          "angle": angle,
                          "distance": distance,
                          }
                       }
        #Airplane climbing
        elif scenario1=="angleofclimb":
            angle = choice([12..20])
            height= choice([5000,6000,..,20000])
            distance=round(height/tan(angle*pi/180),0)
            variables1={  "height": height,
                          "angle": angle,
                          "distance": distance,
                          "distance_miles": round(distance/5280,0),
                       }



        scenario2=choice(["airport","hiker","boats","ceiling","carpentersquare","bridge"])
        #SAS, Law of cosines
        if scenario2=="airport":
            plane1,plane2=sample([" Boeing 737", " Boeing 747", " Boeing 767", "n Airbus A320", "n Airbus A330", 
                                  " McDonnel Douglas MD11", " Bombardier CRJ200", "n Embraer E170"],2)
            d1,d2=sample([10..75],2)
            heading1,heading2=sample([10,20,..,350],2)
            distance=round(sqrt(d1^2+d2^2-2*d1*d2*cos(abs(heading1-heading2)*pi/180)),1)
            variables2={ "plane1": plane1,
                        "plane2": plane2,
                        "distance1": d1,
                        "distance2": d2,
                        "heading1": heading1,
                        "heading2": heading2,
                        "distance3": distance,
                        "units": choice(["miles","kilometers"])
                      }
        elif scenario2=="hiker":
            d1,d2=sample([2..10],2)
            angle=choice([20,25,..,80]+[100,105..,140])
            distance=round(sqrt(d1^2+d2^2-2*d1*d2*cos(pi-angle*pi/180)),1)
            variables2={ "distance1": d1,
                        "distance2": d2,
                        "angle": angle,
                        "direction": choice(["left","right"]),
                        "distance3": distance,
                        "units": choice(["miles","kilometers"])
                      }
        ##AAS Law of sines
        elif scenario2=="boats":
            angle1,angle2=sample([5,10,..,75],2)
            d1=choice([10..50])
            d2=round(d1*sin(angle2*pi/180)/sin(angle1*pi/180),1)
            d3=round(d1*sin((180-angle1-angle2)*pi/180)/sin(angle1*pi/180),1)
            variables2={ "angle1": angle1,
                         "angle2": angle2,
                         "distance1": d1,
                         "distance2": d2,
                         "distance3": d3,
                         "specifier": choice(["taller", "newer", "red"]),
                         "units": choice(["nautical miles", "miles", "kilometers"])
                       }
        elif scenario2=="ceiling":
            angle=choice([85,..,89]+[91..95])
            d=round(choice([2,2.25,..,5]),2)
            units=choice(["inches","centimeters"])
            if units=="centimeters":
                d=2*d
            e=round(d*sin(angle*pi/180)/sin((pi-angle*pi/180)/2),2)
            variables2={ "angle": angle,
                         "distance1": d,
                         "distance2": e,
                         "units": units,
                       }
        #SSS
        elif scenario2=="carpentersquare":
            angle=choice([85,..,89]+[91..95])
            d1,d2=sample([4,4.5,..,20],2)
            d3=round(sqrt(d1^2+d2^2-2*d1*d2*cos(angle*pi/180)),1)
            angle=round(arccos((d3^2-d1^2-d2^2)/(-2*d1*d2))*180/pi,1)
            units=choice(["inches","centimeters"])
            if units=="centimeters":
                d1,d2,d3=(2*d1,2*d2,2*d3)
            variables2={ "angle": angle,
                         "distance1": round(d1,1),
                         "distance2": round(d2,1),
                         "distance3": d3,
                         "units": units,
                       }
        elif scenario2=="bridge":
            d=sample([50..100],3)
            angle_choice = choice(["smallest","largest"])
            if angle_choice=="smallest":
                d.sort()
            else:
                d.sort(reverse=True)

            angle=round(arccos((d[0]^2-d[1]^2-d[2]^2)/(-2*d[1]*d[2]))*180/pi,1)
            shuffle(d)
            variables2={ 
                        "d1": d[0],
                        "d2": d[1],
                        "d3": d[2],
                        "angle_choice": angle_choice,
                        "angle": angle,
                        "units": choice(["feet", "meters"])
                       }


        tasks=[ {scenario1: {**variables1}}, {scenario2: {**variables2}}]
        shuffle(tasks)
        return { "tasks": tasks }
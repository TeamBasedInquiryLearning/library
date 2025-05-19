load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    def data(self):
        
        t1,t2 =  TBIL.special_angles(2,include_min=False)

        tasks=[ {"angler": t1, "angled": t1*360/(2*pi), "degrees": True, "angle": str(t1*360/(2*pi))+r"^\circ", "angle2": TBIL.typeset_angle(t1), "plot": "plotd"},
                {"angler": t2, "angled": t2*360/(2*pi), "degrees": False, "angle": TBIL.typeset_angle(t2), "angle2":str(t2*360/(2*pi))+r"^\circ", "plot": "plotr"},
              ]

        
        return {
            "tasks": tasks
        }
        
    @provide_data
    def graphics(data):
        if data["tasks"][0]["degrees"]:
            dangle=data["tasks"][0]["angler"]
            rangle=data["tasks"][1]["angler"]
        else:
            dangle=data["tasks"][1]["angler"]
            rangle=data["tasks"][0]["angler"]

        return {"plotd": TBIL.plot_angle(dangle,show_angle_value=True,degree_labels=True),
                "plotr": TBIL.plot_angle(rangle,show_angle_value=True),
                }
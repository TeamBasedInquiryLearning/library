load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    def data(self):

        t=[(arcsin,sin),(arccos,cos),(arctan,tan)]
        angles = TBIL.special_angles(3)
        if angles[2]==pi/2 or angles[2]==3*pi/2:
            angles[2]+=choice([pi/6,pi/4,pi/3])*choice([-1,1])
        tasks=[ {"f": f[0], "a": TBIL.typeset_angle(f[1](angles[i])), "value": TBIL.typeset_angle(angles[i])} for i,f in enumerate(t)]
        shuffle(tasks)

        itrig,domain,image = choice( [(arcsin,"[-1,1]", r"\left[-\dfrac{\pi}{2},\dfrac{\pi}{2}\right]"), (arccos, "[-1,1]", r"[0,\pi]"), (arctan, r"(-\infty,\infty)", r"\left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)") ])


        return {
            "itrig": itrig,
            "fname": choice(["f","g","h"]),
            "domain": domain,
            "range": image,
            "tasks": tasks,
        }

    @provide_data
    def graphics(data):
        p=Graphics()
        custom_ticks=[]
        custom_tick_labels=[]
        for xval in [-pi+i*pi/4 for i in [0.. 8]]:
            custom_ticks.append(xval)
            custom_tick_labels.append(TBIL.typeset_angle(xval,latex_delimiters=True))
        if data["itrig"]==arcsin:
            p=plot(arcsin(x),xmin=-1,xmax=1,ymin=-pi,ymax=pi,thickness=3,aspect_ratio=1,detect_poles=True,gridlines=True, ticks=[1,custom_ticks],tick_formatter=[SR(1),custom_tick_labels])
            p.SHOW_OPTIONS['xmin']=-pi
            p.SHOW_OPTIONS['xmax']=pi
        elif data["itrig"]==arccos:
            p=plot(arccos(x),xmin=-1,xmax=1,ymin=-pi,ymax=pi,thickness=3,aspect_ratio=1,detect_poles=True,gridlines=True, ticks=[1,custom_ticks],tick_formatter=[SR(1),custom_tick_labels])
            p.SHOW_OPTIONS['xmin']=-pi
            p.SHOW_OPTIONS['xmax']=pi
        elif data["itrig"]==arctan:
            p=plot(arctan(x),xmin=-pi,xmax=pi,ymin=-pi,ymax=pi,thickness=3,aspect_ratio=1,detect_poles=True,gridlines=True, ticks=[1,custom_ticks],tick_formatter=[SR(1),custom_tick_labels])
            p+=line([(-pi,pi/2),(pi,pi/2)],thickness=3,linestyle='dashed',color='red')
            p+=line([(-pi,-pi/2),(pi,-pi/2)],thickness=3,linestyle='dashed',color='red')
        else:
            print("Error")

        return {"plot": p
               }
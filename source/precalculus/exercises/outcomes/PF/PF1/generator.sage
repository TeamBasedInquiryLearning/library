load("../../../source/common/sagemath/library.sage")
class Generator(BaseGenerator):
    def data(self):
        
        a=choice([-1,1])*choice([2..5]) 
        b=choice([2..4])
        c=choice([-4..4])*b*pi*1/choice([1,2,3])
        amplitude=abs(a)
        period=2*pi/b
        phase_shift=abs(c/b)
        phase_shift_direction="right" if c<0 else "left"
        t=choice([sin,cos])
        f=a*t(b*x+c)

       
        return {
            "b": b, "c": c,
            "f": f,
            "fname": choice(["f","g","h"]),
            "fstring": f"{latex(a)} {latex(t)} \\left( {latex(b)} x {'+'+latex(c) if c>0 else ''} {'-'+latex(abs(c)) if c < 0 else ''} \\right)",
            "amplitude": amplitude,
            "period": period,
            "phase_shift": TBIL.typeset_angle(phase_shift),
            "direction": phase_shift_direction
        }
        
    @provide_data
    def graphics(data):
        return {"plot": TBIL.trig_plot(data["f"],(min(0,-data["c"]/data["b"]),max(0,-data["c"]/data["b"]+2*data["period"])),ticks=[pi/data["b"],1])
                }
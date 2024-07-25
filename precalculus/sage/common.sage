# Library of helpful functions
class TBILCalc:
    @staticmethod
    def numberline_plot(center=0, radius=10):
        P = arrow((center,0),(center-radius,0),color="black", width=1, arrowsize=1, aspect_ratio=1)
        P += arrow((center,0),(center+radius,0),color="black", width=1, arrowsize=1)
        for i in range(center-radius+1,center+radius):
            P += line([(i,-0.2),(i,0.2)],color="black")
            P += text(f"${i}$", (i,-0.6),color="black")
        return P
    
    @staticmethod
    def inequality_plot(
            start=None, 
            strict_start=True, 
            end=None, 
            strict_end=True,
            label_endpoints=True):
        P = Graphics()
        if start is None:
            P += arrow((end,0),(-10,0),color="#0088ff", width=3, arrowsize=3, aspect_ratio=1)
        if end is None:
            P += arrow((start,0),(10,0),color="#0088ff", width=3, arrowsize=3, aspect_ratio=1)
        if start is not None and end is not None:
            P += line([(start,0),(end,0)],color="#0088ff", thickness=3, aspect_ratio=1)

        if start is not None:
            if label_endpoints:
                P += text(f"${round(start,ndigits=2)}$", (start,0.6), color="black")
            if strict_start:
                P += text("(", (start,0), color="#0088ff", fontsize=18)
            else:
                P += text("[", (start,0), color="#0088ff", fontsize=18)

        if end is not None:
            if label_endpoints:
                P += text(f"${round(end,ndigits=2)}$", (end,0.6), color="black")
            if strict_end:
                P += text(")", (end,0), color="#0088ff", fontsize=18)
            else:
                P += text("]", (end,0), color="#0088ff", fontsize=18)
        return P
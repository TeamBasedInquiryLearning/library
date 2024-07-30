# Library of helpful functions
class TBILPrecal:
    @staticmethod
    def numberline_plot(center=0, radius=10):
        P = arrow((center-radius,0),(center+radius,0),color="black", width=1, arrowsize=1, aspect_ratio=1,head=2)
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

    @staticmethod
    def small_rationals(numerators=range(-8,9), 
                        denominators=[2,3,5],
                        dictionary=True,
                        length=1):
        '''Generates a list or dictionary of unique rational numbers with small numerators and denominators. 
        For a dictionary, keys are the rationals and values are the denominators.'''
        fulldict = {m/n:n for m in numerators for n in denominators if m%n !=0}
        dict= { num:fulldict[num] for num in sample(list(fulldict.keys()),length)}
        if dictionary:
            return dict
        return list(dict.keys())

    @staticmethod
    def small_irrationals(rational_part=range(-8,9), 
                          irrational_part=[2,3,5,6,7,8],
                          denominators=[i for i in range(-5,6) if i != 0],
                          dictionary=True,
                          length=1):
        '''Generates a list or dictionary of uniqe irrational numbers of the form (a+sqrt(b))/c. 
        For a dictionary, keys are tuples of rationals and their conjugate, and values are the denominators.'''
        fulldict = { ((a+sqrt(b))/c,(a-sqrt(b))/c):c for a in rational_part for b in irrational_part for c in denominators}
        dict= { pair:fulldict[pair] for pair in sample(list(fulldict.keys()),length)}
        if dictionary:
            return dict
        else:
            return list(dict.keys())
        
    @staticmethod
    def small_complex(real_part=range(-5,6), 
                      imaginary_part=[i for i in range(-5,6) if i != 0],length=1):
        '''Generates a list of unique 2-tuples of conjugate pairs of complex (not real) numbers of the form a+bi.'''
        return sample([(a+b*I,a-b*I) for a in real_part for b in imaginary_part],length)
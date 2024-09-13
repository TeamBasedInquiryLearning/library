# Library of helpful functions
class TBILPrecal:
    @staticmethod
    def numberline_plot(center=0, radius=10):
        P = arrow((center-radius,0),(center+radius,0),color="black", width=1, arrowsize=1, aspect_ratio=1,head=2)
        
        #Print approximately every (radius/10)-th label for longer lines
        label_skip=1
        if radius>10:
            label_skip=round(radius/10)

        for i in range(center-radius+1,center+radius):
            if i % label_skip == 0:
                P += line([(i,-0.2),(i,0.2)],color="black")
                P += text(f"${i}$", (i,-0.6),color="black")
        return P
    
    @staticmethod
    def inequality_plot(
            start=None, 
            strict_start=True, 
            end=None, 
            strict_end=True,
            label_endpoints=True,
            scale=10):
        P = Graphics()
        if start is None:
            P += arrow((end,0),(-1*scale,0),color="#0088ff", width=3, arrowsize=3, aspect_ratio=1)
        if end is None:
            P += arrow((start,0),(1*scale,0),color="#0088ff", width=3, arrowsize=3, aspect_ratio=1)
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
    def intervals_from_inequality(inequality, partition_points,undefined_points=[],checkpoints=None):
        '''Generates a list of strings which are the intervals on which inequality is true.
         Note that you must supply the partition_points, and it is assumed that the inequality
          is defined between them. '''
        #Remove duplicates
        partition_points=list(dict.fromkeys(partition_points))

        if not checkpoints:
            checkpoints=[partition_points[0]-1]
            for i in [0..len(partition_points)-2]:
                checkpoints.extend(1/2*(partition_points[i]+partition_points[i+1]))
            checkpoints.append(partition_points[-1]+1)
        if len(checkpoints)!=len(partition_points)+1:
            raise ValueError("Supplied list of checkpoints should contain one more item than list of partition points")

        intervals= []
        for i in range(0,len(checkpoints)):
            p=checkpoints[i]
            s=""
            if inequality.subs({x:p}): 
                if p<partition_points[0]:
                    if partition_points[0] not in undefined_points and inequality.subs({x:partition_points[0]}):
                        intervals.append(f"(-\\infty, {partition_points[0]}]")
                    else:
                        intervals.append(f"(-\\infty, {partition_points[0]})")
                elif p>partition_points[-1]:
                    if partition_points[-1] not in undefined_points and inequality.subs({x:partition_points[-1]}):
                        intervals.append(f"[{partition_points[-1]}, \\infty)")
                    else:
                        intervals.append(f"({partition_points[-1]}, \\infty)")
                else:
                    s=""
                    if partition_points[i] not in undefined_points and inequality.subs({x:partition_points[i]}):
                        s+="["
                    else:
                        s+="("
                    s+=f"{partition_points[i-1]}, {partition_points[i]}"
                    if partition_points[i] not in undefined_points and inequality.subs({x:partition_points[i]}):
                        s+="]"
                    else:
                        s+=")"

            if s != "":
                intervals.append(s)

        return intervals

    @staticmethod
    def numberline_from_intervals(intervals):
        #Assumes intervals are sorted and non-overlapping
        P=Graphics()
        scale=10
        interval_dict_list=[]
        for interval in intervals:
            interval_dict_list.append({})
            if interval[0] == "(":
                interval_dict_list[-1]["left_strict"]=True
            else:
                interval_dict_list[-1]["left_strict"]=False
            if interval[-1] == ")":
                interval_dict_list[-1]["right_strict"]=True
            else:
                interval_dict_list[-1]["right_strict"]=False
            
            #Discard opening ( or [ and closing ])
            interval=interval[1:-1]
            left,right = interval.split(",")
            left=left.strip()
            right=right.strip()
            if left == "-\\infty":
                interval_dict_list[-1]["left"]=None
            else:
                interval_dict_list[-1]["left"]=Rational(left)
                if abs(Rational(left))>= scale:
                    scale=abs(Rational(left))+3
            if right == "\\infty":
                interval_dict_list[-1]["right"]=None
            else:
                interval_dict_list[-1]["right"]=Rational(right)
                if abs(Rational(right))>= scale:
                    scale=abs(Rational(right))+3

        P+=TBILPrecal.numberline_plot(radius=scale)
        for i in interval_dict_list:
            P+=TBILPrecal.inequality_plot( start=i["left"], strict_start=i["left_strict"], 
            end=i["right"], strict_end=i["right_strict"], label_endpoints=False,scale=scale)
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
                          length=1,
                          full_list=False):
        '''Generates a list or dictionary of uniqe irrational numbers of the form (a+sqrt(b))/c. 
        For a dictionary, keys are tuples of rationals and their conjugate, and values are the denominators.'''
        fulldict = { ((a+sqrt(b))/c,(a-sqrt(b))/c):c for a in rational_part for b in irrational_part for c in denominators}
        if full_list:
            length=len(fulldict)
        dict= { pair:fulldict[pair] for pair in sample(list(fulldict.keys()),min(length,len(fulldict)))}
        if dictionary:
            return dict
        else:
            return list(dict.keys())
        
    @staticmethod
    def small_complex(real_part=range(-5,6), 
                      imaginary_part=[i for i in range(-5,6) if i != 0],length=1):
        '''Generates a list of unique 2-tuples of conjugate pairs of complex (not real) numbers of the form a+bi.'''
        return sample([(a+b*I,a-b*I) for a in real_part for b in imaginary_part],length)

    @staticmethod
    def line_from_points(point1,point2):
        '''Returns the equation of a line through the two given points'''
        if point1[0]==point2[0]:
            return x==point1[0]
        elif point1[1]==point2[1]:
            return y==point1[1]
        else:
            slope= (point2[1]-point1[1])/(point2[0]-point1[0])
            return TBILPrecal.line_from_point_slope(point1,slope)

    @staticmethod
    def line_from_point_slope(point,slope):
        '''Returns the equation of a line from a point and slope'''
        return y==slope*x+point[1]-slope*point[0]

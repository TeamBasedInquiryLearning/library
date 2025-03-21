class TBIL:

    # Precal/Cal

    @staticmethod
    def plot_angle(
        angle,
        reference_angle=0,
        show_axes=True,
        show_unit_circle=False,
        show_unit_point=False,
        label_unit_point=False,
        show_angle_value=False,
        show_reference_angle_value=False,
        show_triangle=False,
        triangle_labels=False,
        degree_labels=False,
    ):
        if degree_labels:
            angle_label = f"${latex(angle*180/pi)}^\\circ$"
            reference_angle_label = f"${latex(reference_angle*180/pi)}^\\circ$"
        else:
            angle_label = TBIL.typeset_angle(angle)
            reference_angle_label = TBIL.typeset_angle(reference_angle)

        reference_coordinate = (cos(reference_angle),sin(reference_angle))
        mid_reference_angle=reference_angle/2
        mid_reference_coordinate = (cos(mid_reference_angle),sin(mid_reference_angle))
        end_angle = reference_angle+angle
        end_coordinate = (cos(end_angle),sin(end_angle))
        mid_angle = reference_angle+angle/2
        mid_coordinate = (cos(mid_angle),sin(mid_angle))
        p=plot([],aspect_ratio=1,ticks=[[],[]])
        p+=arrow((0,0),reference_coordinate)
        p+=arrow((0,0),end_coordinate) #TODO hide arrowheads when show_unit_circle
        p+=arc((0,0),0.1,sector=(reference_angle, end_angle),color="black") #TODO add arrowhead
        if show_angle_value:
            if type(show_angle_value) is str:
                angle_value_label = show_angle_value
            else:
                angle_value_label = angle_label
            p+=text(angle_value_label,(0.2*c for c in mid_coordinate), fontsize="16")
        if show_reference_angle_value:
            p+=arc((0,0),0.1,sector=(0, reference_angle),color="black") 
            p+=text(reference_angle_label,(0.2*c for c in mid_reference_coordinate), fontsize="16")
        if show_unit_point:
            p+=point(end_coordinate,size="50",color="red")
        if label_unit_point:
            if type(label_unit_point) is tuple and len(label_unit_point)==2:
                label=f"$\\left({label_unit_point[0]},{label_unit_point[1]}\\right)$"
            else:
                label=f"$\\left({latex(cos(end_angle))},{latex(sin(end_angle))}\\right)$"
            p+=text(label, (1.4*c for c in end_coordinate),color="black",fontsize="18")
        if show_unit_circle:
            p+=circle((0,0),1,color="#ddd")
        if show_triangle:
            if cos(angle)*sin(angle)!=0:
                p+=line([(0,0),(end_coordinate[0],0),end_coordinate],color="green",thickness=2)
                #Little square in corner
                delta=0.08
                xdelta = -1*delta*cos(angle)/abs(cos(angle))
                ydelta = delta*sin(angle)/abs(sin(angle))
                p+=line([(end_coordinate[0],ydelta),(end_coordinate[0]+xdelta,ydelta),(end_coordinate[0]+xdelta,0)],color="green")
        if triangle_labels:
            if type(triangle_labels) is tuple and len(triangle_labels)==2:
                xlabel=triangle_labels[0]
                ylabel=triangle_labels[1]
            else:
                xlabel=f"${latex(cos(end_angle))}$"
                ylabel=f"${latex(sin(end_angle))}$"
            p+=text(xlabel, (0.5*end_coordinate[0],0.2),color="green",fontsize="14")
            p+=text(ylabel, (end_coordinate[0]+0.2, 0.5*end_coordinate[1]),color="green",fontsize="14")
            
        if not show_axes:
            p.axes(False)
        p.xmin(-1)
        p.xmax(1)
        p.ymin(-1)
        p.ymax(1)
        return p

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
        
        P.axes(False)
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
        P.axes(False)
        return P

    @staticmethod
    def intervals_from_inequality(inequality, partition_points,undefined_points=None,checkpoints=None):
        if undefined_points is None: undefined_points = []
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
                    if partition_points[i-1] not in undefined_points and inequality.subs({x:partition_points[i-1]}):
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

        P+=TBIL.numberline_plot(radius=scale)
        for i in interval_dict_list:
            P+=TBIL.inequality_plot( start=i["left"], strict_start=i["left_strict"], 
            end=i["right"], strict_end=i["right_strict"], label_endpoints=False,scale=scale)
        P.axes(False)
        return P

    @staticmethod
    def typeset_angle(theta):
        angle_string=f"${latex(theta)}$"
        if type(theta) is sage.symbolic.expression.Expression and theta.is_rational_expression() and denominator(theta)!=1:
            if numerator(theta)<0:
                angle_string = f"$-\\dfrac{{{latex(-1*numerator(theta))}}}{{{denominator(theta)}}}$"
            else:
                angle_string = f"$\\dfrac{{{latex(numerator(theta))}}}{{{denominator(theta)}}}$"
        return angle_string

    @staticmethod
    def trig_plot(f, *args, **kwds):
        if len(args)==0:
            raise ValueError("Second positional argument should be a tuple of the form (var, min, max) or (xmin, xmax)")
        if type(args[0]) is tuple and len(args[0])==2:
            xmin=args[0][0]
            xmax=args[0][1]
        elif type(args[0]) is tuple and len(args[0])==3:
            xmin=args[0][1]
            xmax=args[0][2]
        else:         
            xmin=0
            xmax=2*pi
        if 'ticks' not in kwds.keys():
            delta=pi/4
            yticks=0.5
        elif type(kwds['ticks']) is sage.symbolic.expression.Expression:
            delta=kwds['ticks']
            yticks=0.5
        elif type(kwds['ticks']) is list and len(kwds['ticks'])==2:
            delta=kwds['ticks'][0]
            yticks=kwds['ticks'][1]
        else:
            raise ValueError("Keywork argument ticks= should be either a symbolic expression or list of two symbolic expressions")
        custom_ticks=[]
        custom_tick_labels=[]
        for x in [xmin+delta*i for i in [0.. int((xmax-xmin)/delta)]]:
            custom_ticks.append(x)
            custom_tick_labels.append(TBIL.typeset_angle(x))
                
        #Default formatting
        if 'color' not in kwds.keys():
            kwds['color']='blue'
        if 'thickness' not in kwds.keys():
            kwds['thickness']=3
            
        kwds['ticks']=[custom_ticks,yticks]
        if yticks==1:
            yticklabel = SR(1)
        else:
            yticklabel = "latex"
        kwds['tick_formatter']=[custom_tick_labels,yticklabel]
                
        p=plot(f, *args, **kwds)
        return p


    @staticmethod
    def small_rationals(numerators=range(-8,9), 
                        denominators=None,
                        dictionary=True,
                        length=1):
        '''Generates a list or dictionary of unique rational numbers with small numerators and denominators. 
        For a dictionary, keys are the rationals and values are the denominators.'''
        if denominators is None: denominators = [2,3,5]
        fulldict = {m/n:n for m in numerators for n in denominators if m%n !=0}
        dict= { num:fulldict[num] for num in sample(list(fulldict.keys()),length)}
        if dictionary:
            return dict
        return list(dict.keys())

    @staticmethod
    def small_irrationals(rational_part=range(-8,9), 
                          irrational_part=None,
                          denominators=None,
                          dictionary=True,
                          length=1,
                          full_list=False):
        '''Generates a list or dictionary of uniqe irrational numbers of the form (a+sqrt(b))/c. 
        For a dictionary, keys are tuples of rationals and their conjugate, and values are the denominators.'''
        if irrational_part is None: irrational_part = [2,3,5,6,7,8]
        if denominators is None: denominators=[i for i in range(-5,6) if i != 0]
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
            return TBIL.line_from_point_slope(point1,slope)

    @staticmethod
    def line_from_point_slope(point,slope):
        '''Returns the equation of a line from a point and slope'''
        return y==slope*x+point[1]-slope*point[0]

    # Linear Algebra

    @staticmethod
    def config_matrix_typesetting():
        # globally set display of matrices
        latex.matrix_delimiters("[", "]")
        latex.matrix_column_alignment("c")

    class RowOp(SageObject):
        def __init__(self,optype,row1, row2, scalar=1):
            pm = "+"
            if scalar < 0:
                pm = "-"
            if optype == "elementary":
                self.string = f"R_{row1} {pm} {abs(scalar)} R_{row2} \\to R_{row1}"
            if optype=="diagonal":
                self.string = f"{scalar} R_{row1} \\to R_{row1}"
            if optype=="permutation":
                self.string = f"R_{row1} \\leftrightarrow R_{row2}"
            
        def _latex_(self):
            return self.string

    #Used for constructing things like solution sets of systems of equations
    class SetBuilder(SageObject):
        def __init__(self, element=None, predicate=None):
            self.element=element
            self.predicate=predicate
            
        def _latex_(self):
            if self.element==None:
                return r"\left\{\right\}"
            string=r"\left\{"+latex(self.element)
            if self.predicate==None:
                string+=r"\right\}"
            else:
                try:
                    iter(self.predicate)
                except TypeError:
                    pred = [self.predicate]
                else:
                    pred = self.predicate
                string+=r"\middle|\,"+"".join([latex(p) for p in pred])+r"\right\}"
            return string

    #Used to force Sage to use {} around a set -- sometimes Sage is dumb about this with vectors and matrices
    class BracedSet(SageObject):
        def __init__(self,list):
            self.list=list

        def _latex_(self):
            string=r"\left\{"
            for i in range(0,len(self.list)-1):
                string+= latex(self.list[i])+","
            string+= latex(self.list[-1])+r"\right\}"
            return string

    #Special case of BracedSet for vectors -- forces them into our standard column vectors
    class VectorSet(BracedSet):
        def __init__(self,vectors):
            self.list=[column_matrix(v) for v in vectors]

    #Similar to VectorSet, but for typesetting in prose, e.g. "The vectors v1,v2, and v3..."
    class VectorList(SageObject):
        def __init__(self,vectors):
            self.vecList=[column_matrix(v) for v in vectors]

        def _latex_(self):
            string=""
            for i in range(0,len(self.vecList)-1):
                string+= latex(self.vecList[i])+","
            string+= r"\text{ and }" + latex(self.vecList[-1])
            return string

    #Typeset a linear combination without simplifying, as Sage likes to do automatically
    class LinearCombination(SageObject):    
        def __init__(self,coeffs,vecs,parentheses=false):
            self.coefficients=[]
            self.vectors=[]
            self.length=min(len(coeffs),len(vecs))
            for i in range(0,self.length):
                self.coefficients.append(coeffs[i])
                self.vectors.append(vecs[i])
            self.parentheses=parentheses
    
        def _latex_(self):
            string=""
            for i in range(0,self.length-1):
                string+= latex(self.coefficients[i])
                if self.parentheses:
                    string+= r"\left("+latex(self.vectors[i])+r"\right)"
                else: 
                    string+=latex(self.vectors[i])
                string+="+"
            string+= latex(self.coefficients[-1])
            if self.parentheses:
                string+= r"\left("+latex(self.vectors[-1])+r"\right)"
            else: 
                string+=latex(self.vectors[-1])
            return string

    #Generic equation, which could be used with polynomial or matrix equations. Often used with a LinearCombination passed as leftside
    class Equation(SageObject):
        def __init__(self,leftside,rightside):
            self.lhs = leftside
            self.rhs = rightside
        def _latex_(self):
            return latex(self.lhs)+"="+latex(self.rhs)

    #Vector equation class
    class VectorEquation(Equation):
        def __init__(self,A,vars=None):
            self.matrix=A
            #Check if column subdivision exists
            if not self.matrix.subdivisions()[1]:
                self.matrix=self.matrix.augment(zero_vector(ZZ, len(self.matrix.columns())), subdivide=true)

            #if vars were not supplied, create them
            if not vars:
                vars = vector([var("x_"+str(i+1)) for i in range(0,len(self.matrix.subdivision(0,0).columns()))])
            
            super().__init__(TBIL.LinearCombination(vars,[column_matrix(c) for c in self.matrix.subdivision(0,0).columns()]), column_matrix(A.column(-1)))

    @staticmethod
    def choices_from_list(lst):
        """
        Given a list, return a list of choices in a canonical way,
        in a random order.
        The first item of the list is the "correct" choice.
        """
        choices = [
            {"item": lst[i],"correct":(i==0)} 
            for i in range(len(lst))
        ]
        shuffle(choices)
        for i in range(len(lst)):
            choices[i]["letter"] = chr(ord('a')+i)
        return choices

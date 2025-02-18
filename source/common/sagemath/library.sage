class TBIL:
    def plot_angle(angle, show_unit_circle=False, show_unit_point=False, show_angle_value=False):
        p=arrow((0,0),(1,0),aspect_ratio=1,ticks=[[],[]],xmin=-1,xmax=1,ymin=-1,ymax=1)
        p+=arrow((0,0),(cos(angle),sin(angle))) #hide arrowhead when show_unit_circle
        p+=arc((0,0),0.1,sector=(0, angle),color="black") #add arrowhead
        if show_angle_value:
            p+=text(f"${latex(angle)}$",(0.2*cos(angle/2),0.2*sin(angle/2)))
        if show_unit_point:
            p+=point((cos(angle),sin(angle)),size="50",color="red")
            p+=text(f"$\\left({latex(cos(angle))},{latex(sin(angle))}\\right)$", (1.2*cos(angle),1.2*sin(angle)),color="black") #todo add reference angles
        if show_unit_circle:
            p+=circle((0,0),1,color="#ddd")
        return p

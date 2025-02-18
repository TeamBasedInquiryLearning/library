class TBIL:
    def plot_angle(
        angle,
        reference_angle=0,
        show_axes=True,
        show_unit_circle=False,
        show_unit_point=False,
        show_angle_value=False
    ):
        reference_coordinate = (cos(reference_angle),sin(reference_angle))
        end_angle = reference_angle+angle
        end_coordinate = (cos(end_angle),sin(end_angle))
        mid_angle = reference_angle+angle/2
        mid_coordinate = (cos(mid_angle),sin(mid_angle))
        p=plot([],aspect_ratio=1,ticks=[[],[]])
        p+=arrow((0,0),reference_coordinate)
        p+=arrow((0,0),end_coordinate) #TODO hide arrowheads when show_unit_circle
        p+=arc((0,0),0.1,sector=(reference_angle, end_angle),color="black") #TODO add arrowhead
        if show_angle_value:
            p+=text(f"${latex(angle)}$",(0.2*c for c in mid_coordinate), fontsize="24")
        if show_unit_point:
            p+=point(end_coordinate,size="50",color="red")
            p+=text(f"$\\left({latex(cos(end_angle))},{latex(sin(end_angle))}\\right)$", (1.4*c for c in end_coordinate),color="black",fontsize="18")
        if show_unit_circle:
            p+=circle((0,0),1,color="#ddd")
        if not show_axes:
            p.axes(False)
        p.xmin(-1)
        p.xmax(1)
        p.ymin(-1)
        p.ymax(1)
        return p

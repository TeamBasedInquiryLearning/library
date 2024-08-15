x,y,z=var("x y z")
p = revolution_plot3d(x/2,(x,0,4), show_curve=False,parallel_axis="x",opacity=0.5,frame=False)
p += revolution_plot3d((4,z),(z,0,2), show_curve=False,parallel_axis="x",opacity=0.5)
p += revolution_plot3d((2,z),(z,0,1), show_curve=False,parallel_axis="x",opacity=1)
p += line([(0,0,-3), (0,0,3)],color="black",label="x")
p += line([(-1,0,0), (5,0,0)],color="black")
# p += text3d("Volume=∫A(x)dx",(4,0,2.5))
# p += text3d("Area=A(x)",(2,0,1.25))
p

x,y,z = var('x y z')
p = revolution_plot3d(x^2,(x,0,2), show_curve=True,parallel_axis="x",opacity=0.5,frame=False)
p += revolution_plot3d(4,(x,0,2), show_curve=True,parallel_axis="x",opacity=0.5)
p += revolution_plot3d((0,z),(z,0,4), show_curve=True,parallel_axis="x",opacity=0.5)
p += revolution_plot3d(2,(x,0,sqrt(2)), show_curve=True,parallel_axis="x",opacity=1)
p += line([(0,0,-5), (0,0,5)],color="black",label="x")
p += line([(-1,0,0), (4,0,0)],color="black")
p

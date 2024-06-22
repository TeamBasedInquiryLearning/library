x,y,z = var('x y z')
p = plot(x^2,(x,0,2),aspect_ratio=1,color='red')
p += line([(0,0),(0,4),(2,4)],color="red")
p

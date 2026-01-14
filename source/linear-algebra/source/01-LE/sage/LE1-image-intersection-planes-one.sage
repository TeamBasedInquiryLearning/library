x,y,z = var("x y z")
GREEN = "#90EE90"
BLUE = "#7070FF"
PURPLE = "#EE90EE"
RED = "#FF0000"
p = implicit_plot3d(-2*x+y+3*z==9,(x,-5,5),(y,-5,5),(z,-5,5),color=GREEN)
p += implicit_plot3d(x+2*z==7,(x,-5,5),(y,-5,5),(z,-5,5),color=BLUE)
p += implicit_plot3d(x+y+z==6,(x,-5,5),(y,-5,5),(z,-5,5),color=PURPLE)
p += arrow3d((0,0,0), (1,2,3), 1,color=RED,thickness=10)
p

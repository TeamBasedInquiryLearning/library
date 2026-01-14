x,y,z = var("x y z")
GREEN = "#90EE90"
BLUE = "#7070FF"
PURPLE = "#EE90EE"
RED = "#FF0000"
p = implicit_plot3d(x+y+3*z==3,(x,-5,5),(y,-5,5),(z,-5,5),color=GREEN)
p += implicit_plot3d(2*x-y-3*z==0,(x,-5,5),(y,-5,5),(z,-5,5),color=BLUE)
p += implicit_plot3d(x==3,(x,-5,5),(y,-5,5),(z,-5,5),color=PURPLE)
p

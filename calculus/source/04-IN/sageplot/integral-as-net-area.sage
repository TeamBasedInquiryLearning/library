def riemann_plot(f,a,b,n):
    a,b = sorted([a,b])
    delta = (b-a)/n
    p = plot(f,xmin=a-(b-a)/10,xmax=b+(b-a)/10,color='black')
    for k in range(n):
        x_0 = a+k*delta
        y_0 = f(x=x_0)
        if y_0 > 0:
            color = "#88f"
        elif y_0 < 0:
            color = "#f88"
        else:
            color = "gray"
        p += polygon([(x_0,f(x=x_0)),(x_0+delta,f(x=x_0)),(x_0+delta,0),(x_0,0)], color=color, edgecolor="black",aspect_ratio=0.5)
    return p

graphics_array([riemann_plot((x-2)*(x-4),0,5,n) for n in [6,16,41]])
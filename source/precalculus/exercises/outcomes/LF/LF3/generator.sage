load("../sage/common.sage")
class Generator(BaseGenerator):
  def data(self):

    x=var('x')
    y=var('y')
    #Task 1
    #Line containing two points
    task1={}
    task1_type = choice(["two_points","point_intercept","two_intercepts"])
    points1=[]
    if task1_type == "two_points":
      #Construct points in opposite quadrants
      if choice([True,False]):
        points1.append((choice([1..7]),choice([0..7])))
        points1.append((choice([-7..0]),choice([-7..0])))
      else:
        points1.append( (choice([1..7]),choice([-7..0])) )
        points1.append( (choice([-7..0]),choice([0..7])) ) 
      
      task1.update( { "point1":points1[0], "point2": points1[1]})

    elif task1_type == "point_intercept":
      points1.append( (choice([-7..-1,1..7]),choice([-7..-1,1..7])) ) 

      intercept=choice(["x","y"])
      intercept_value= choice([-6..-1,1..6])
      if intercept=="x":
        points1.append( (intercept_value,0) )
      else:
        points1.append( (0,intercept_value) )

      task1.update( {"point":points1[0], "int_type": intercept, "intercept": intercept_value})

    elif task1_type=="two_intercepts":
      x_intercept=choice([-6..-1,1..6])
      points1.append( (x_intercept,0) )
      y_intercept=choice([-6..-1,1..6])
      points1.append( (0,y_intercept) )
      task1.update( {"x_intercept": x_intercept, "y_intercept": y_intercept})

    line1 = TBILPrecal.line_from_points(points1[0],points1[1])

    #Task 2   
    #Point and slope
    task2={}
    task2_type = choice(["point_slope","intercept_slope"])
    
    slope = choice([-4..4])
    task2.update({"slope":slope})
    if task2_type == "point_slope":
      task2["point"]=( (choice([-5..5]),choice([-5..5])))
    elif task2_type == "intercept_slope":
      task2["int_type"]=choice(["x","y"])
      task2["intercept"] = choice([-6..-1,1..6])
      if task2["int_type"]=="x":
        task2["point"] = (task2["intercept"],0)
      if task2["int_type"]=="y":
        task2["point"] = (0,task2["intercept"])

    line2 = TBILPrecal.line_from_point_slope(task2["point"],slope)

    #Task 3
    variable = choice(["x","y"])
    value = choice([-7..7])

    #Task 4
    form = choice(["point_slope","slope_intercept","standard"])
    if form == "point_slope":
      point = (choice([-6..6]),choice([-6..6]))
      slope = choice([-3..-1,1..3])
      equation = y-point[1]== (x-point[0]).mul(slope,hold=True)
      line4 = equation.rhs().unhold()+point[1]
    elif form == "slope_intercept":
      b=choice([-6..6])
      slope = choice([-3..-1,1..3])
      equation = y==slope*x+b
      line4 = equation.rhs()
    elif form=="standard":
      A=choice([-6..-1,1..6])
      B=choice([-6..-1,1..6])
      C=choice([-7..7])
      equation = A*x+B*y==C
      line4 = -A/B*x+C/B


    return {
      "points1": points1,
      "line1": line1,
      task1_type: task1,
      "point2": task2["point"],
      "line2": line2,
      task2_type: task2,
      "var": variable,
      "value": value,
      "equation": equation,
      "line4": line4,
    } 

  @provide_data
  def graphics(data):
    #Graph for Task 1
    #p=Graphics()
    p1=plot(data["line1"].rhs(),-8,8,ymin=-8,ymax=8,thickness=2,gridlines=True,ticks=[1,1],aspect_ratio=1)
    p1+=point(data["points1"],size=30)

    p2=plot(data["line2"].rhs(),-8,8,ymin=-8,ymax=8,thickness=2,gridlines=True,ticks=[1,1],aspect_ratio=1)
    p2+=point(data["point2"],size=30)

    p3=Graphics()
    if data["var"]=="x":
      p3+=line([(data["value"],-8),(data["value"],8)],xmin=-8,xmax=8,ymin=-8,ymax=8,thickness=2,gridlines=True,ticks=[1,1],aspect_ratio=1)
    elif data["var"]=="y":
      #p3+=parametric_plot((x,data["value"]),(x,-8,8),ymin=-8,ymax=8,thickness=2,gridlines=True,ticks=[1,1],aspect_ratio=1)
      p3+=plot(data["value"],-8,8,ymin=-8,ymax=8,thickness=2,gridlines=True,ticks=[1,1],aspect_ratio=1)

    p4 = plot(data["line4"],-8,8,ymin=-8,ymax=8,thickness=2,gridlines=True,ticks=[1,1],aspect_ratio=1)
        
    return {"plot1":p1, "plot2":p2, "plot3": p3, "plot4": p4}
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

    return {
      "points1": points1,
      "line1": line1,
      task1_type: task1,
      #"point3": 5,
      #"int_type": 6,
      #"intercept1": 7, 
      #"intercept2": 8, 
      #"intercept3": 9, 
      "point4": 10,
      "slope1":11,
      "slope2": 12,
      "intercept4": 13,
      "x_or_y": 14,
      "value": 15,  
      "equation": 16,
    } 

  @provide_data
  def graphics(data):
    #Graph for Task 1
    p=Graphics()
    p=plot(data["line1"].rhs(),-8,8,ymin=-8,ymax=8,thickness=2,gridlines=True,ticks=[1,1],aspect_ratio=1)
    p+=point(data["points1"],size=30)
        
    return {"plot1":p}
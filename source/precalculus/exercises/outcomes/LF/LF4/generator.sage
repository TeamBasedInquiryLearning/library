class Generator(BaseGenerator):
  def data(self):

    x=var('x')
    y=var('y')
    #Shuffle which task asks for parallel, which for perpindicular
    (orientation1,orientation2) = tuple(sample(["perpindicular","parallel"],2))

    #Task 1
    variable = choice(["a","b","c","d"])

    range = 6
    #Get two given points
    points = sample([(i,j) for i in [-1*range..range] for j in [-6..6]],2)
    #Choose third point so that line is not horizontal or vertical and points[0] is not repeated
    points.append( (choice([i for i in [-1*range..range] if i != points[1][0] and i!= points[0][0]]),
                    choice([i for i in [-1*range..range] if i != points[1][1] and i!= points[0][1]]) ) )
    
    m = (points[2][1]-points[1][1])/(points[2][0]-points[1][0])

    if orientation1=="parallel":
      m2=m
    elif orientation1=="perpindicular":
      m2=-1/m

    #Vary whether solving for x or y component
    solve_component = choice(["x","y"])
    if solve_component == "x":
      point1 = (variable, choice([i for i in [-1*range..range] if i != points[0][1]]))
      a= 1/m2*(point1[1]-points[0][1])+points[0][0]
    elif solve_component == "y":
      point1 = (choice([i for i in [-1*range..range] if i != points[0][0]]),variable)
      a = m2*(point1[0]-points[0][0])+points[0][1]

    #Task2
    line = choice([-8..-1,1..8])*x+choice([-8..-1,1..8])*y==choice([-10..10])

    point5=(choice([-1*range..range]),choice([-1*range..range]))
    #If point is on line, move it a bit
    if line.subs({x:point5[0],y:point5[1]}):
      point5=(point5[0],point5[1]+choice([-4..-1,1..4]))

    slope = -1*line.lhs().coefficients(x)[1][0]/line.lhs().coefficients(y)[1][0]
    if orientation1=="parallel":
      slope2=slope
    elif orientation1=="perpindicular":
      slope2=-1/slope
    new_line = y-point5[1]==(x-point5[0]).mul(slope2,hold=True)

    return {
      "var": variable,
      "orientation1": orientation1,
      #Passing the tuple results in odd typesetting of the variable
      "point1": f"({point1[0]},{point1[1]})",
      "point2": points[0],
      "point3": points[1],
      "point4": points[2],
      "answer": a,
      "orientation2": orientation2,
      "point5": point5,
      "line": line,
      "new_line": new_line,

    } 
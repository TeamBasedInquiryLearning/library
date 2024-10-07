class Generator(BaseGenerator):
  def data(self):
    x=var('x')
    y=var('y')

    #Task 1
    #Generate a line in standard form
    A=choice([-10..-1,1..10])
    B=choice([-10..-1,1..10])
    C=choice([-10..10])
    line1 = A*x+B*y == C
    slope1= -A/B
    yint1 = C/B

    #Task 2
    #Given graph
    point2 = (choice([-5..5]),choice([-5..5]))
    #If point is in quadrant 2 or 4, slope down.  Otherwise, positive slope
    #This helps ensure graph doesn't stretch out too much vertically
    if (point2[0] <0 and point2[1] > 0) or (point2[0]>0 and point2[1] < 0):
      #Trick Sage into making it a fraction 
      slope2=choice([-6,..,-2])/2
    else:
      slope2=choice([1,..,6])/2
    line2_ps = y-point2[1]==(x-point2[0]).mul(slope2,hold=True)
    line2_si = y==slope2*x+(point2[1]-slope2*point2[0])

    #Give slope and point
    slope3=choice([-8..-1,1..8])
    point3 = (choice([-10..10]),choice([-10..10]))
    line3_ps = y-point3[1]==(x-point3[0]).mul(slope3,hold=True)
    line3_si = y==slope3*x+(point3[1]-slope3*point3[0])

    #Give two points
    (a,b,c,d) = sample([-10..10],4)
    point4_1 = (a,b)
    point4_2 = (c,d)
    slope4 =  (point4_1[1]-point4_2[1])/(point4_1[0]-point4_2[0])
    line4_ps = y-point4_1[1]==(x-point4_1[0]).mul(slope4,hold=True)
    line4_si = y==slope4*x+(point4_1[1]-slope4*point4_1[0])


    return {
      "line1": line1,
      "slope1": slope1,
      "yint1": yint1,
      "line2_si": line2_si, 
      "line2_ps": line2_ps,
      "slope3": slope3, 
      "point3": point3,
      "line3_si": line3_si, 
      "line3_ps": line3_ps,
      "point4_1": point4_1,
      "point4_2": point4_2,
      "line4_si": line4_si, 
      "line4_ps": line4_ps,
    } 

  @provide_data
  def graphics(data):
    p=plot(data["line2_si"].rhs(),-10,10,ymin=-10,ymax=10,thickness=2,gridlines=True,ticks=[1,1],aspect_ratio=1)
    return {"plot":p}

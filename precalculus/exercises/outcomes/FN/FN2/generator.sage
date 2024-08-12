class Generator(BaseGenerator):
  def data(self):
    (fname,gname)=sample(["f","g","h"],2)

    types = sample(["polynomial","radical","rational"],2)
    cut=choice([-2..2])

    pieces=[]
    for type in types:
      if type == "polynomial":
        pieces.append(choice([1..3])*x^choice([2,3])+choice([-3..3])*x^choice([0,1]))
      if type == "radical":
        pieces.append(sqrt(choice([1,3])*x^2+choice([1,5])))
      if type == "rational":
        pieces.append((choice([1,4])*x+choice([-4..4]))/(choice([1,2])*x^2+choice([1..5])))
    
    f1(x)=pieces[0]
    f2(x)=pieces[1]

    #f1(x)=-x^2
    #f2(x)=x^3

    cut_left = choice([True,False])
    if cut_left:
      intervals=[[-5,cut],(cut,5)]
    else:
      intervals=[(-5,cut),[cut,5]]
    f(x) = piecewise([(intervals[0], f1(x)), (intervals[1], f2(x))])
    flatex=r"\begin{cases}"+latex(f1(x))
    if cut_left: 
      flatex += r"& -5 < x \leq "
    else:
      flatex += r"& -5 < x < "
    flatex +=str(cut)+r" \\ "+ latex(f2(x))+r" & "+ str(cut) 
    if cut_left:
      flatex+=r" < x < 5 "
    else:
      flatex+=r" \leq x < 5 "
    flatex+=r"\end{cases}"

    x1=choice([-4..cut-1])
    x2=choice([cut+1..4])

    tasks= [ {"value": x1, "result": f(x1)}, {"value": x2, "result": f(x2)}, {"value":cut, "result":f(cut)}]
    shuffle(tasks)


    #R.<z> = PolynomialRing(QQ)

    level=choice([-5..-1,1..5])
    xpoints=sample([-6..6],3)
    xpoints.sort()
    pieces=[]
    left=xpoints[0]-choice([1..3])
    domain=[left]
    slope=choice([-3..-1,1..3])
    for i in [0..len(xpoints)-1]:
      if i == len(xpoints)-1:
        domain.append(xpoints[i]+choice([1..3]))
        pieces.append( ((left, domain[1]), (-1)^i*slope*(x-xpoints[i])+level))
      else:
        right=1/2*(xpoints[i]+xpoints[i+1])
        pieces.append( ((left, right), (-1)^i*slope*(x-xpoints[i])+level))
        left=right


    xvalue=choice([domain[0]..domain[1]])
    gxvalue=None
    for p in pieces:
      if p[0][0] <= xvalue and xvalue <= p[0][1]:
        gxvalue = p[1].subs({x:xvalue})

    return {
      "fname": fname,
      "f":flatex,
      "tasks":tasks,
      "gname": gname,
      "g_pieces":pieces,
      "g_domain":domain,
      "xvalue":xvalue, 
      "gx":gxvalue,
      "result":level,
      "values": [{"x": i} for i in xpoints]
    } 


  @provide_data
  def graphics(data):
    p=Graphics()
    for piece in data["g_pieces"]:
      p+=plot(piece[1],piece[0][0],piece[0][1],thickness=3,gridlines=True,ticks=[1,1])
    #If you return plot(p) the gridlines disappear, so return p
    return {"plot": p}
      